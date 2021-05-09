import numpy as np
import cv2


def onMouse(event, x, y, flags, param):
    global title
    pt = (x, y)
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.rectangle(image, pt + (30, 30), 100, 2)
        cv2.imshow(title, image)
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(image, pt, 20, 100, 2)
        cv2.imshow(title, image)


image = np.ones((600, 800), np.uint8) * 255
title = "Draw Event"
cv2.namedWindow(title)
cv2.imshow(title, image)
cv2.setMouseCallback(title, onMouse)
cv2.waitKey(0)
cv2.destroyAllWindows()