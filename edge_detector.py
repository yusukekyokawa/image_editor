#輪郭検出する
import cv2
import numpy as np

def main():
    gray = cv2.imread("/home/kiyo/PycharmProjects/image_editor/images/arcKG00121.jpg")

    #ガウシアンフィルタ処理
    gaussian = cv2.GaussianBlur(gray, ksize=(3, 3), sigmaX=1.3)

    #ラプラシアンフィルタ処理
    #laplacian = cv2.Laplacian(gray, cv2.CV_32F, ksize=3)

    #メディアンフィルタ処理
    #medain = cv2.medianBlur(gray, ksize=3)
    #sobel = cv2.Sobel(gray, cv2.CV_32F, 1, 0, ksize=3)

    #結果を出力
    cv2.imwrite("gaussian.jpg", gaussian)
    #cv2.imwrite("laplacian.jpg", laplacian)
    #cv2.imwrite("medain.jpg", medain)
    #cv2.imwrite("sobel.jpg", sobel)

if __name__ =="__main__":
    main()