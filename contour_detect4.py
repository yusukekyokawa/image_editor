import  cv2
from image_prepro import binary_threshold, resize_image


#画像の輪郭検出
def detect_contour(path, min_size):
    contoured = cv2.imread(path)
    forcrop = cv2.imread(path)

    # make binary image　　画像の2値か
    katagami = binary_threshold(path)
    katagami = cv2.bitwise_not(katagami)

    # detect contour
    im2, contours, hierarchy = cv2.findContours(katagami, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

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

    return contoured, crops


def padding_position(x, y, w, h, p):
    return x - p, y - p, w + p * 2, h + p * 2
