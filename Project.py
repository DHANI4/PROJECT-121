import cv2
import time 
import numpy as np
#to save a output.avi in a file 
fourcc = cv2.VideoWriter_fourcc(*'XVID') 
output_file = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
#starting the web cam
cap = cv2.VideoCapture(0)
#allowing the webcam to start by making the code sleep for 2 seconds.
time.sleep(2) 
bg = 0
#capturing background for 60 frames
#Capturing background for 60 frames 
for i in range(60):
     ret,bg = cap.read() 
#Flipping the background 
bg = np.flip(bg, axis=1)
#major{reading the captured frame until the camera is open}
while (cap.isOpened()):
    ret, img = cap.read()
    if not ret: 
         break
    #Flipping the img 
    img = np.flip(img, axis=1)
    #converting color from bgr to hsv
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    #generating mask to dectect red color
    #these values can also be changed as per the color
    lower_red = np.array([0, 0, 0]) 
    upper_red = np.array([0, 0, 0]) 
    mask_1 = cv2.inRange(hsv, lower_red, upper_red)
    lower_red = np.array([0, 0, 0]) 
    upper_red = np.array([0, 0, 0]) 
    mask_2 = cv2.inRange(hsv, lower_red, upper_red)
    mask_1=mask_1+mask_2
    #open and expand the image where there is mask_1
    mask_1 = cv2.morphologyEx(mask_1, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8)) 
    mask_1 = cv2.morphologyEx(mask_1, cv2.MORPH_DILATE, np.ones((3, 3), np.uint8))
    #selecting only the part that doesn't have mask_1
    mask_2 = cv2.bitwise_not(mask_1)
    #keeping only the part of the image without red color
    res_1 = cv2.bitwise_and(img, img, mask=mask_2)
    #keeping only the part of the image with red color
    res_2 = cv2.bitwise_and(img, img, mask=mask_1)
    #generating with mask_1 and mask_2 together
    final_output = cv2.addWeighted(res_1, 1, res_2, 1, 0) 
    output_file.write(final_output) 
    #Displaying the output to the user 
    cv2.imshow("magic", final_output) 
    cv2.waitKey(1)
cap.release() 
cv2.destroyAllWindows()