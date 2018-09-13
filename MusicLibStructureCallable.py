# import all necessary libraries
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import time


def data_restructure(path):
    print('Structuring Music Library...')
    # opening the XML file
    music_lib = open(path)

    # creating a beautiful soup object
    soup = BeautifulSoup(music_lib, 'xml')

    # an empty list to store tracks
    track_list = []

    # for loop to cut out the track data
    for track in soup.find_all('TRACK'):
        track_list.append(track)

    # converting to a numpy array
    music_pre_df = (np.array(track_list))

    # chopping off unwanted rows
    music_df = music_pre_df[:1180]

    # setting the counters
    x = 0
    y = 1

    # creating some more empty lists
    music_array = []
    bpm_array = []
    genre_array = []
    duration_array = []
    key_array = []
    score = []


    #for loop to cut out everything except for track title and bpm
    for tracks in music_df:

        # selecting which row and converting it into a string
        line = np.array_str(music_df[x:y])

        #print(line)

        # finding the beginning of the track name
        start = line.find('Name="') + 6

        # finding the end of the track name
        end = line.find('PlayCount') - 2

        # creating a string of the track name
        song_name_pre = line[start:end]
        song_name = song_name_pre.replace('&amp;', '&')

        # same process repeated...
        line_2 = np.array_str(music_df[x:y])
        start_2 = line.find('AverageBpm="') + 12
        end_2 = line.find('BitRate="') - 2
        bpm = line_2[start_2:end_2]

        line_3 = np.array_str(music_df[x:y])
        start_3 = line_3.find('Genre="') + 7
        end_3 = line_3.find('Grouping="') - 2
        genre_pre = line_3[start_3:end_3]

        genre_1 = genre_pre.replace('&amp;', '&')
        genre = genre_1.replace('Hip-Hop', 'Hip Hop')

        line_4 = np.array_str(music_df[x:y])
        start_4 = line_4.find('TotalTime="') + 11
        end_4 = line_4.find('TrackID="') - 2
        duration = line_4[start_4:end_4]

        line_5 = np.array_str(music_df[x:y])
        start_5 = line_5.find('Tonality="') + 10
        end_5 = line_5.find('TotalTime="') - 2
        key = line_5[start_5:end_5]

        # increasing the counters by one
        x += 1
        y += 1

        # adding the parsed data as rows at the bottom of the arrays
        bpm_array.append(bpm)
        music_array.append(song_name)
        genre_array.append(genre)
        duration_array.append(duration)
        key_array.append(key)
        score.append(0)

    # making a new 6d array based on the six 1d arrays the for loop made
    music_array = np.vstack((music_array, bpm_array, duration_array, genre_array, key_array, score)).T

    # converting the array into a data frame
    df = pd.DataFrame(music_array, columns=['Song Title', 'Song BPM', 'Song Duration', 'Genre', 'Key', 'Score'])

    # saving the data frame to a csv
    df.to_csv('music_lib_final_test.csv')

    # printing out the array for debugging
    #print(music_array)
    print('Done')
