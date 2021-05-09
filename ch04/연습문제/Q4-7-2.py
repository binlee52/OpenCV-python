import numpy as np
import cv2

def onMouse(event, x, y, flags, param):
    global title
    pt = (x, y)
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(image, pt, 5, 100, 1)
        cv2.imshow(title, image)
    elif event == cv2.EVENT_RBUTTONDOWN:
        # pt + (30, 30) 과 pt, (30, 30)은 다름..!
        cv2.rectangle(image, pt + (30, 30), 100, 2)
        cv2.imshow(title, image)
        

image = np.ones((300, 300), np.uint8) * 255
title = "Draw Event"
cv2.namedWindow(title)
cv2.imshow(title, image)
cv2.setMouseCallback(title, onMouse)
cv2.waitKey(0)
cv2.destroyAllWindows()