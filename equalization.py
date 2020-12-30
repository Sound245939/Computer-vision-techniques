from unittest import result
from matplotlib import pyplot as plt
import cv2
import numpy as np
from PIL import Image



def color_quantization(img, k):

  img2=img.copy()
  rows, cols = img.shape[:2]
#formula to find the inensity of images

   step = 256 / k
   for x in range(rows):
     for y in range(cols):
        result= (np.floor(img[x,y] /step) * step)
        img2[x,y]=result
return img2

#displays the original and quantised images
img = cv2.imread('flower.jpeg', 0)
cv2.imshow('original',img)
color_16 = color_quantization(img,16)
img_2=color_16.copy()
cv2.imshow('cluster16',img_2)
#plots histogram of quantised image
plt.hist(img_2.ravel(), 256, [0 ,256])
plt.show()
#image equalisation of the quantised image
equ=cv2.equalizeHist(img_2)
res=np.hstack((img_2,equ))
cv2.imshow('res.png',res)
plt.hist(equ.ravel(), 256, [0 ,256])
