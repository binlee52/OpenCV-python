import cv2, numpy as np
from Common.filters import filter

image = cv2.imread("../images/aircraft.jpg", cv2.IMREAD_GRAYSCALE)
if image is None:
    raise Exception("영상파일 읽기 오류")

dst = []

# Roberts Mask
mask1 = [-1, 0, 0, 0, 1, 0, 0, 0, 0]
mask2 = [0, 0, -1, 0, 1, 0, 0, 0, 0]

# Prewitt Mask
mask3 = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
mask4 = [-1, -1, -1, 0, 0, 0, 1, 1, 1]

for mask in [mask1, mask2, mask3, mask4]:
    mask = np.float32(mask).reshape(3, 3)
    dst.append(filter(image, mask))

# Sobel Mask
dst.append(cv2.convertScaleAbs(cv2.Sobel(np.float32(image), cv2.CV_32F, 1, 0, 3)))
dst.append(cv2.convertScaleAbs(cv2.Sobel(np.float32(image), cv2.CV_32F, 0, 1, 3)))


for i, x in enumerate(dst):
    cv2.imshow(f"dst {i + 1}", x)
cv2.waitKey(0)