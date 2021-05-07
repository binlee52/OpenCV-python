import numpy as np
import cv2

image = np.zeros((200, 400), np.uint8)
image[:] = 200

title1, title2 = "Position1", "Position2"
cv2.namedWindow(title1, cv2.WINDOW_AUTOSIZE)
cv2.namedWindow(title2)

# 모니터 좌상단이 기준점
cv2.moveWindow(title1, 150, 150)    # 가로로 150px, 세로로 150px 이동시킴
cv2.moveWindow(title2, 400, 50)

cv2.imshow(title1, image)
cv2.imshow(title2, image)
cv2.waitKey(0)              # 키 입력 대기
cv2.destroyAllWindows()     # 키 입력 후 열린 윈도우 닫기
