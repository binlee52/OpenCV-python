import cv2
import numpy as np

image = cv2.imread("../images/aircraft.jpg")
if image is None:
    raise Exception

dst1 = cv2.convertScaleAbs(cv2.Laplacian(image, cv2.CV_32F, 1))

gaus1 = cv2.GaussianBlur(image, (3, 3), 0)
gaus2 = cv2.GaussianBlur(image, (9, 9), 0)
dst2 = gaus1 - gaus2

cv2.imshow("dst1 - Laplacian", dst1)
cv2.imshow("dst2 - DoG", dst2)
cv2.waitKey(0)