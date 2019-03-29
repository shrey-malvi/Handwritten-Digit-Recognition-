import cv2
import numpy as np
import math
from scipy import ndimage
def getBestShift(img):
    cy,cx = ndimage.measurements.center_of_mass(img)

    rows,cols = img.shape
    shiftx = np.round(cols/2.0-cx).astype(int)
    shifty = np.round(rows/2.0-cy).astype(int)

    return shiftx,shifty


def shift(img,sx,sy):
    rows,cols = img.shape
    M = np.float32([[1,0,sx],[0,1,sy]])
    shifted = cv2.warpAffine(img,M,(cols,rows))
    return shifted
gray=cv2.imread('image.png',0)
gray = cv2.resize(255-gray, (28, 28))
		# better black and white version
ret, gray = cv2.threshold(gray, 180, 255, cv2.THRESH_BINARY)

while np.sum(gray[0]) == 0:
        gray = gray[1:]

while np.sum(gray[:,0]) == 0:
        gray = np.delete(gray,0,1)

while np.sum(gray[-1]) == 0:
        gray = gray[:-1]

while np.sum(gray[:,-1]) == 0:
        gray = np.delete(gray,-1,1)
print(np.shape(gray))

rows,cols = gray.shape

if rows > cols:
        factor = 20.0/rows
        rows = 20
        cols = int(round(cols*factor))
        # first cols than rows
        gray = cv2.resize(gray, (cols,rows))
else:
        factor = 20.0/cols
        cols = 20
        rows = int(round(rows*factor))
        # first cols than rows
        gray = cv2.resize(gray, (cols, rows))

colsPadding = (int(math.ceil((28-cols)/2.0)),int(math.floor((28-cols)/2.0)))
rowsPadding = (int(math.ceil((28-rows)/2.0)),int(math.floor((28-rows)/2.0)))
gray = np.lib.pad(gray,(rowsPadding,colsPadding),'constant')

shiftx,shifty = getBestShift(gray)
shifted = shift(gray,shiftx,shifty)
gray = shifted

# save the processed images
cv2.imwrite("image_1.png", gray)
"""
all images in the training set have an range from 0-1
and not from 0-255 so we divide our flatten images
(a one dimensional vector with our 784 pixels)
to use the same 0-1 based range
"""
flatten = gray.flatten() / 255.0
