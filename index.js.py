import cv2

# img_0 = cv2.imread('D:\\Projects\\PYTHON\\images\\hanuman.png')
img_1 = cv2.imread('.\\images\\friend.jpg')
# img_2 = cv2.imread('.\\yash.JPG')

# cv2.imshow('image', img_0)
cv2.imshow('image1', img_1)
grayimg = cv2.imread('.\\images\\friend.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow('grayimg',grayimg)
# cv2.imshow('image2', img_2)
cv2.waitKey(0)

# pip install opencv-python