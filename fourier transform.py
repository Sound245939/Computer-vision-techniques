import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('Lena.png',0)

#performing fourier transform of image
img_f=cv2.dft(np.float32(img),flags=cv2.DFT_COMPLEX_OUTPUT)

#shifts the zero-frequency component to centre of spectrum
img_f1=np.fft.fftshift(img_f)

#displays the specturm of the image
mangnitude_spectrum = 20*np.log(cv2.magnitude(img_f1[:,:,0],img_f1[:,:,1]))

#magnitude_spectrum =np.asarray(mangnitude_spectrum,dtype=np.uint8)
#inverse fourier tranform shifting
#need to apply a mask in order to inverse the fourier transform
rows,cols =img.shape
c,cl = rows//2 ,cols//2

#creating the mask, which is just shifting the pixels back to the centre
#which is just shifting the pixels back to the centre
mask=np.zeros((rows,cols,2),np.uint8)
mask[c-30:c+30, cl-30:cl+30] = 1

#applying mask
img_f2= img_f1*mask
img_ishift=np.fft.ifftshift(img_f2)
img_inv=cv2.idft(img_ishift)
img_inv=cv2.magnitude(img_inv[:,:,0],img_inv[:,:,1])

#retains the image back to the original after the fourier tranform by
performing the inverse

#img_f3=cv2.magnitude(img_f2[:,:,0],img_f2[:,:,1])
plt.subplot(121),plt.imshow(img, cmap='gray')
plt.title('input image'), plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(img_inv, cmap='gray')
plt.title('restored'), plt.xticks([]), plt.yticks([])
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
