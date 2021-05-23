import cv2
import numpy as np

capture = cv2.VideoCapture("images/video_file.mp4")
if not capture.isOpened():
    raise Exception("동영상 파일 개방 안됨")

title = "Main Window"

frame_rate = capture.get(cv2.CAP_PROP_FPS)
delay = int(1000 / frame_rate)
frame_cnt = 0       # 현재 프레임 번호

cv2.namedWindow(title, cv2.WINDOW_NORMAL)
cv2.resizeWindow(title, 960, 540)

while True:
    ret, frame = capture.read()
    if not ret or cv2.waitKey(delay) >= 0:
        break

    frame_cnt += 1

    mask = np.zeros(frame.shape, np.uint8)
    mask[100:200, 100:100+200] = 50
    frame = cv2.add(frame, mask)
    frame = cv2.rectangle(frame, (100, 100), (300, 200), (0, 0, 255), thickness=5)

    tmp = cv2.multiply(frame, 1.5)
    frame[500:700, 500:600] = tmp[500:700, 500:600]

    frame = cv2.rectangle(frame, (500, 500), (600, 700), (0, 0, 255), thickness=5)
    cv2.imshow(title, frame)

capture.release()
