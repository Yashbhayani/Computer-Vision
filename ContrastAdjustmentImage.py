import cv2
import numpy as np

img=cv2.imread('.\\images\\friend.jpg')
img1=img+100
img2=img-100
img3=img*100
res=np.hstack((img,img1,img2,img3))
cv2.imshow("Complementary image",res);
cv2.waitKey(0)