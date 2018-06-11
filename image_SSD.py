#イメージテンプレート（SSDで類似評価）
import  cv2
import numpy as np

def main():
    img = cv2.imread("/home/kiyo/PycharmProjects/image_editor/images/arcKG00121.jpg")
    temp = cv2.imread("/home/kiyo/PycharmProjects/image_editor/th21.jpg")


    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    temp = cv2.cvtColor(temp, cv2.COLOR_RGB2GRAY)

    h,w = temp.shape

    match = cv2.matchTemplate(gray, temp, cv2.TM_SQDIFF)
    min_value, max_value, mina_pt, max_pt = cv2.minMaxLoc(match)
    pt = mina_pt
    cv2.rectangle(img, (pt[0],pt[1]),(pt[0] +w, pt[1] + h),
                  (0, 0, 200), 3)
    cv2.imwrite("output.jpg", img)

if __name__ =="__main__":
    main()