import numpy as np
from PIL import ImageGrab
import cv2
import time
import pyautogui
import matplotlib as plt
import pyaudio


#This is a countdown to give me time to switch to over to Rekordbox
for i in list(range(3))[::-1]:
    print(i+1)
    time.sleep(1)


#This is a function that starts the music on Rekordbox by sending a key stroke
def play():
    pyautogui.keyDown('z')
    pyautogui.keyUp('z')


#This is a function that takes in a pre defined area and cuts out the background
def roi(img, verticies):
    mask = np.zeros_like(img)
    cv2.fillPoly(mask, verticies, 255)
    masked = cv2.bitwise_and(img, mask)
    return masked


#This function draws lines based on the edges that it finds
#def draw_lines(img, lines):
#    try:
#        for line in lines:
#            coords = line[0]
#            cv2.line(img, (coords[0], coords[1]), (coords[2], coords[3]), [255, 255, 255], 3)
#    except:
#        pass


#This function converts the image captured by cv2 into grayscale so it can process quicker
#This function also usses Canny to detect edges
def process_img(original_image):
    deck_one = True
    processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    processed_img = cv2.Canny(processed_img, threshold1=100, threshold2=200)
    processed_img = cv2.GaussianBlur(processed_img, (5, 5), 0)
    #verticies_deck_one = np.array([[550, 350], [650, 350], [650, 390], [550, 390]])
    #verticies_deck_one = np.array([[960, 180], [1900, 180], [1900, 200], [960, 200]])
    verticies_deck_one = np.array([[0, 0], [1920, 0], [1920, 1080], [0, 1080]])
    if deck_one is True:
        processed_img = roi(processed_img, [verticies_deck_one])

    #lines = cv2.HoughLinesP(processed_img, 1, np.pi/180, 180, np.array([]), 30, 5)
    #draw_lines(processed_img, lines)
    return processed_img


last_time = time.time()

#This function takes a screen grab and saves it to a variable and displays the screen
def screen():
    while True:
        screen = ImageGrab.grab(bbox=(0, 40, 1920, 1080))
        new_screen = process_img(np.array(screen))
        #cv2.imshow('window2', cv2.cvtColor(np.array(screen), cv2.COLOR_BGR2RGB))
        cv2.imshow('window', new_screen)
        cv2.imwrite('Screencap.png', new_screen)
        #time.sleep(3)
        #time.sleep(.1)
        #old_screen = cv2.imread('data_new.png', 0)
        #cv2.imwrite('data_old.png', old_screen)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break



#This function uses feature matching to detect something on screen
def analyze():
    loop = True
    while loop is True:
        img1 = cv2.imread('Images.png', 0)
        img2 = cv2.imread('data.png', 0)

        orb = cv2.ORB_create()

        kp1, des1 = orb.detectAndCompute(img1, None)
        kp2, des2 = orb.detectAndCompute(img2, None)

        bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

        matches = bf.match(des1, des2)
        matches = sorted(matches, key=lambda x: x.distance)

        img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches[:10], None, flags=2)
        plt.imshow(img3)
        plt.show()

#This is me calling all of the functions
play()
screen()
analyze()
