import cv2 as cv
import numpy as np
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
