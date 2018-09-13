# import all necessary libraries
import pandas as pd
from get_u_input_test import get_genre
import random
global genres


# Loop that gets user input
def get_genre_song():
    # defining global variable genres as an array obtained from user input
    global genres
    genres = get_genre()

    # load in dataframe from the data structure we did earlier
    music_lib = pd.read_csv('music_lib_final.csv')

    # setting a variable = the length of the dataframe
    length = len(music_lib)

    # setting a variable = the length of the genres array from user input
    length_2 = len(genres)

    # creating an array of songs to chose from
    songs = []

    # some dummy variables for counting
    x = 0
    y = 1

    # for loop to parse data from each row in the dataframe
    for n in range(0, length, 1):
        # setting a variable = the nth row in the dataframe
        track = music_lib[x:y]

        # increase the dummy variables by one
        x += 1
        y += 1

        # parse the genre from the dataframe
        genre_pre = str(track['Genre'].values)
        genre = genre_pre[2:-2]

        # parse the song title from the dataframe
        song_pre = str(track['Song Title'].values)
        song = song_pre[2:-2]

        # parse the song duration from the dataframe
        song_duration_pre = str(track['Song Duration'].values)
        song_duration_pre_2 = song_duration_pre[1:-1]
        song_duration = float(song_duration_pre_2)

        # loop to decide if the song is the correct genre
        for k in range(0, length_2, 1):
            if genre == str(genres[k]):
                temp = [song, song_duration, x, y]

                # add the given song to the list of songs if it is the genre that the user selected
                songs.append(temp)

    # setting a variable = the amount of songs that have been chosen to be in the correct genre(s)
    songs_length = len(songs)

    # generate a random integer from 0 to the length of the list
    rand = random.randrange(0, songs_length, 1)

    # return the song
    return songs[rand]

# get_genre_song()

# all of that repeated, but it doesn't ask for the user to select genre again
def get_song():
    global genres
    music_lib = pd.read_csv('music_lib_final.csv')
    length = len(music_lib)
    length_2 = len(genres)

    songs = []

    x = 0
    y = 1

    for n in range(0, length, 1):
        track = music_lib[x:y]
        x += 1
        y += 1
        genre_pre = str(track['Genre'].values)
        genre = genre_pre[2:-2]
        song_pre = str(track['Song Title'].values)
        song = song_pre[2:-2]
        song_duration_pre = str(track['Song Duration'].values)
        song_duration_pre_2 = song_duration_pre[1:-1]
        song_duration = int(song_duration_pre_2)

        for k in range(0, length_2, 1):
            if genre == str(genres[k]):
                temp = [song, song_duration]
                songs.append(temp)
    songs_length = len(songs)
    rand = random.randrange(0, songs_length, 1)
    print(songs[rand])
