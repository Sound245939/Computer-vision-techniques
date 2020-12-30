import cv2
import matplotlib.pyplot as plt


img_bgr = cv2.imread('kitten.jpg', 1)
cv2.imshow('original',img_bgr)


# get height and width of the image

height, width, _ = img_bgr.shape
 for i in range(0, height - 1):
   for j in range(0, width - 1):
# Get the pixel value
      pixel = img_bgr[i, j]
      pixel[0] = 255 - pixel[0]
      pixel[1] = 255 - pixel[1]
      pixel[2] = 255 - pixel[2]
      mg_bgr[i, j] = pixel


# Display the negative transformed image
cv2.imshow('negative',img_bgr)
