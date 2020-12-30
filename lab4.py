import cv2
import numpy as np
from matplotlib import pyplot as p

img= cv2.imread('flower.jpeg',0)
print(img.shape)

cv2.imshow("original",img)


noise_Gaussian = np.zeros((img.shape[0], img.shape[1]), dtype='uint8')
cv2.randn(noise_Gaussian, 64, 32) # generates the random noise in image
noisy_image = cv2.add(img, noise_Gaussian)# adds gaussian noise to the filter

filtered_image = cv2.GaussianBlur(noisy_image, (3,3),7)
cv2.imshow("Gaussian noise added - severe", noisy_image) #displays the image with noise

cv2.imshow("Gaussian noise severe - filtered", filtered_image)

def sharp(filtered_image):
    img3=filtered_image.copy()
    kernel_sharpening = np.array([[-1,-1,-1],
                              [-1, 9,-1],
                              [-1,-1,-1]])
# applying the sharpening kernel to the input image & displaying it.
    sharpened = cv2.filter2D(img3, -1, kernel_sharpening)
    return sharpened

def salt_pepper(img,snr):
    img2= img.copy()
    row,col,w = img2.shape
    #mask is created to diffrentiate between the image singal to the noise
    mask =np.random.choice((0,1,2),size=(1,col,w), p=[snr,(1-snr)/2.,(1-snr)/2.])
    np.repeat(mask,row,axis=0)
    img2[mask==1] = 255 #salt
    img2[mask==2] =0 #pepper
    return img2

img3=salt_pepper(img,0.9)
cv2.imshow('s&p',img3)

sharpen_image = sharp(filtered_image)
cv2.imshow('Image Sharpening', sharpen_image)




cv2.waitKey(0)
cv2.destroyAllWindows()
