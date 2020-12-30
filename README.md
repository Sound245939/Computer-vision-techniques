# AI-CVLAB

Objective
The main goal of this lab is to understand the impact of different mathematical functions
performed on images for high and low frequency images and make conclusions based on the
results obtained.
This report consists of different methods of image and histogram manipulation
Histogram stretching
Histogram equalization
Image thresholding and negative of image
Performing DFT and inverse DFT on Lena image
Histogram stretching
Histogram stretching is one of the methods of enhancing contrast. This is done by finding the
minimum and maximum pixel intensity multiply by levels of gray.
The following equation below is used to perform histogram stretching.
Where f(x,y) is the value of each pixel density
fmin is the min value of pixels and fmax is the max value of the pixels.
In the example below, the image is first quantized then histogram stretching is performed on the
image. The image is quantized for 3 levels of intensities 16,32 and 128.
Image quantisation is done in order to group colors that look similar together. If we specify that
we only want to show the picture in 4 colors, the quantization will try to see where each pixel
color should fit in those four colors and then rearrange the image.
In this example, the image has first been quantised and to the quantised image histogram
stretching has been performed.
