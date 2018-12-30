import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img=cv.imread('sudoku.png')
pts1=np.float32([[25,25],[225,25],[25,225],[225,225]])
pts2=np.float32([[0,0],[200,0],[0,200],[200,200]])
arr=cv.getPerspectiveTransform(pts1,pts2)
res=cv.warpPerspective(img,arr,(200,200))

plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(res),plt.title('Output')
plt.show()