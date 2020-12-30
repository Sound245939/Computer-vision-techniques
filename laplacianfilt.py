import cv2
import numpy as np
from matplotlib.pyplot import gray

img = cv2.imread('kitten.jpg',0)
def laplace_filter(img,kernel):

    m,n = kernel.shape

    d = int((m-1)/2)
    h,w = img.shape[0], img.shape[1]

    dst = np.zeros((h,w)) #returns new array of above given shape
    filtered_image = cv2.GaussianBlur(img, (3, 3), 3)

#checks the new array by subtracting each value from the row and column of old array
    for y in range (d, h-d):
        for x in range(d, w-d):
            dst[y][x]= np.sum(img[y-d:y+d+1,x-d:x+d+1]*kernel)

    laplacian = cv2.Laplacian(filtered_image, cv2.CV_8U, ksize=5)
    cv2.imshow('laplacian ', laplacian)


    return dst

kernel =np.array([[0,1,0],
                      [1,-4,1],
                      [0,1,0]])

sharpened = cv2.filter2D(img, -1, kernel)
cv2.imshow('laplacian2d ', sharpened)

dst = laplace_filter(img,kernel)
cv2.imshow('laplacian filtered',dst)

cv2.waitKey(0)
cv2.destroyAllWindows()