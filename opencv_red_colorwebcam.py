import cv2
import numpy as np
x=23
cap = cv2.VideoCapture(0)

while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of red color in HSV
    lower_red1 = np.array([0,100,100])
    upper_red1= np.array([10,255,255])
    lower_red2=np.array([160,100,100])
    upper_red2=np.array([179,100,100])
    # Threshold the HSV image to get only red colors
    mask2 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask1=cv2.inRange(hsv, lower_red2, upper_red2)
    mask=cv2.addWeighted(mask1,1.0,mask2,1.0,0)
    # Bitwise-AND q and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
x=23
cv2.destroyAllWindows()