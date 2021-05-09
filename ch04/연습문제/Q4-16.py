import cv2
from Common.utils import put_string

capture = cv2.VideoCapture("images/video_file.avi")
if not capture.isOpened():
    raise Exception("동영상 파일 개방 안됨")

frame_rate = capture.get(cv2.CAP_PROP_FPS)
delay = int(1000 / frame_rate)
frame_cnt = 0       # 현재 프레임 번호

while True:
    ret, frame = capture.read()
    if not ret or cv2.waitKey(delay) >= 0:
        break

    # 컬러 영상 채널 분리 (BGR)
    blue, green, red = cv2.split(frame)
    frame_cnt += 1

    cv2.add(green[100:300, 200:300], 50, green[100:300, 200:300])

    # 단일 채널 영상 합성
    frame = cv2.merge([blue, green, red])
    put_string(frame, 'frame_cnt: ', (20, 30), frame_cnt)
    cv2.rectangle(frame, (200, 100), (300, 300), (0, 0, 255), 3)
    cv2.imshow("Read Video File", frame)

capture.release()
