import pandas as pd
import random
from get_u_input import get_genre

def song_picker():
    music_lib = pd.read_csv('music_lib_3.csv')

    #print(music_lib)

    length = len(music_lib.index)
    x = 0
    y = 1
    hip_hop = []
    temp_vars = []
    for n in range(0, length, 1):
        track = music_lib[x:y]
        song_genre_pre = str(track['Genre'].values)
        song_genre_string = song_genre_pre[2:-2]

        song_name_pre = str(track['Song Title'].values)
        song_name_pre = str(track['Song Title'].values)
        song_name_string = song_name_pre[2:-2]

        song_duration = str(track['Song Duration'].values)
        song_duration_string = song_duration[1:-1]
        song_duration_float = float(song_duration_string)

        temp_vars = [song_name_string, song_duration_string, song_genre_string]

        if song_genre_string == 'Hip Hop':
            #print(song_name_string)
            hip_hop.append(temp_vars)

        x += 1
        y += 1
    rand = random.randint(1, len(hip_hop))
    song = hip_hop[rand]

    #print(song)

    return song


#print(song_picker())


