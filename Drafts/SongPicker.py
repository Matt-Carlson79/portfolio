import pandas as pd
import random
from get_u_input import get_genre
import time
from data_2 import data
global hip_hop_processed



def get_data():
    global hip_hop_processed
    hip_hop_processed = data()


def song_picker():
    # genres = pd.DataFrame(get_genre())
    #
    # hip_hop_pre = genres[0:1]
    # hip_hop_string = str(hip_hop_pre['True/False'].values)
        # hip_hop_string[2:-2]
    #
    # blends_mash_ups_pre = genres[1:2]
    # blends_mash_ups_string = str(blends_mash_ups_pre['True/False'].values)
    # blends_mash_ups_processed = blends_mash_ups_string[2:-2]
    #
    # electro_pre = genres[2:3]
    # electro_string = str(electro_pre['True/False'].values)
    # electro_processed = electro_string[2:-2]
    #
    # pop_pre = genres[3:4]
    # pop_string = str(pop_pre['True/False'].values)
    # pop_processed = pop_string[2:-2]
    #
    # alternative_pre = genres[4:5]
    # alternative_string = str(alternative_pre['True/False'].values)
    # alternative_processed = alternative_string[2:-2]
    #
    # club_pre = genres[5:6]
    # club_string = str(club_pre['True/False'].values)
    # club_processed = club_string[2:-2]
    #
    # country_pre = genres[6:7]
    # country_string = str(country_pre['True/False'].values)
    # country_processed = country_string[2:-2]
    #
    # dance_pre = genres[7:8]
    # dance_string = str(dance_pre['True/False'].values)
    # dance_processed = dance_string[2:-2]
    #
    # electronica_pre = genres[8:9]
    # electronica_string = str(electronica_pre['True/False'].values)
    # electronica_processed = electronica_string[2:-2]
    #
    # house_pre = genres[9:10]
    # house_string = str(house_pre['True/False'].values)
    # house_processed = house_string[2:-2]
    #
    # intros_pre = genres[10:11]
    # intros_string = str(intros_pre['True/False'].values)
    # intros_processed = intros_string[2:-2]
    #
    # latin_pre = genres[11:12]
    # latin_string = str(latin_pre['True/False'].values)
    # latin_processed = latin_string[2:-2]
    #
    # randb_pre = genres[12:13]
    # randb_string = str(randb_pre['True/False'].values)
    # randb_processed = randb_string[2:-2]
    #
    # remix_pre = genres[13:14]
    # remix_string = str(remix_pre['True/False'].values)
    # remix_processed = remix_string[2:-2]
    #
    # rock_pre = genres[14:15]
    # rock_string = str(rock_pre['True/False'].values)
    # rock_processed = rock_string[2:-2]
    #
    # trap_pre = genres[15:16]
    # trap_string = str(trap_pre['True/False'].values)
    # trap_processed = trap_string[2:-2]
    #
    # twerk_pre = genres[16:17]
    # twerk_string = str(twerk_pre['True/False'].values)
    # twerk_processed = twerk_string[2:-2]

    music_lib = pd.read_csv('music_lib_final.csv')

    length = len(music_lib.index)
    x = 0
    y = 1
    hip_hop = []
    temp_vars = []
    if hip_hop_processed == 'True':
        for n in range(0, length, 1):
            track = music_lib[x:y]
            song_genre_pre = str(track['Genre'].values)
            song_genre_string = song_genre_pre[2:-2]


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
        global song
        song = hip_hop[rand]

    counter = 3
    for n in range(0, 3, 1):
        print(counter)
        counter -= 1
        time.sleep(1)

    return song

def song_picker_get_data():
    # genres = pd.DataFrame(get_genre())
    #
    # hip_hop_pre = genres[0:1]
    # hip_hop_string = str(hip_hop_pre['True/False'].values)
        # hip_hop_string[2:-2]
    #
    # blends_mash_ups_pre = genres[1:2]
    # blends_mash_ups_string = str(blends_mash_ups_pre['True/False'].values)
    # blends_mash_ups_processed = blends_mash_ups_string[2:-2]
    #
    # electro_pre = genres[2:3]
    # electro_string = str(electro_pre['True/False'].values)
    # electro_processed = electro_string[2:-2]
    #
    # pop_pre = genres[3:4]
    # pop_string = str(pop_pre['True/False'].values)
    # pop_processed = pop_string[2:-2]
    #
    # alternative_pre = genres[4:5]
    # alternative_string = str(alternative_pre['True/False'].values)
    # alternative_processed = alternative_string[2:-2]
    #
    # club_pre = genres[5:6]
    # club_string = str(club_pre['True/False'].values)
    # club_processed = club_string[2:-2]
    #
    # country_pre = genres[6:7]
    # country_string = str(country_pre['True/False'].values)
    # country_processed = country_string[2:-2]
    #
    # dance_pre = genres[7:8]
    # dance_string = str(dance_pre['True/False'].values)
    # dance_processed = dance_string[2:-2]
    #
    # electronica_pre = genres[8:9]
    # electronica_string = str(electronica_pre['True/False'].values)
    # electronica_processed = electronica_string[2:-2]
    #
    # house_pre = genres[9:10]
    # house_string = str(house_pre['True/False'].values)
    # house_processed = house_string[2:-2]
    #
    # intros_pre = genres[10:11]
    # intros_string = str(intros_pre['True/False'].values)
    # intros_processed = intros_string[2:-2]
    #
    # latin_pre = genres[11:12]
    # latin_string = str(latin_pre['True/False'].values)
    # latin_processed = latin_string[2:-2]
    #
    # randb_pre = genres[12:13]
    # randb_string = str(randb_pre['True/False'].values)
    # randb_processed = randb_string[2:-2]
    #
    # remix_pre = genres[13:14]
    # remix_string = str(remix_pre['True/False'].values)
    # remix_processed = remix_string[2:-2]
    #
    # rock_pre = genres[14:15]
    # rock_string = str(rock_pre['True/False'].values)
    # rock_processed = rock_string[2:-2]
    #
    # trap_pre = genres[15:16]
    # trap_string = str(trap_pre['True/False'].values)
    # trap_processed = trap_string[2:-2]
    #
    # twerk_pre = genres[16:17]
    # twerk_string = str(twerk_pre['True/False'].values)
    # twerk_processed = twerk_string[2:-2]

    get_data()

    music_lib = pd.read_csv('music_lib_final.csv')

    length = len(music_lib.index)
    x = 0
    y = 1
    hip_hop = []
    temp_vars = []
    if hip_hop_processed == 'True':
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
        global song
        song = hip_hop[rand]

    counter = 3
    for n in range(0, 3, 1):
        print(counter)
        counter -= 1
        time.sleep(1)

    return song


