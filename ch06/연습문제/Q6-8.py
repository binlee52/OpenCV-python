import cv2
import numpy as np

image1 = cv2.imread("../images/add1.jpg")
image2 = cv2.imread("../images/add2.jpg")
if image1 is None or image2 is None:
    raise Exception("영상파일 읽기 오류")

image3 = cv2.addWeighted(image1, 0.5, image2, 0.5, 0)

image = cv2.hconcat([image1, image3, image2])
cv2.imshow("dst", image)

cv2.waitKey(0)
cv2.destroyAllWindows()