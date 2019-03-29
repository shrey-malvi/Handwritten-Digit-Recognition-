import cv2
import numpy as np

img = cv2.imread('3.png',0)
#kernel = np.ones((3,3),np.uint8)
#erosion = cv2.erode(img,kernel,iterations = 3)
constant= cv2.copyMakeBorder(img,5,5,5,5,cv2.BORDER_CONSTANT,(0,0,0))
kernel = np.ones((7,7),np.uint8)
erosion = cv2.erode(constant,kernel,iterations = 1)
width = 32
height = 32
dim = (width, height)
 
# resize image
resized = cv2.resize(erosion, dim, interpolation = cv2.INTER_AREA)
cv2.imshow('img',resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
#image_final = cv2.bitwise_and(img2gray, img2gray, mask=mask)
#ret, new_img = cv2.threshold(image_final, 180, 255, cv2.THRESH_BINARY)
#kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (1,1))
#dilated = cv2.dilate(new_img, kernel, iterations=9)
