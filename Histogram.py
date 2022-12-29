import cv2
import matplotlib.pyplot as plt

img = cv2.imread('.\\images\\friend.jpg',0)
cv2.imshow('original image',img)
plt.hist(img.ravel(),256,[0,256])
plt.show()
cv2.waitKey(0)