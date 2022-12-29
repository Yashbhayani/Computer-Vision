import cv2

img = cv2.imread('.\\images\\friend.jpg')
cv2.imshow('original image',img)
# comp_image = 255 - img
comp_image = cv2.bitwise_not(img)
cv2.imshow("Complementary image",comp_image);
cv2.waitKey(0)

# # pip install opencv-python
