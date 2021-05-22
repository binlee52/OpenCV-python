import numpy as np, cv2

image = cv2.imread("images/color.png", cv2.IMREAD_COLOR)
if image is None:
    raise Exception("영상파일 읽기 오류 발생")

# mask를 image와 같은 크기로 선언, 원소값을 0으로 초기화
mask = np.zeros(image.shape[:2], np.uint8)
mask[60:160, 20:120] = 255      # 관심영역 255 설정

sum_value = cv2.sumElems(image)
mean_value1 = cv2.mean(image)
mean_value2 = cv2.mean(image, mask)     # mask  행렬이 1인 원소에 대해서만 평균을 계산

print("sum_value 자료형:", type(sum_value), type(sum_value[0]))
print("[sum_value] =", sum_value)
print("[mean_value1] =", mean_value1)
print("[mean_value2] =", mean_value2)
print()

mean, stddev = cv2.meanStdDev(image)
mean2, stddev2 = cv2.meanStdDev(image, mask=mask)
print("mean 자료형:", type(mean), type(mean[0][0]))
print("[mean] =", mean.flatten())
print("[stddev] =", stddev.flatten())
print()

print("[mean2] =", mean2.flatten())
print("[stddev2] =", stddev2.flatten())

cv2.imshow("image", image)
cv2.imshow("mask", mask)

cv2.waitKey(0)
cv2.destroyAllWindows()

