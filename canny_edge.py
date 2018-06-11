# -*- coding:utf-8 -*-
import cv2
import numpy as np


def main():
    # 入力画像を読み込み
    img = cv2.imread("C:/Users/kiyo/PycharmProjects/image_editor/images/arcKG00001.jpg")

    # グレースケール変換
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    #画像の2値化
    ret, thresh1 = cv2.threshold(gray, 127, 255, cv2.THRESH_TOZERO)
    # 方法2(OpenCVで実装)
    edge2 = cv2.Canny(thresh1, 100, 200)

    # 結果を出力
    cv2.imwrite("output2.jpg", edge2)


if __name__ == "__main__":
    main()