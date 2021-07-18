import numpy as np, cv2
from Common.functions import contain_pts



def draw_rect(img):
    rois = [(p - small, small * 2) for p in pts1]
    for (x, y), (w, h) in np.int32(rois):
        roi = img[y:y+h, x:x+w]
        val = np.full(roi.shape, 80, np.uint8)
        cv2.add(roi, val, roi)
        cv2.rectangle(img, (x, y, w, h), (0, 255, 0), 1)
    cv2.polylines(img, [pts1.astype(int)], True, (0, 255, 0), 1)
    cv2.imshow("select rect", img)

def warp(img):
    perspect_mat = cv2.getPerspectiveTransform(pts1, pts2)
    dst = cv2.warpPerspective(img, perspect_mat, (350, 400), cv2.INTER_CUBIC)
    cv2.imshow("perspective transform", dst)

def onMouse(event, x, y, flags, param):
    global check
    if event==cv2.EVENT_LBUTTONDOWN:
        for i, p in enumerate(pts1):
            p1, p2 = p - small, p + small
            if contain_pts((x, y), p1, p2):
                check = i
    if event == cv2.EVENT_LBUTTONUP:
        check = -1
    if check >= 0:
        pts1[check] = (x, y)
        draw_rect(np.copy(image))
        warp(np.copy(image))

image = cv2.imread("images/aircraft.jpg", cv2.IMREAD_COLOR)
if image is None:
    raise Exception("영상파일 읽기 에러")
small = np.array([12, 12])
check = -1
pts1 = np.float32([(100, 100), (300, 100), (300, 300), (100, 300)])
pts2 = np.float32([(0, 0), (400, 0), (400, 350), (0, 350)])
draw_rect(np.copy(image))
cv2.setMouseCallback("select rect", onMouse, 0)
cv2.waitKey(0)