import cv2
import numpy as np

def bar1(value):
    global image, v1, v2
    v1 = value
    dst = cv2.Canny(image, v1, v2)
    cv2.imshow("dst", dst)

def bar2(value):
    global image1, image2, image3, v1, v2
    v2 = value
    dst = cv2.Canny(image, v1, v2)
    cv2.imshow("dst", dst)


image = cv2.imread("../images/aircraft.jpg")
if image is None:
    raise Exception("영상파일 읽기 오류")

v1, v2 = 100, 150

dst = cv2.Canny(image, v1, v2)

cv2.imshow("src", image)
cv2.imshow("dst", dst)
cv2.createTrackbar("image1", "dst", v1, 255, bar1)
cv2.createTrackbar("image2", "dst", v2, 255, bar2)
cv2.waitKey(0)
cv2.destroyAllWindows()
