import cv2
import matplotlib as plt
import numpy as np
import time

img_1 = cv2.imread('Screencap.png', 0)
img_template = cv2.imread('blank_template.png', 0)
w, h = img_template.shape[::-1]
res = False
res = cv2.matchTemplate(img_1, img_template, cv2.TM_CCOEFF_NORMED)
threshold = 0.8


if res is True:
    print('Yes')
else:
    print('No')

#cv2.imshow('window', img_1)

#if cv2.waitKey(25) & 0xFF == ord('q'):
#    cv2.destroyAllWindows()


#time.sleep(10)
