import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread('data_new.png', 1)
img2 = cv2.imread('data_old.png', 1)
dif = cv2.absdiff(img1, img2)
if dif == 0:
    motion = False
else:
    motion = True

print(motion)
