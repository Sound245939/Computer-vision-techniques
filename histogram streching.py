def hist_stretch(img_2):

  #histogram stretching
# Create zeros array to store the stretched image
rows, cols = img_2.shape[:2]
min=img_2.min()
max=img_2.max()

# Loop over the image and apply Min-Max formulae

for i in range(0,rows):
for j in range(0,cols):
img3[i,j] = 255*(img3[i,j]-min)/(max-min)
return img3
