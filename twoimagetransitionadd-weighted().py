import cv2
import numpy as np
import time

img1 = cv2.imread('abc.jpg')
img2 = cv2.imread('g.jpg')
res = img1
i = 10
inc = 1
cv2.imshow('res',res)
while(1):
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break
    else:
       
        res = cv2.addWeighted(img1,0.1*i,img2,0.1*(10-i),0)
        if i == 10 or i == 0:
            inc = -inc
        i = i + inc
        cv2.imshow('res',res)
        time.sleep(0.2)

cv2.destroyAllWindows()