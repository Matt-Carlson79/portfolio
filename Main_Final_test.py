# import all necessary libraries
import time
import pyautogui
import SongPicker_New
import MusicLibStructureCallable
from Song_matcher import song_matcher
import pandas as pd
# create some variables to choose which song gets played
x = 0
y = 1

# is deck 2 playing?
deck_2_playing = False


# countdown function to give user time to open the rekordbox app
def countdown():
    counter = 3
    for n in range(0, 3, 1):
        print(counter)
        counter -= 1
        time.sleep(1)


# this is the main loop that transitions between songs
def main_loop(deck_2_playing):#,x, y)
    global index

    # if a button press fails, don't crash
    pyautogui.FAILSAFE = False
    music_lib = pd.read_csv('music_lib_final_test.csv')

    # load in the next song with logic deciding with or without popup
    if number == 0:
        track = SongPicker_New.get_genre_song()
        global index_1
        global index_2
        index_1 = track[2]
        index_2 = track[3]
        # setting the song duration to a variable in order to wait
        song_duration_float = float(track[1])

        # setting the song name to type in the search bar
        song_name_string = track[0]

    else:
        track_ind = song_matcher(index_1, index_2)
        index_1 = int(track_ind.index.values)
        index_2 = int(index_1 + 1)
        track_2 = music_lib[index_1:index_2]

        song_pre = str(track_2['Song Title'].values)
        song_name_string = song_pre[2:-2]

        # the new song name
        song_duration_pre = str(track_2['Song Duration'].values)
        song_duration_pre_2 = song_duration_pre[1:-1]
        song_duration_float = float(song_duration_pre_2)





    # print statement for debugging
    print(song_duration_float)

    # set the length of the song name string to know how long to run the for loop
    length = len(song_name_string)

    # another countdown function
    counter = 3
    for n in range(0, 3, 1):
        print(counter)
        counter -= 1
        time.sleep(1)

    # hot key to use the search bar
    pyautogui.press('s')

    # types in the name of the desired song into the search bar
    for n in range(0, length, 1):
        key = song_name_string[n]
        pyautogui.press(key)

    # let the program catch up
    time.sleep(.5)

    # select the chosen song
    pyautogui.press('tab')

    # load the chosen song
    pyautogui.keyDown('l')
    pyautogui.keyUp('l')

    # let the program catch up
    time.sleep(1)

    # play deck 1
    pyautogui.keyDown('z')
    pyautogui.keyUp('z')

    # for loop to fade up the volume
    for n in range(0, 35, 1):
        pyautogui.keyDown('a')
        pyautogui.keyUp('a')
        pyautogui.keyDown('+')
        pyautogui.keyUp('+')

    # let the program catch up
    time.sleep(.5)

    # pauses deck 2 if it's playing
    if deck_2_playing is True:
        pyautogui.keyDown('n')
        pyautogui.keyUp('n')

    # move on to the next song in the list
    # try:
    #     x += 1
    #     y += 1
    #     print(x, y)
    # except:
    #     print('error')

    # chose the next song using the SongPicker function
    # track_2 = SongPicker_New.get_song()

    track_ind = song_matcher(index_1, index_2)
    index_1 = int(track_ind.index.values)
    index_2 = int(index_1 + 1)
    track_2 = music_lib[index_1:index_2]

    song_pre = str(track_2['Song Title'].values)
    song_name_string_2 = song_pre[2:-2]

    # the new song name
    song_duration_pre = str(track_2['Song Duration'].values)
    song_duration_pre_2 = song_duration_pre[1:-1]
    song_duration_float_2 = float(song_duration_pre_2)

    # the new song length
    length_2 = len(song_name_string_2)

    # move the cursor to the search bar
    pyautogui.press('s')

    # type in the song name
    for n in range(0, length_2, 1):
        key = song_name_string_2[n]
        pyautogui.press(key)

    # wait for the program to catch up
    time.sleep(1)

    # select the chosen song
    pyautogui.press('tab')

    # load the song into deck 2
    pyautogui.keyDown('r')
    pyautogui.keyUp('r')

    # set the wait time
    countdown = int((song_duration_float - 40))

    # wait until the song has almost finished
    time.sleep(countdown)

    # for n in range(0, countdown, 1):
    #     time.sleep(1)
    #     print(datetime.datetime.fromtimestamp(int(countdown)).strftime('%M:%S'))
    #     countdown -= 1

    # play deck 2
    pyautogui.keyDown('n')
    pyautogui.keyUp('n')


    # fade over to deck 2
    for n in range(0, 35, 1):
        pyautogui.keyDown('d')
        pyautogui.keyUp('d')
        pyautogui.keyDown('=')
        pyautogui.keyUp('=')

    # stop playing deck 2
    pyautogui.keyDown('z')
    pyautogui.keyUp('z')

    # set the second time.sleep
    countdown_2 = int((song_duration_float_2 - 40))

    # wait until the second song is over
    time.sleep(countdown_2)

    # move on to the next song
    # try:
    #     x += 1
    #     y += 1
    #     print(x, y)
    # except:
    #     print('error')

# load in the music library
MusicLibStructureCallable.data_restructure('MusicLibrary.xml')

# dummy variable for logic
number = 0

# main loop
while True:
    # run the main function
    main_loop(deck_2_playing=deck_2_playing)#,x=x, y=y,)

    # move on to the next song
    # x += 2
    # y += 2

    # deck 2 is playing
    deck_2_playing = True

    # increase dummy variable for logic
    number += 1


