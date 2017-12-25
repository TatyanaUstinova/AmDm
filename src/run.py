# coding: utf-8

from app import SearchResult, Song, Artist
import user_input


if __name__ == "__main__":
    print("\nAmdm\n")

    sign = user_input.get_user_sign()

    search_result = SearchResult(sign)
    artist_url = search_result.get_artist_url()

    artist = Artist(artist_url)
    print("\n{}\n".format(artist.name))

    songs = artist.get_songs()
    for num, song in enumerate(songs, 1):
        print("{}. {}\n".format(num, song))

    songs_amount = len(songs)

    def process_input(number):
        return user_input.check_user_int(user_input.cast_to_int(number), songs_amount)

    song_number = user_input.cast_to_int(user_input.get_user_song(process_input))

    chosen_song = songs[song_number - 1]
    print("\n{}\n".format(chosen_song))

    chords = chosen_song.text
    print("\n{}\n".format(chords))

    directory_name = user_input.get_user_saving_details()
    if directory_name:
        chosen_song.save_chords_text(directory_name)
        chosen_song.save_chords_img(directory_name)
