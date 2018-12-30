import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('checkers.jpg')
rows,cols,ch = img.shape

pts1 = np.float32([[200,200],[200,800],[800,200]])
pts2 = np.float32([[800,200],[200,800],[200,200]])

M = cv2.getAffineTransform(pts1,pts2)

dst = cv2.warpAffine(img,M,(cols,rows))

plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()