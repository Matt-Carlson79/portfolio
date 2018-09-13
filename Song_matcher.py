import pandas as pd
import random


def song_matcher(one, two):
    music_lib_pre = pd.read_csv('music_lib_final_test.csv')
    music_lib = music_lib_pre[:-4]
    song = 0
    bpm = 0
    key = 0
    genre = 0
    name = 0
    compatible_array = [song, bpm, key, genre, name]
    x = 0
    y = 1

    global matches
    matches = []
    # matches = pd.DataFrame(columns=['Song Title', 'Song Bpm', 'Song Key', 'Song Genre', 'Song Name', 'Score'])

    song_title_str = str(music_lib[x:y]['Song Title'].values)[2:-2]

    song_bpm_str = str(music_lib[x:y]['Song BPM'].values)[1:-2]
    song_bpm_start = song_bpm_str.find('.')
    if song_bpm_start > 0:
        song_bpm_float = float(song_bpm_str[:song_bpm_start])
    else:
        song_bpm_float = float(song_bpm_str)

    song_key_str = str(music_lib[one:two]['Key'].values)[2:-2]
    song_genre_str = str(music_lib[one:two]['Genre'].values)[2:-2]
    song_name_start = song_title_str.find('(')
    song_name = song_title_str[:song_name_start]
    song_1 = [song_title_str, song_bpm_float, song_key_str, song_genre_str, song_name]

    x += 1
    y += 1

    for k in range(0, len(music_lib), 1):
        song_title_str = str(music_lib[x:y]['Song Title'].values)[2:-2]
        song_bpm_str = str(music_lib[x:y]['Song BPM'].values)[1:-2]
        song_bpm_start = song_bpm_str.find('.')

        try:
            if song_bpm_start > 0:
                song_bpm_float = float(song_bpm_str[:song_bpm_start])
            else:
                song_bpm_float = float(song_bpm_str)
        except:
            pass
        # print(song_bpm_float, song_bpm_start)
        song_key_str = str(music_lib[x:y]['Key'].values)[2:-2]
        song_genre_str = str(music_lib[x:y]['Genre'].values)[2:-2]
        song_name_start = song_title_str.find('(')
        song_name = song_title_str[:song_name_start]
        score = 0
        song_2 = [song_title_str, song_bpm_float, song_key_str, song_genre_str, song_name, score]


        if song_1[4] != song_2[4]:
            compatible_array[4] = 6
        else:
            compatible_array[4] = 0

        if (song_1[1] - 6) <= song_2[1]  <= (song_1[1] + 6):
            compatible_array[1] = 2
        else:
            compatible_array[1] = 0

        if song_1[2] == 'Fm':
            if song_2[2] == ('Bbm' or 'Fm' or 'Cm' or 'Ab'):
                compatible_array[2] = 2
            else:
                compatible_array[2] = 0

        if song_1[3] == 'Dance':
            if song_2[3] == 'Mashup':
                compatible_array[3] = 1
            elif song_2[3] == 'Dance':
                compatible_array[3] = 1
            elif song_2[3] == 'House':
                compatible_array[3] = 1
            elif song_2[3] == 'Club':
                compatible_array[3] = 1
            elif song_2[3] == 'Electro':
                compatible_array[3] = 1
            elif song_2[3] == 'Electronica':
                compatible_array[3] = 1
            elif song_2[3] == 'Twerk':
                compatible_array[3] = 1
            elif song_2[3] == 'Moombahton':
                compatible_array[3] = 1
            else:
                compatible_array[3] = 0
        elif song_1[3] == 'Mashup':
            if song_2[3] == 'Mashup':
                compatible_array[3] = 1
            elif song_2[3] == 'Dance':
                compatible_array[3] = 1
            elif song_2[3] == 'House':
                compatible_array[3] = 1
            elif song_2[3] == 'Club':
                compatible_array[3] = 1
            elif song_2[3] == 'Electro':
                compatible_array[3] = 1
            elif song_2[3] == 'Electronica':
                compatible_array[3] = 1
            elif song_2[3] == 'Twerk':
                compatible_array[3] = 1
            elif song_2[3] == 'Moombahton':
                compatible_array[3] = 1
            else:
                compatible_array[3] = 0
        elif song_1[3] == 'House':
            if song_2[3] == 'Mashup':
                compatible_array[3] = 1
            elif song_2[3] == 'Dance':
                compatible_array[3] = 1
            elif song_2[3] == 'House':
                compatible_array[3] = 1
            elif song_2[3] == 'Club':
                compatible_array[3] = 1
            elif song_2[3] == 'Electro':
                compatible_array[3] = 1
            elif song_2[3] == 'Electronica':
                compatible_array[3] = 1
            elif song_2[3] == 'Twerk':
                compatible_array[3] = 1
            elif song_2[3] == 'Moombahton':
                compatible_array[3] = 1
            else:
                compatible_array[3] = 0
        elif song_1[3] == 'Club':
            if song_2[3] == 'Mashup':
                compatible_array[3] = 1
            elif song_2[3] == 'Dance':
                compatible_array[3] = 1
            elif song_2[3] == 'House':
                compatible_array[3] = 1
            elif song_2[3] == 'Club':
                compatible_array[3] = 1
            elif song_2[3] == 'Electro':
                compatible_array[3] = 1
            elif song_2[3] == 'Electronica':
                compatible_array[3] = 1
            elif song_2[3] == 'Twerk':
                compatible_array[3] = 1
            elif song_2[3] == 'Moombahton':
                compatible_array[3] = 1
            else:
                compatible_array[3] = 0
        elif song_1[3] == 'Electro':
            if song_2[3] == 'Mashup':
                compatible_array[3] = 1
            elif song_2[3] == 'Dance':
                compatible_array[3] = 1
            elif song_2[3] == 'House':
                compatible_array[3] = 1
            elif song_2[3] == 'Club':
                compatible_array[3] = 1
            elif song_2[3] == 'Electro':
                compatible_array[3] = 1
            elif song_2[3] == 'Electronica':
                compatible_array[3] = 1
            elif song_2[3] == 'Twerk':
                compatible_array[3] = 1
            elif song_2[3] == 'Moombahton':
                compatible_array[3] = 1
            else:
                compatible_array[3] = 0
        elif song_1[3] == 'Electronica':
            if song_2[3] == 'Mashup':
                compatible_array[3] = 1
            elif song_2[3] == 'Dance':
                compatible_array[3] = 1
            elif song_2[3] == 'House':
                compatible_array[3] = 1
            elif song_2[3] == 'Club':
                compatible_array[3] = 1
            elif song_2[3] == 'Electro':
                compatible_array[3] = 1
            elif song_2[3] == 'Electronica':
                compatible_array[3] = 1
            elif song_2[3] == 'Twerk':
                compatible_array[3] = 1
            elif song_2[3] == 'Moombahton':
                compatible_array[3] = 1
            else:
                compatible_array[3] = 0
        elif song_1[3] == 'Twerk':
            if song_2[3] == 'Mashup':
                compatible_array[3] = 1
            elif song_2[3] == 'Dance':
                compatible_array[3] = 1
            elif song_2[3] == 'House':
                compatible_array[3] = 1
            elif song_2[3] == 'Club':
                compatible_array[3] = 1
            elif song_2[3] == 'Electro':
                compatible_array[3] = 1
            elif song_2[3] == 'Electronica':
                compatible_array[3] = 1
            elif song_2[3] == 'Twerk':
                compatible_array[3] = 1
            elif song_2[3] == 'Moombahton':
                compatible_array[3] = 1
            else:
                compatible_array[3] = 0
        elif song_1[3] == 'Moombahton':
            if song_2[3] == 'Mashup':
                compatible_array[3] = 1
            elif song_2[3] == 'Dance':
                compatible_array[3] = 1
            elif song_2[3] == 'House':
                compatible_array[3] = 1
            elif song_2[3] == 'Club':
                compatible_array[3] = 1
            elif song_2[3] == 'Electro':
                compatible_array[3] = 1
            elif song_2[3] == 'Electronica':
                compatible_array[3] = 1
            elif song_2[3] == 'Twerk':
                compatible_array[3] = 1
            elif song_2[3] == 'Moombahton':
                compatible_array[3] = 1
            else:
                compatible_array[3] = 0
        elif song_2[3] == 'Hip Hop':
            if song_2[3] == 'Hip Hop':
                compatible_array[3] = 1
            elif song_2[3] == 'Trap':
                compatible_array[3] = 1
            else:
                compatible_array[3] = 0
        elif song_1[3] == 'Pop':
            if song_2[3] == 'Pop':
                compatible_array[3] = 1
            else:
                compatible_array[3] = 0
        elif song_1[3] == 'R&B':
            if song_2[3] == 'R&B':
                compatible_array[3] = 1
            else:
                compatible_array[3] = 0
        elif song_1[3] == 'Latin':
            if song_2[3] == 'Latin':
                compatible_array[3] = 1
            else:
                compatible_array[3] = 0
        elif song_1[3] == 'Rock':
            if song_2[3] == 'Rock':
                compatible_array[3] = 1
            elif song_2[3] == 'Alternative':
                compatible_array[3] = 1
            else:
                compatible_array[3] = 0
        elif song_1[3] == 'Trap':
            if song_2[3] == 'Trap':
                compatible_array[3] = 1
            elif song_2[3] == 'Hip Hop':
                compatible_array[3] = 1
            else:
                compatible_array[3] = 0
        elif song_1[3] == 'Reggae':
            if song_2[3] == 'Reggae':
                compatible_array[3] = 1
            else:
                compatible_array[3] = 0

        score = (compatible_array[0] + compatible_array[1] + compatible_array[2] + compatible_array[3] + compatible_array[4])
        song_list = [song_title_str, score]
        matches.append(song_list)
        # song_np = np.array(song_2)#np.vstack([song_title_str, song_bpm_float, song_key_str, song_genre_str, song_name, score]))
        # print(song_np.item(5))
        # np.append(arr=np, values=song_np, axis=6)
        # song_np.item(5) = score

        # song_np[5] = score
        # songs = pd.DataFrame(song_2)
        # print(song_np)
        # matches.append(song_np, ignore_index='True')
        # print(matches)

        x += 1
        y += 1

    length = len(matches)
    path =[]
    n = 0
    best = 0
    for i in range(0, length, 1):
        string = str(matches[i]).replace('\"', "\'")

        start = string.find("\',")

        int = float(string[(start + 3): -1])

        #print(string, start, int)

        if int > best:
            best = int
        elif int == best:
            path.append(i)

    # print(best)
    # print(path)
    v = 0
    chosen = []
    for p in range(0, len(path), 1):
        chosen.append(matches[path[v]])
        v += 1

    rand = random.randrange(0, len(chosen), 1)
    chosen_pre = str(chosen[rand])
    end = chosen_pre.find("\',")
    chosen_title = chosen_pre[2:end]

    q = 0
    w = 1
    for f in range(0, len(music_lib), 1):
        dummy = str(music_lib[q:w]['Song Title'].values)[2:-2]
        if chosen_title == dummy:
            song = music_lib[q:w]
        q += 1
        w += 1

    return song
