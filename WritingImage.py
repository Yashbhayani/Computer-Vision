import cv2

img_1 = cv2.imread('.\\images\\friend.jpg')

cv2.imshow('image1', img_1)
grayimg = cv2.imread('.\\images\\friend.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow('grayimg',grayimg)
cv2.waitKey(0)

# pip install opencv-python