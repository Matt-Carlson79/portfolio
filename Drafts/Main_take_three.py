import pandas as pd
import numpy as np
import time
import pyautogui
import math

def mainLoop():
    deck = 1
    counter = 3
    x = 0
    y = 1
    song_playing = False
    pyautogui.FAILSAFE = False
    music_lib = pd.read_csv('music_lib_2.csv')

    while True:
        try:
            if song_playing is False:
                track = music_lib[x:y]

                song_name_pre = str(track['Song Title'].values)
                song_name_string = song_name_pre[2:-2]

                song_bpm_pre = str(track['Song BPM'].values)
                song_bpm_string = song_bpm_pre[1:-2]
                song_bpm_float = float(song_bpm_string)

                song_genre_pre = str(track['Genre'].values)
                song_genre_string = song_genre_pre[2:-2]

                song_duration = str(track['Song Duration'].values)
                song_duration_string = song_duration[1:-1]
                song_duration_float = float(song_duration_string)

                length = len(song_name_string)

                for i in range(0, 3, 1):
                    print(counter)
                    counter -= 1
                    time.sleep(1)

                pyautogui.keyDown('s')
                pyautogui.keyUp('s')

                for x in range(0, length, 1):
                    key = song_name_string[x]
                    pyautogui.press(key)

                pyautogui.press('tab')
                time.sleep(.5)

                if deck == 1:
                    pyautogui.keyDown('l')
                    pyautogui.keyUp('l')
                else:
                    pyautogui.keyDown('r')
                    pyautogui.keyUp('r')

                time.sleep(.5)

                if deck == 1:
                    pyautogui.keyDown('z')
                    pyautogui.keyUp('z')
                    for x in range(0, 35, 1):
                        pyautogui.press('+')
                        pyautogui.press('a')
                else:
                    pyautogui.keyDown('n')
                    pyautogui.keyUp('n')
                    for x in range(0, 35, 1):
                        pyautogui.press('=')
                        pyautogui.press('d')
                song_playing = True

                x += 1
                y += 1

                print('fail')

                if deck == 1:
                    deck = 2
                elif deck == 2:
                    deck = 1

                track_2 = music_lib[x:y]

                song_name_pre_2 = str(track_2['Song Title'].values)
                song_name_string_2 = song_name_pre_2[2:-2]

                song_bpm_pre_2 = str(track_2['Song BPM'].values)
                song_bpm_string_2 = song_bpm_pre_2[1:-2]
                song_bpm_float_2 = float(song_bpm_string_2)

                song_genre_pre_2= str(track_2['Genre'].values)
                song_genre_string = song_genre_pre_2[2:-2]

                song_duration_2 = str(track_2['Song Duration'].values)
                song_duration_string_2 = song_duration_2[1:-1]
                song_duration_float_2 = float(song_duration_string_2)

                length_2 = len(song_name_string_2)

                pyautogui.keyDown('s')
                pyautogui.keyUp('s')

                for x in range(0, length_2, 1):
                    key = song_name_string_2[x]
                    pyautogui.press(key)

                time.sleep(.5)

                ###FIX THIS

                time.sleep(30)

                pyautogui.keyDown('n')
                pyautogui.keyUp('n')

                # for x in range(0, 35, 1):
                #     pyautogui.press('=')
                #     pyautogui.press('d')

            if song_playing is True:
                track = music_lib[x:y]

                song_name_pre = str(track['Song Title'].values)
                song_name_string = song_name_pre[2:-2]

                #song_bpm_pre = str(track['Song BPM'].values)
                #song_bpm_string = song_bpm_pre[1:-2]
                #song_bpm_float = float(song_bpm_string)

                song_genre_pre = str(track['Genre'].values)
                song_genre_string = song_genre_pre[2:-2]

                pyautogui.keyDown('s')
                pyautogui.keyUp('s')

                length = len(song_name_string)

                for x in range(0, length, 1):
                    key = song_name_string[x]
                    pyautogui.press(key)

                    pyautogui.press('tab')
                    time.sleep(.5)

                if deck == 1:
                    pyautogui.keyDown('l')
                    pyautogui.keyUp('l')
                else:
                    pyautogui.keyDown('r')
                    pyautogui.keyUp('r')

                if deck == 1:
                    pyautogui.keyDown('z')
                    pyautogui.keyUp('z')
                    for x in range(0, 34, 1):
                        pyautogui.press('+')
                        pyautogui.press('a')
                        pyautogui.press('*')
                else:
                    pyautogui.keyDown('n')
                    pyautogui.keyUp('n')
                    for x in range(0, 34, 1):
                        pyautogui.press('=')
                        pyautogui.press('d')
                        pyautogui.press('-')

                pyautogui.keyDown('z')
                pyautogui.keyUp('z')

            # song_duration = str(track['Song Duration'].values)
            # song_duration_string = song_duration[1:-1]
            # song_duration_float = float(song_duration_string)

            print('done')
            break
        except:
            print('Error')








mainLoop()

