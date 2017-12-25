# coding: utf-8

import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup
import os
from contextlib import closing


class BaseSoup(object):

    @staticmethod
    def parse_html(url):
        """
        Parses the HTML code.
        :param url: the URL of a web page
        :return:
        """

        with closing(urllib.request.urlopen(url)) as content:
            html = content.read()
            soup = BeautifulSoup(html, "html.parser")

            return soup


class SearchResult(BaseSoup):
    """
    'цой' -> 'https://amdm.ru/akkordi/viktor_coi/'
    """

    def __init__(self, sign):

        self.sign = sign

        search_url = self._get_search_result_url()

        self.soup = self.parse_html(search_url)

    def _get_search_result_url(self):
        """
        Gets the URL of search result page.
        :return:
        """

        search_url = "https://amdm.ru/search/?q={}".format(urllib.parse.quote(self.sign))

        return search_url

    def get_artist_url(self):
        """
        Gets the URL of the artist page.
        :return:
        """

        table = self.soup.find("table", {"class": "items"})
        rows = table.findAll("tr")
        href = rows[1].findAll("a", {"class": "artist"})[0]["href"]

        artist_url = "https:{}".format(href)

        return artist_url


class Song(BaseSoup):
    """
    Artist('https://amdm.ru/akkordi/viktor_coi/'), 'Следи за собой',
    'https://amdm.ru/akkordi/viktor_coi/14639/sledi_za_soboy/' -> chords
    """

    def __init__(self, artist, name, url):

        self.artist = artist
        self.name = name
        self.url = url
        self.chords = None
        self._soup = None

    def __str__(self):
        return "{} \U0001F3B5 {}".format(self.name, self.url)  # \U0001F31F (star)

    @property
    def soup(self):
        if not self._soup:
            self._soup = self.parse_html(self.url)
        return self._soup

    @property
    def text(self):
        """
        Gets the chords text of the song.
        :return:
        """

        pre = self.soup.find("pre", {"itemprop": "chordsBlock"})

        chords = pre.get_text()

        self.chords = chords

        return chords

    def save_chords_text(self, local_directory):
        """
        Saves the chords to local directory.
        :param local_directory: the local directory name where the chords will be saved
        :return:
        """

        text = "{}\n\n{}\n\n{}".format(self.artist.name, self.name, self.text)

        name_to_save = "_".join("{}_{}.txt".format(self.artist.name, self.name).split())
        file_path = os.path.join(local_directory, name_to_save)

        with open(file_path, "w") as f:
            f.write(text)

    def save_chords_img(self, local_directory):
        """
        Saves the chords images to local directory.
        :param local_directory: the local directory name where the images will be saved
        :return:
        """

        images = self.soup.find("div", {"id": "song_chords"})

        for img in images.findAll("img"):
            src = img["src"]

            src_url = "https:{}".format(src)

            content = urllib.request.urlopen(src_url)

            file_name = os.path.split(src_url)[1]
            base_name = os.path.splitext(file_name)[0]  # without extension
            name_to_save = "{}.png".format(base_name)
            file_path = os.path.join(local_directory, name_to_save)

            with open(file_path, "wb") as f:
                f.write(content.read())


class Artist(BaseSoup):
    """
    'https://amdm.ru/akkordi/viktor_coi/' -> name, songs[Song]
    """

    def __init__(self, url):

        self.soup = self.parse_html(url)

        self.name = self.soup.find("h1").string

    def get_songs(self):
        """
        Gets all songs of specific artist.
        :return:
        """

        table = self.soup.find("table", {"id": "tablesort"})
        songs = []

        for row in table.findAll("tr")[1:]:
            song = row.find("a", {"class": "g-link"})

            song_name = song.string
            href = song["href"]

            song_url = "https:{}".format(href)

            songs.append(Song(self, song_name, song_url))

        return songs
