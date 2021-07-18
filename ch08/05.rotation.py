import numpy as np, math, cv2
from Common.interpolation import bilinear_value
from Common.functions import contain

def rotate(img, degree):
    dst = np.zeros(img.shape[:2], img.dtype)
    radian = (degree/180) * np.pi
    sin, cos = np.sin(radian), np.cos(radian)

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            y = -j * sin + i * cos
            x = j * cos + i * sin
            if contain((y, x), img.shape):
                dst[i, j] = bilinear_value(img, [x, y])

    return dst


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


image = cv2.imread("./images/aircraft.jpg", cv2.IMREAD_GRAYSCALE)
if image is None:
    raise Exception("영상파일 읽기 오류")

center = np.divmod(image.shape[::-1], 2)[0]
dst1 = rotate(image, 20)
dst2 = rotate_pt(image, 20, center)

cv2.imshow("image", image)
cv2.imshow("dst1 : rotated on (0, 0)", dst1)
cv2.imshow("dst2 : rotated on center point", dst2)
cv2.waitKey(0)