# coding: utf-8

import unittest

from app import SearchResult, Song, Artist


class AmDmTestCase(unittest.TestCase):

    EN_SIGNS = [
        {
            "sign": "green day",
            "search_url": "https://amdm.ru/search/?q=green%20day"
        },
        {
            "sign": "guns n roses",
            "search_url": "https://amdm.ru/search/?q=guns%20n%20roses"
        },
        {
            "sign": "milky chance",
            "search_url": "https://amdm.ru/search/?q=milky%20chance"
        }
    ]

    RU_SIGNS = [
        {
            "sign": "би 2",
            "search_url": "https://amdm.ru/search/?q=%D0%B1%D0%B8%202"
        },
        {
            "sign": "чайф",
            "search_url": "https://amdm.ru/search/?q=%D1%87%D0%B0%D0%B9%D1%84"
        },
        {
            "sign": "ария",
            "search_url": "https://amdm.ru/search/?q=%D0%B0%D1%80%D0%B8%D1%8F"
        }
    ]

    EN_ARTISTS = [
        {
            "name": "Green Day",
            "url": "https://amdm.ru/akkordi/green_day/"
        },
        {
            "name": "Guns N Roses",
            "url": "https://amdm.ru/akkordi/guns_n_roses/"
        },
        {
            "name": "Milky Chance",
            "url": "https://amdm.ru/akkordi/milky_chance/"
        }
    ]

    RU_ARTISTS = [
        {
            "name": "Би-2",
            "url": "https://amdm.ru/akkordi/bi_2/"
        },
        {
            "name": "Чайф",
            "url": "https://amdm.ru/akkordi/chaif/"
        },
        {
            "name": "Ария",
            "url": "https://amdm.ru/akkordi/aria/"
        }
    ]

    EN_SONGS = [
        {
            "number": 6,
            "name": "21 Guns",
            "url": "https://amdm.ru/akkordi/green_day/95030/21_guns/"
        },
        {
            "number": 116,
            "name": "Patience (crd)",
            "url": "https://amdm.ru/akkordi/guns_n_roses/7507/patience_crd/"
        },
        {
            "number": 5,
            "name": "Flashed Junk Mind",
            "url": "https://amdm.ru/akkordi/milky_chance/157186/flashed_junk_mind/"
        }
    ]

    RU_SONGS = [
        {
            "number": 118,
            "name": "Мой рок-н-ролл",
            "url": "https://amdm.ru/akkordi/bi_2/93443/moy_rok_n_roll/"
        },
        {
            "number": 34,
            "name": "Бутылка кефира, полбатона",
            "url": "https://amdm.ru/akkordi/chaif/136559/butilka_kefira_polbatona/"
        },
        {
            "number": 308,
            "name": "Штиль",
            "url": "https://amdm.ru/akkordi/aria/92710/shtil/"
        }
    ]

    MILKY_CHANCE_SONGS = [
        ("Becoming", "https://amdm.ru/akkordi/milky_chance/153446/becoming/"),
        ("Down By The River", "https://amdm.ru/akkordi/milky_chance/129556/down_by_the_river/"),
        ("Fairytale", "https://amdm.ru/akkordi/milky_chance/121809/fairytale/"),
        ("Feathery", "https://amdm.ru/akkordi/milky_chance/129039/feathery/"),
        ("Flashed Junk Mind", "https://amdm.ru/akkordi/milky_chance/157186/flashed_junk_mind/"),
        ("Loveland", "https://amdm.ru/akkordi/milky_chance/153126/loveland/"),
        ("Roxanne", "https://amdm.ru/akkordi/milky_chance/143121/roxanne/"),
        ("Stolen Dance", "https://amdm.ru/akkordi/milky_chance/129316/stolen_dance/"),
        ("Stolen Dance", "https://amdm.ru/akkordi/milky_chance/137538/stolen_dance/"),
        ("Stolen Dance", "https://amdm.ru/akkordi/milky_chance/136771/stolen_dance/"),
        ("The Unknown Song", "https://amdm.ru/akkordi/milky_chance/153132/the_unknown_song/")
    ]

    def test_get_search_result_url(self):

        for en_sign in AmDmTestCase.EN_SIGNS:
            search_result = SearchResult(en_sign["sign"])
            self.assertEqual(search_result.get_search_result_url(), en_sign["search_url"])

        for ru_sign in AmDmTestCase.RU_SIGNS:
            search_result = SearchResult(ru_sign["sign"])
            self.assertEqual(search_result.get_search_result_url(), ru_sign["search_url"])

    def test_get_artist_url(self):

        for en_sign, en_artist in zip(AmDmTestCase.EN_SIGNS, AmDmTestCase.EN_ARTISTS):
            search_result = SearchResult(en_sign["sign"])
            self.assertEqual(search_result.get_artist_url(), en_artist["url"])

        for ru_sign, ru_artist in zip(AmDmTestCase.RU_SIGNS, AmDmTestCase.RU_ARTISTS):
            search_result = SearchResult(ru_sign["sign"])
            self.assertEqual(search_result.get_artist_url(), ru_artist["url"])

    def test_get_artist_name(self):

        for en_artist in AmDmTestCase.EN_ARTISTS:
            artist = Artist(en_artist["url"])
            self.assertEqual(artist.name, en_artist["name"])

        for ru_artist in AmDmTestCase.RU_ARTISTS:
            artist = Artist(ru_artist["url"])
            self.assertEqual(artist.name, ru_artist["name"])

    def test_get_songs(self):

        milky_chance = AmDmTestCase.EN_ARTISTS[2]
        artist = Artist(milky_chance["url"])

        songs =artist.get_songs()

        for song, mc_song in zip(songs, AmDmTestCase.MILKY_CHANCE_SONGS):
            self.assertIsInstance(song, Song)
            self.assertEqual(song.name, mc_song[0])
            self.assertEqual(song.url, mc_song[1])

    def test_get_song(self):

        for en_artist, en_song in zip(AmDmTestCase.EN_ARTISTS, AmDmTestCase.EN_SONGS):

            artist = Artist(en_artist["url"])
            songs = artist.get_songs()

            chosen_song = songs[en_song["number"] - 1]

            self.assertEqual(chosen_song.name, en_song["name"])
            self.assertEqual(chosen_song.url, en_song["url"])

        for ru_artist, ru_song in zip(AmDmTestCase.RU_ARTISTS, AmDmTestCase.RU_SONGS):

            artist = Artist(ru_artist["url"])
            songs = artist.get_songs()

            chosen_song = songs[ru_song["number"] - 1]

            self.assertEqual(chosen_song.name, ru_song["name"])
            self.assertEqual(chosen_song.url, ru_song["url"])


if __name__ == "__main__":
    unittest.main()
