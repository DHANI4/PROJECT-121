import cv2
import numpy as np

cap = cv2.VideoCapture(0)
image=cv2.imread("bang.jpg")
while True:
    ret, frame = cap.read()
    frame=cv2.resize(frame,(640,480))
    