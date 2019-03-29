import cv2
img = cv2.imread('newimagetext.png')
img2gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 180, 255, cv2.THRESH_BINARY)
_, contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
index=1
for contour in contours:
    [x, y, w, h] = cv2.boundingRect(contour)
    cv2.rectangle(img,(x,y),(x+w,y+h),(100,255,100),2)
    cropped = mask[y :y +  h , x : x + w]
    s =str(index) + '.png'
    print(s)
    cv2.imwrite(s , cropped)
    index = index + 1
    
cv2.imshow('result', img)
cv2.waitKey()
