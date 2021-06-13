import cv2
import numpy as np

def bar1(value):
    global image1, image2, image3, image, v1, v2
    v1 = value
    image3 = cv2.addWeighted(image1, v1/100, image2, v2/100, 0)
    image = cv2.hconcat([image1, image3, image2])
    cv2.imshow("dst", image)

def bar2(value):
    global image1, image2, image3, image, v1, v2
    v2 = value
    image3 = cv2.addWeighted(image1, v1/100, image2, v2/100, 0)
    image = cv2.hconcat([image1, image3, image2])
    cv2.imshow("dst", image)


image1 = cv2.imread("../images/add1.jpg")
image2 = cv2.imread("../images/add2.jpg")
if image1 is None or image2 is None:
    raise Exception("영상파일 읽기 오류")

v1, v2 = 30, 30

image3 = cv2.addWeighted(image1, v1/100, image2, v2/100, 0)
noimage = np.zeros(image1.shape[:3], image1.dtype)
image = cv2.hconcat([image1, image3, image2])

cv2.imshow("dst", image)
cv2.createTrackbar("image1", "dst", v1, 100, bar1)
cv2.createTrackbar("image2", "dst", v2, 100, bar2)
cv2.waitKey(0)
cv2.destroyAllWindows()
