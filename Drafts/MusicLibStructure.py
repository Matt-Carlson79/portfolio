# import all necessary libraries
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import time

# opening the XML file
music_lib = open('MusicLibrary.XML')

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


#for loop to cut out everything except for track title and bpm
for tracks in music_df:

    # selecting which row and converting it into a string
    line = np.array_str(music_df[x:y])

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

    genre = genre_pre.replace('&amp;', '&')

    line_4 = np.array_str(music_df[x:y])
    start_4 = line_4.find('TotalTime="') + 11
    end_4 = line_4.find('TrackID="') - 2
    duration = line_4[start_4:end_4]

    # increasing the counters by one
    x += 1
    y += 1

    # adding the parsed data as rows at the bottom of the arrays
    bpm_array.append(bpm)
    music_array.append(song_name)
    genre_array.append(genre)
    duration_array.append(duration)

# making a new 2d array based on the two 1d arrays the for loop made
music_array = np.vstack((music_array, bpm_array, duration_array, genre_array)).T

# converting the array into a data frame
df = pd.DataFrame(music_array, columns=['Song Title', 'Song BPM', 'Song Duration', 'Genre'])

# saving the data frame to a csv
df.to_csv('music_lib_3.csv')

# printing out the array for debugging
print(music_array)


