#輪郭を直線に近似する

import cv2
import matplotlib.pyplot as plt


def various_contours(path):
    color = cv2.imread(path)
    grayed = cv2.cvtColor(color, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(grayed, 218, 255, cv2.THRESH_BINARY)
    inv = cv2.bitwise_not(binary)
    _, contours, _ = cv2.findContours(inv, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for c in contours:
        if cv2.contourArea(c) < 90:
            continue

        epsilon = 0.01 * cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, epsilon, True)
        cv2.drawContours(color, c, -1, (0, 0, 255), 3)
        cv2.drawContours(color, [approx], -1, (0, 255, 0), 3)

    plt.imshow(cv2.cvtColor(color, cv2.COLOR_BGR2RGB))

various_contours()