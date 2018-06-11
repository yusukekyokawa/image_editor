import  numpy as np
import cv2

img = cv2.imread('C:/Users/kiyo/PycharmProjects/image_editor/images/arcKG00001.jpg', 1)
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[4]
img = cv2.drawContours(img, [cnt], 0, (0,255,0), 3)
cv2.imshow("result", img)
cv2.waitKey(0)
cv2.destroyAllWindows()