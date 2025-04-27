import cv2
import os

os.system("libcamera-still -o snapshot.jpg --width 640 --height 480 --nopreview --timeout 1")
image = cv2.imread("snapshot.jpg")