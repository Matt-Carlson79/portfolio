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


line_4 = np.array_str(music_df[x:y])
start_4 = line_4.find('TotalTime="') + 11
end_4 = line_4.find('TrackID="') - 2
genre = line_4[start_4:end_4]
