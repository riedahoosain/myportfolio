# Webcam Motion Detector
# A program that monitors the computer webcam and sends an email when a new object enters the view.

import cv2 # this is opencv-python

video = cv2.VideoCapture(0)
check, frame = video.read()
print(check)
print(frame)