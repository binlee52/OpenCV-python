from Common.filters import filter
import cv2, numpy as np

image = cv2.imread("../images/aircraft.jpg")
if image is None:
    raise Exception("영상파일 읽기 오류")
b, g, r = cv2.split(image)
bmask = np.array([1/9] * 9, np.float32).reshape(3, 3)
data = [0, -1, 0, -1, 5, -1, 0, -1, 0]
smask = np.array(data, np.float32)
for x in [b, g, r]:
    x = filter(x, bmask)
    x = filter(x, smask)

dst = cv2.merge((b, g, r))
dst2 = cv2.filter2D(image, -1, bmask)
dst2 = cv2.filter2D(dst2, -1, smask)
cv2.imshow("image", dst)
cv2.imshow("dst2", dst2)
cv2.waitKey(0)
