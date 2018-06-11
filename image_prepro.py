#画像の前処理に関する関数まとめ

import cv2
import numpy as np

#グレースケール化
def to_grayscale(path):
    img = cv2.imread(path)
    grayed = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return grayed


#画像の2値化
def binary_threshold(path):
    img = cv2.imread(path)
    grayed = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    under_thresh = 105
    upper_thresh = 145
    maxValue = 255
    th, drop_back = cv2.threshold(grayed, under_thresh, maxValue, cv2.THRESH_BINARY)
    th, clarify_born = cv2.threshold(grayed, upper_thresh, maxValue, cv2.THRESH_BINARY_INV)
    merged = np.minimum(drop_back, clarify_born)
    return merged


#画像のぼかし
def blur(img):
    filtered = cv2.GaussianBlur(img, (11, 11), 0)
    return filtered
