import numpy as np
import cv2


def onChangeRec(value):
    global image, title, rectangle_thickness
    print("Rectangle 굵기: {}".format(value))
    rectangle_thickness = value


def onChangeCir(value):
    global image, title, circle_thickness
    print("Circle 굵기: {}".format(value))
    circle_thickness = value


def onMouse(event, x, y, flags, param):
    global title, rectangle_thickness, circle_thickness
    pt = (x, y)
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.rectangle(image, pt + (30, 30), 100, rectangle_thickness)
        cv2.imshow(title, image)
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(image, pt, 20, 100, circle_thickness)
        cv2.imshow(title, image)


rectangle_thickness, circle_thickness = 1, 1
image = np.ones((600, 800), np.uint8) * 255
title = "Drawing Rectangle & Circle Event"

cv2.namedWindow(title)
cv2.imshow(title, image)

cv2.setMouseCallback(title, onMouse)
cv2.createTrackbar("Rect: ", title, 1, 10, onChangeRec)
cv2.createTrackbar("Cir: ", title, 1, 50, onChangeCir)

cv2.waitKey(0)
cv2.destroyAllWindows()
