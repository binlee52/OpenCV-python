import numpy as np
import cv2

image = cv2.imread("./images/color.png", cv2.IMREAD_COLOR)
if image is None:
    raise Exception("영상 읽기 에러")

mask = np.zeros(image.shape[:2], np.uint8)
mask[200:400, 100:200] = 255

mean_value = cv2.mean(image, mask)
r, g, b = list(map(np.mean, cv2.split(image[200:400, 100:200])))

print("cv2.mean() 함수를 사용하여 구한 평균 : {}".format(mean_value))
print("영상의 원소 순회 방법을 사용하여 구한 평균 : ({} {} {} 0.0)".format(r, g, b))
