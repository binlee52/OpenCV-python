import numpy as np, cv2
from Common.functions import contain
def contain_pts(p, p1, p2):
    return p1[0] <= p[0] < p2[0] and p1[1] <= p[1] < p2[1]

def onMouse(event, x, y, flags, param):
    global check, pts

    if event == cv2.EVENT_LBUTTONDOWN:
        if contain((y, x), image.shape):
            pts.append((x, y))
            check = 1
    if event == cv2.EVENT_LBUTTONUP:
        if check == 1:
            if contain((y, x), image.shape):
                pts.append((x, y))
                # cv2.line(image, pts[0], pts[1], (0, 0, 255), 3)
                m = np.subtract(pts[1], pts[0])
                print(m)
                aff = np.float32([[1, 0, m[0]],
                                   [0, 1, m[1]]])
                dst = cv2.warpAffine(image, aff, (image.shape[0] + m[0], image.shape[1] + m[1]))

                cv2.imshow("image", dst)
                check = -1

    if check < 0:
        pts = []

image = cv2.imread("../images/aircraft.jpg", cv2.IMREAD_COLOR)
if image is None:
    raise Exception("영상파일 읽기 오류")

check = 0
pts = []
cv2.imshow("image", image)
cv2.setMouseCallback("image", onMouse, 0)
cv2.waitKey(0)