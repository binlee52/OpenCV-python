import cv2
import numpy as np

logo = cv2.imread("./images/logo.jpg")
if logo is None:
    raise Exception("영상 읽기 실패")

blue, green, red = cv2.split(logo)
masks = []
for x in [blue, green, red]:
    # 임계값 235 이상인 값을 255로 치환. 미만은 0으로.
    mask = cv2.threshold(x, 235, 255, cv2.THRESH_BINARY)[1]
    masks.append(mask)

# 마스크 연산 수행 - 마스크 배열의 원소가 0이 아닌 좌표만 계산을 수행
blue_img = cv2.bitwise_and(logo, logo, mask=masks[0])
green_img = cv2.bitwise_and(logo, logo, mask=masks[1])
red_img = cv2.bitwise_and(logo, logo, mask=masks[2])

cv2.imshow('logo', logo)
cv2.imshow("blue_img", blue_img)
cv2.imshow("green_img", green_img)
cv2.imshow("red_img", red_img)

cv2.waitKey(0)
cv2.destroyAllWindows()