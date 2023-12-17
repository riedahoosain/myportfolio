# Webcam Motion Detector
# A program that monitors the computer webcam and sends an email when a new object enters the view.

import cv2 # this is opencv-python
import time

video = cv2.VideoCapture(0)
time.sleep(1)
while True:    
    check, frame = video.read()
    cv2.imshow("My Video", frame)
    key=cv2.waitKey(1)
    if key == ord("q"):
        break
video.release()