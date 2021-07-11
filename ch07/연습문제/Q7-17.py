import numpy as np, cv2
import os
path = "../images/plate/"
file = os.listdir(path)
n = 0
length = len(file)

switch_case = {
    2490368: 1,
    2621440: -1
}

while True:
    n %= length
    fname = file[n]
    image = cv2.imread(path + fname, cv2.IMREAD_COLOR)
    if image is None:
        raise Exception("영상파일 읽기 실패")
    mask = np.ones((5, 17), np.uint8)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.blur(gray, (5, 5))
    gray = cv2.Sobel(gray, cv2.CV_8U, 1, 0, 5)
    th_img = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)[1]
    morph = cv2.morphologyEx(th_img, cv2.MORPH_CLOSE, mask, iterations=3)
    image = cv2.hconcat([image,
                         cv2.cvtColor(th_img, cv2.COLOR_GRAY2BGR),
                         cv2.cvtColor(morph, cv2.COLOR_GRAY2BGR)])
    cv2.imshow("image", image)
    key = cv2.waitKeyEx(100)
    if key == 27:
        break
    try:
        n += switch_case[key]
    except KeyError:
        continue

cv2.destroyAllWindows()