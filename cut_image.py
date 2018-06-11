import cv2
import numpy as np

def resize_image(img, size):
    # size is enough to img
    img_size = img.shape[:2]
    if img_size[0] > size[1] or img_size[1] > size[0]:
        raise Exception("img is larger than size")

    # centering
    row = (size[1] - img_size[0]) // 2
    col = (size[0] - img_size[1]) // 2
    resized = np.zeros(list(size) + [img.shape[2]], dtype=np.uint8)
    resized[row:(row + img.shape[0]), col:(col + img.shape[1])] = img

    # filling
    mask = np.full(size, 255, dtype=np.uint8)
    mask[row:(row + img.shape[0]), col:(col + img.shape[1])] = 0
    filled = cv2.inpaint(resized, mask, 3, cv2.INPAINT_TELEA)

    return filled