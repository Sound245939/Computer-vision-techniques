import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('flower.jpeg',0)

retuval,thresold = cv2. threshold (img,45,255,cv2.THRESH_BINARY)
img2= thresold.copy()

gaussian =cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,
115,1)



cv2.imshow('original',img)
plt.hist(img.ravel(), 256, [0 ,256])
plt.show()
cv2.imshow('thres',img2)
plt.hist(img2.ravel(), 256, [0 ,256])
plt.show()
cv2.imshow('gaus',gaussian)
plt.hist(gaussian.ravel(), 256, [0 ,256])
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
