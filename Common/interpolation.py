import numpy as np, cv2, math
from Common.functions import contain

def scaling(img, size):
    dst = np.zeros(size[::-1], img.dtype)
    ratioY, ratioX = np.divide(size[::-1], img.shape[:2])
    y = np.arange(0, img.shape[0], 1)
    x = np.arange(0, img.shape[1], 1)
    y, x = np.meshgrid(y, x)
    i, j = np.int32(y * ratioY), np.int32(x*ratioX)
    dst[i, j] = img[y, x]
    return dst

def scaling_nearest(img, size):
    dst = np.zeros(size[::-1], img.dtype)
    ratioY, ratioX = np.divide(size[::-1], img.shape[:2])
    i = np.arange(0, size[1], 1)
    j = np.arange(0, size[0], 1)
    i, j = np.meshgrid(i, j)
    y, x = np.int32(i/ratioY), np.int32(j/ratioX)
    dst[i, j] = img[y, x]
    return dst

def bilinear_value(img, pt):
    x, y = np.int32(pt)
    if x >= img.shape[1]-1:
        x -= 1
    if y >= img.shape[0] - 1:
        y -= 1
    # 4개 화소 - 관심 영역으로 접근
    P1, P2, P3, P4 = np.float32(img[y:y+2, x:x+2].flatten())
    alpha, beta = pt[1] - y, pt[0] - x  # 거리 비율
    M1 = P1 + alpha * (P3 - P1)         # 1차 보간
    M2 = P2 + alpha * (P4 - P2)
    P = M1 + beta * (M2 - M1)       # 2차 보간
    return np.clip(P, 0, 255)


def rotate_pt(img, degree, pt):
    dst = np.zeros(img.shape[:2], img.dtype)
    radian = (degree/180) * np.pi
    sin, cos = math.sin(radian), math.cos(radian)

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            jj, ii = np.subtract((j, i), pt)
            y = -jj * sin + ii * cos
            x = jj * cos + ii * sin
            x, y = np.add((x, y), pt)
            if contain((y, x), img.shape):
                dst[i, j] = bilinear_value(img, (x, y))
    return dst