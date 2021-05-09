import numpy as np
import cv2


def onMouse(event, x, y, flags, param):
    global title, pt

    if event == cv2.EVENT_LBUTTONDOWN:
        # 값이 음수일 때는 첫 번째 마우스 클릭을 의미
        if pt[0] < 0:
            pt = (x, y)
        else:
            # 파란색 사각형
            cv2.rectangle(image, pt, (x, y), (255, 0, 0), 2)
            cv2.imshow(title, image)
            pt = (-1, -1)       # 시작 좌표 초기화

    elif event == cv2.EVENT_RBUTTONDOWN:
        if pt[0] < 0:
            pt = (x, y)
        else:
            dx, dy = pt[0] - x, pt[1] - y
            radius = int(np.sqrt(dx*dx + dy*dy))        # 반지름 계산
            cv2.circle(image, pt, radius, (0, 0, 255), 2)
            cv2.imshow(title, image)
            pt = (-1, -1)       # 시작 좌표 초기화


image = np.full((300, 500, 3), (255, 255, 255), np.uint8)
pt = (-1, -1)
title = "Draw Event"
cv2.imshow(title, image)
cv2.setMouseCallback(title, onMouse)
cv2.waitKey(0)