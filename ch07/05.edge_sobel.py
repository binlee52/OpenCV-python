import numpy as np, cv2
from Common.filters import differential

image = cv2.imread("images/aircraft.jpg", cv2.IMREAD_GRAYSCALE)
if image is None:
    raise Exception("영상파일 읽기 오류")

image = np.array(image, np.float32)
data1 = [-1, 0, 1,
        -2, 0, 2,
        -1, 0, 1]

data2 = [-1, -2, -1,
          0, 0, 0,
          1, 2, 1]

dst, dst1, dst2 = differential(image, data1, data2)

dst3 = cv2.Sobel(np.float32(image), cv2.CV_32F, 1, 0, 3)    # x 방향 미분 - 수직 마스크
dst4 = cv2.Sobel(np.float32(image), cv2.CV_32F, 0, 1, 3)    # y 방향 미분 - 수평 마스크
dst3 = cv2.convertScaleAbs(dst3)
dst4 = cv2.convertScaleAbs(dst4)

cv2.imshow("dst1- vertical_mask", dst1)
cv2.imshow("dst2- horizontal_mask", dst2)
cv2.imshow("dst3- vertical_OpenCV", dst3)
cv2.imshow("dst4- horizontal_OpenCV", dst4)
cv2.waitKey(0)
