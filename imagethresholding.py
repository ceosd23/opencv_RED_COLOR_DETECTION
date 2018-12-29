import cv2
import numpy as np
import time
from matplotlib import pyplot as plt

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
img=cv.imread('abc.jpg')
rows,cols=img.shape[:2]
M=np.float32([[1,0,200],[0,1,200]])

dst=cv.warpAffine(img,M,(cols,rows))
N=cv.getRotationMatrix2D((cols/2,rows/2),90,1)
print(N)
res=cv.warpAffine(img,N,(cols,rows))
res=cv.resize(res,None,0.5,0.5,cv.INTER_AREA)

cv.imshow('img',res)
cv.waitKey(0)
cv.destroyAllWindows()
img = cv2.imread('checkers.jpg')
rows,cols,ch = img.shape

pts1 = np.float32([[200,200],[200,800],[800,200]])
pts2 = np.float32([[800,200],[200,800],[200,200]])

M = cv2.getAffineTransform(pts1,pts2)

dst = cv2.warpAffine(img,M,(cols,rows))

plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()
img=cv.imread('sudoku.png')
pts1=np.float32([[25,25],[225,25],[25,225],[225,225]])
pts2=np.float32([[0,0],[200,0],[0,200],[200,200]])
arr=cv.getPerspectiveTransform(pts1,pts2)
res=cv.warpPerspective(img,arr,(200,200))

plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(res),plt.title('Output')
plt.show()