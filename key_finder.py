import pandas as pd
import random

x = 0
y = 1

music_lib = pd.read_csv('music_lib_final_test.csv')
length = len(music_lib)
songs = []
fitted_songs = []

for n in range(0, 10, 1):
    track_1 = music_lib[x:y]

    l = 0
    m = 1

    for k in range(0, length, 1):
        track = music_lib[l:m]

        genre_pre = str(track['Genre'].values)
        genre_new = genre_pre[2:-2]

        genre_pre_1 = str(track_1['Genre'].values)
        genre = genre_pre_1[2:-2]

        bpm_pre = str(track_1['Song BPM'].values)
        bpm_pre_2 = bpm_pre[1:-1]
        bpm = float(bpm_pre_2)

        bpm_pre = str(track['Song BPM'].values)
        bpm_pre_2 = bpm_pre[1:-1]
        bpm_new = float(bpm_pre_2)

        key_pre = str(track['Key'].values)
        key_new = key_pre[2:-2]

        key_pre_1 = str(track_1['Key'].values)
        key = key_pre_1[2:-2]

        song_pre_1 = str(track_1['Song Title'].values)
        global song
        song = song_pre_1[2:-2]
        song_name_end = song.find('(')
        song_name = song[:song_name_end]

        song_pre = str(track['Song Title'].values)
        new_song = song_pre[2:-2]
        song_name_new_end = new_song.find('(')
        song_name_new = new_song[:song_name_new_end]

        if (bpm - 10) <= bpm_new <= (bpm + 10) and genre == genre_new and song_name_new != song_name:
            songs.append(new_song)
        two_songs = [song, new_song]
        fitted_songs.append(two_songs)

        l += 1
        m += 1
    x += 1
    y += 1
songs_df = pd.DataFrame(fitted_songs)
print(songs_df[0:1000])



