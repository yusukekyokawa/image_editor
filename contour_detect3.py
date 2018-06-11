import cv2
import numpy as np
import matplotlib.pyplot as plt

im = cv2.imread("C:/Users/kiyo/PycharmProjects/image_editor/images/arcKG00001.jpg")
im2 = cv2.imread("C:/Users/kiyo/PycharmProjects/image_editor/images/arcKG00001.jpg")

# グレースケール
im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

# ガウスフィルタ
im_gray_smooth = cv2.GaussianBlur(im_gray, (11, 11), 0)

# 2値化
ret, th1 = cv2.threshold(im_gray_smooth, 130, 255, cv2.THRESH_BINARY)

# 輪郭検出
im, contours, hierarchy = cv2.findContours(th1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# 輪郭描画
cv2.drawContours(im, contours, -1, (0, 255, 0), 3)

# 描画
plt.subplot(2, 2, 1), plt.imshow(im2, 'gray')
plt.title('input image')
plt.subplot(2, 2, 2), plt.imshow(im, 'gray')
plt.title('output image')
plt.subplot(2, 2, 3), plt.imshow(im_gray_smooth, 'gray')
plt.title(u'グレースケール+ガウスフィルタ')
plt.subplot(2, 2, 4), plt.imshow(th1, 'gray')
plt.title(u'2値化')

plt.show()