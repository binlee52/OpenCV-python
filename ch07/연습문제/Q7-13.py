import cv2, numpy as np

image = cv2.imread("../images/aircraft.jpg")
if image is None:
    raise Exception("영상파일 읽기 오류")

blur1 = cv2.blur(image, (3, 3))     # 평균 블러링
blur2 = cv2.GaussianBlur(image, (5, 5), 0)      # 중심에 있는 픽셀에 높은 가중치
blur3 = cv2.medianBlur(image, 5)    # 무작위 노이즈 제거에 효과적

cv2.imshow("image", image)
cv2.imshow("blur - blur", blur1)
cv2.imshow("blur - Gaussian", blur2)
cv2.imshow("blur - median", blur3)
cv2.waitKey(0)
