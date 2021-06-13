# imshow(winname, mat) -> None
# . The function may scale the image, depending on its depth:
# . - If the image is 8-bit unsigned, it is displayed as is.
# . - If the image is 16-bit unsigned or 32-bit integer, the pixels are divided by 256.
# That is, the value range [0,255\*256] is mapped to [0,255].
# . - If the image is 32-bit or 64-bit floating-point, the pixel values are multiplied by 255. That is, the
# .   value range [0,1] is mapped to [0,255].

import numpy as np
import cv2

image1 = np.zeros((50, 512), np.float32)
image2 = np.zeros((50, 512), np.float32)
rows, cols = image1.shape[:2]

# 행렬 전체 초기화
for i in range(rows):
    for j in range(cols):
        image1.itemset((i, j), j//2/255)            # 화소값 점진적 증가
        image2.itemset((i, j), j//20*10/255)        # 계단 현상 증가

cv2.imshow("image1", image1)
cv2.imshow("image2", image2)
cv2.waitKey(0)
cv2.destroyAllWindows()