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
cv2.resizeWindow(title, 400, 300)

while True:
    ret, frame = capture.read()
    if not ret or cv2.waitKey(delay) >= 0:
        break
    frame_cnt += 1
    mask = np.zeros(frame.shape[:2], np.uint8)
    # 세로열(30~270), 가로행(30~350)
    mask[30:30+240, 30:30+320] = 255
    frame = cv2.bitwise_or(frame, frame, mask=mask)
    cv2.rectangle(frame, (30, 30), (30+320, 30+240), color=(0, 0, 255), thickness=4)
    cv2.imshow(title, frame)

capture.release()
