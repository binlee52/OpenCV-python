import numpy as np
import cv2

switch_case ={
    2424832: -1,
    2555904: 1
}

# 트랙바 콜백 함수
def onChange(value):
    global image, title

    add_value = value - int(image[0][0])
    image = image + add_value
    cv2.setTrackbarPos("Brightness", title, image[0][0])
    cv2.imshow(title, image)


image = np.zeros((300, 500), np.uint8)

title = "Trackbar Event"
cv2.imshow(title, image)

cv2.createTrackbar("Brightness", title, image[0][0], 255, onChange)

while True:
    key = cv2.waitKeyEx(100)
    if key == 27:
        break
    try:
        x = switch_case[key]
        if 0 <= image[0][0] + x <= 255:
            onChange(image[0][0] + x)
    except KeyError:
        continue

cv2.waitKey(0)
cv2.destroyAllWindows()
