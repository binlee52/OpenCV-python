import numpy as np
import cv2

image = cv2.imread("./images/flip_test.png", cv2.IMREAD_GRAYSCALE)
if image is None:
    raise Exception("영상파일 읽기 오류 발생")

min_val, max_val, _, _ = cv2.minMaxLoc(image)

# 255를 구해진 차분으로 나누어서 비율을 계산
ratio = 255 / (max_val - min_val)

# 영상 화소값에 화소 최소값을 뺀 후에 비율로 곱하여 영상내 최소값이 0이 되고
# 최대값이 255가 되도록 한다. 이 때 반올림하여 8비트 정수형(uint8)로 변환한다
dst = np.round((image - min_val) * ratio).astype('uint8')

min_dst, max_dst, _, _ = cv2.minMaxLoc(dst)

print("원본 영상 최솟값= %d, 최댓값= %d" % (min_val, max_val))
print("수정 영상 최솟값= %d, 최댓값= %d" % (min_dst, max_dst))
cv2.imshow("image", image)
cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
