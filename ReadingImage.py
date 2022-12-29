import cv2

img_1 = cv2.imread('.\\images\\friend.jpg')

cv2.imshow('image1', img_1)
cv2.waitKey(0)

# pip install opencv-python