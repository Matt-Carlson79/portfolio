# import all necessary modules
import pyautogui
import numpy as np
import matplotlib.pyplot as plt
import time
import sounddevice as sd


def MainLoop():
    # the frame rate of the input device
    fr = 48000

    # the duration of each sample recording
    duration = 3

    # which deck is playing
    deck = 1

    # the threshold of what counts as music
    threshold = .08

    # i was experimenting with displaying the musics waveform in real time
    wave_form = []

    # countdown before starting
    counter = 3

    # loop to countdown before starting the program
    for i in range(0, 3, 1):
        print(counter)
        counter -= 1
        time.sleep(1)

    # finding the first song
    pyautogui.keyDown('down')
    pyautogui.keyUp('down')

    # load the song into deck 1
    pyautogui.keyDown('l')
    pyautogui.keyUp('l')

    time.sleep(.5)

    # start playing deck 1
    pyautogui.keyDown('z')
    pyautogui.keyUp('z')

    for i in range(0, 34, 1):
        pyautogui.press('+')

    # find the second song
    pyautogui.press('down')
    pyautogui.press('down')

    # load the second song into deck 2
    pyautogui.keyDown('r')
    pyautogui.keyUp('r')

    while True:
        # the command to start recording
        recording = sd.rec(int(duration * fr), channels=2, samplerate=fr)

        # need to wait for the recording to finish
        time.sleep(3)

        # stop the recording
        sd.stop()

        # take the recording and store as a numpy array
        data = np.array(recording)

        # take the absolute value of the wave form
        data_processed_1 = np.absolute(data)

        # average the wave form
        data_processed_2 = np.average(data_processed_1)

        # if the average of the absolute value of the wave form recorded over 3 seconds is less than .08 than press some buttons
        if data_processed_2 < threshold and deck == 1:
            # this is some stuff i was testing with beat matching {
            # pyautogui.keyDown('q')
            # pyautogui.keyUp('q')
            # pyautogui.keyDown('y')
            # pyautogui.keyUp('y') }

            # the hot key to pause/play deck 2
            pyautogui.keyDown('n')
            pyautogui.keyUp('n')

            # for loop fades the next song in
            for x in range(0, 34, 1):
                pyautogui.press('d')

            # the hot key to pause/play deck 1
            pyautogui.keyDown('z')
            pyautogui.keyUp('z')

            # finding the next song
            pyautogui.keyDown('down')
            pyautogui.keyUp('down')
            pyautogui.keyDown('down')
            pyautogui.keyUp('down')

            # load the song into deck 1
            pyautogui.keyDown('l')
            pyautogui.keyUp('l')

            # some trivial text for debugging
            print('Enjoy your next song!')

            # tell the program we are now playing deck 2
            deck = 2

        # All the same stuff but for deck 2
        elif data_processed_2 < threshold and deck == 2:
            # pyautogui.keyDown('q')
            # pyautogui.keyUp('q')
            # pyautogui.keyDown('y')
            # pyautogui.keyUp('y')
            pyautogui.keyDown('z')
            pyautogui.keyUp('z')
            for x in range(0, 34, 1):
                pyautogui.press('a')
            pyautogui.keyDown('n')
            pyautogui.keyUp('n')
            pyautogui.keyDown('down')
            pyautogui.keyUp('down')
            pyautogui.keyDown('down')
            pyautogui.keyUp('down')

            # load the song into deck 2
            pyautogui.keyDown('r')
            pyautogui.keyUp('r')

            print('Enjoy your next song!')
            deck = 1
        # DONT FORGET ELIF QUIT STATEMENT
        else:
            # some more trivial text for debugging
            print('Music Playing')

        wave_form.append(np.array(data))

    #plt.plot(wave_form)
    #plt.show()


# run the function
MainLoop()
