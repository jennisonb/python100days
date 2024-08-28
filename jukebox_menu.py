from nested_data import albums

SONGS_LIST_INDEX = 3

while True:
    print("=" * 50)
    print("Please choose your album (invlid choice exits): ")
    # list the albums and offer a choice
    for index, (title, artist, year, songs) in enumerate(albums):
        print(f"{index +1}.\t{title}")
    album_choice = int(input("=> "))

    if album_choice < 1 or album_choice > len(albums):
        break
    else:
        album_title = albums[album_choice - 1][0]
        album_artist = albums[album_choice - 1][1]
        print(f"Please choose your song for the {album_title} album: ")
        chosen_album_songs = albums[album_choice - 1][SONGS_LIST_INDEX]
        for index, (track_num, song_title) in enumerate(chosen_album_songs):
            print(f"{track_num}.\t{song_title}")
        song_choice = int(input("=> "))

        if song_choice < 1 or song_choice > len(chosen_album_songs):
            print("Invlid song choice")
        else:
            chosen_song_title = chosen_album_songs[song_choice - 1][1]
            print(
                f'\nNow playing "{chosen_song_title}" from {album_artist}\'s "{album_title}" album...\n'
            )
