import numpy as np
import cv2
from image_prepro import padding_position,to_grayscale,blur, resize_image,binary_threshold

def main():
    img = cv2.imread("./images/"+"arcKG"+"00001"+".jpg")
    ret = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
    blur_img = blur(ret)
    cv2.imshow("katagmai", blur_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()







"""#画像の輪郭検出
def detect_contour(img, min_size):
    #contoured = cv2.imread(path)
    forcrop = cv2.imread(path)

    # make binary image　　画像の2値か
    img = binary_threshold(path)
    img = cv2.bitwise_not(img)

    # detect contour
    im2, contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    crops = []
    # draw contour
    for c in contours:
        if cv2.contourArea(c) < min_size:
            continue

        # rectangle area
        x, y, w, h = cv2.boundingRect(c)
        x, y, w, h = padding_position(x, y, w, h, 5)

        # crop the image
        cropped = forcrop[y:(y + h), x:(x + w)]
        cropped = resize_image(cropped, (210, 210))
        crops.append(cropped)

        # draw contour
        cv2.drawContours(contoured, c, -1, (0, 0, 255), 3)  # contour
        cv2.rectangle(contoured, (x, y), (x + w, y + h), (0, 255, 0), 3)  #rectangle contour

    return contoured, crops"""

if __name__ =="__main__":
    main()