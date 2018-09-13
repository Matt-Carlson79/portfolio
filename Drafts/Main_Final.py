import pandas as pd
import time
import pyautogui



x = 0
y = 1
deck_2_playing = False


def countdown():
    counter = 3
    for n in range(0, 3, 1):
        print(counter)
        counter -= 1
        time.sleep(1)


def main_loop(x, y, deck_2_playing):

    pyautogui.FAILSAFE = False
    music_lib = pd.read_csv('music_lib_3.csv')

    track = music_lib[x:y]

    song_name_pre = str(track['Song Title'].values)
    song_name_string = song_name_pre[2:-2]

    song_duration = str(track['Song Duration'].values)
    song_duration_string = song_duration[1:-1]
    song_duration_float = float(song_duration_string)
    print(song_duration_float)
    length = len(song_name_string)

    pyautogui.press('s')

    for n in range(0, length, 1):
        key = song_name_string[n]
        pyautogui.press(key)

    time.sleep(.5)

    pyautogui.press('tab')

    pyautogui.keyDown('l')
    pyautogui.keyUp('l')
    pyautogui.keyDown('z')
    pyautogui.keyUp('z')

    for n in range(0, 35, 1):
        pyautogui.keyDown('a')
        pyautogui.keyUp('a')
        pyautogui.keyDown('+')
        pyautogui.keyUp('+')

    time.sleep(.5)

    if deck_2_playing is True:
        pyautogui.keyDown('n')
        pyautogui.keyUp('n')

    try:
        x += 1
        y += 1
        print(x, y)
    except:
        print('error')

    track_2 = music_lib[x:y]
    song_name_pre_2 = str(track_2['Song Title'].values)
    song_name_string_2 = song_name_pre_2[2:-2]

    song_duration_2 = str(track_2['Song Duration'].values)
    song_duration_string_2 = song_duration_2[1:-1]
    song_duration_float_2 = float(song_duration_string_2)

    length_2 = len(song_name_string_2)

    pyautogui.press('s')

    for n in range(0, length_2, 1):
        key = song_name_string_2[n]
        pyautogui.press(key)

    time.sleep(.5)

    pyautogui.press('tab')
    pyautogui.keyDown('r')
    pyautogui.keyUp('r')

    countdown = int((song_duration_float - 40))

    time.sleep(countdown)

    # for n in range(0, countdown, 1):
    #     time.sleep(1)
    #     print(datetime.datetime.fromtimestamp(int(countdown)).strftime('%M:%S'))
    #     countdown -= 1

    pyautogui.keyDown('n')
    pyautogui.keyUp('n')



    for n in range(0, 35, 1):
        pyautogui.keyDown('d')
        pyautogui.keyUp('d')
        pyautogui.keyDown('=')
        pyautogui.keyUp('=')

    pyautogui.keyDown('z')
    pyautogui.keyUp('z')

    countdown_2 = int((song_duration_float_2 - 40))

    time.sleep(countdown_2)

    try:
        x += 1
        y += 1
        print(x, y)
    except:
        print('error')



countdown()

while True:
    main_loop(x=x, y=y, deck_2_playing=deck_2_playing)
    x += 2
    y += 2
    deck_2_playing = True



