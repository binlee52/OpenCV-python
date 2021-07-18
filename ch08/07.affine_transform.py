import numpy as np, cv2
from Common.functions import contain
from Common.interpolation import bilinear_value

def affine_transform(img, mat):
    rows, cols = img.shape[:2]
    inv_mat = cv2.invertAffineTransform(mat)

    pts = [np.dot(inv_mat, (j, i, 1)) for i in range(rows) for j in range(cols)]
    dst = [bilinear_value(img, p) if contain(p, size) else 0 for p in pts]
    dst = np.reshape(dst, (rows, cols)).astype("uint8")
    return dst


image = cv2.imread("images/aircraft.jpg", cv2.IMREAD_GRAYSCALE)
if image is None:
    raise Exception("영상파일 읽기 에러")

center = (200, 200)
angle, scale = 30, 1
size = image.shape[::-1]

pt1 = np.array([(30, 70), (20, 240), (300, 110)], np.float32)
pt2 = np.array([(120, 20), (10, 180), (280, 260)], np.float32)
aff_mat = cv2.getAffineTransform(pt1, pt2)
rot_mat = cv2.getRotationMatrix2D(center, angle, scale)

dst1 = affine_transform(image, aff_mat)
dst2 = affine_transform(image, rot_mat)
dst3 = cv2.warpAffine(image ,aff_mat, size, cv2.INTER_LINEAR)
dst4 = cv2.warpAffine(image, rot_mat, size, cv2.INTER_LINEAR)

image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
dst1 = cv2.cvtColor(dst1, cv2.COLOR_GRAY2BGR)
dst3 = cv2.cvtColor(dst3, cv2.COLOR_GRAY2BGR)

for i in range(len(pt1)):
    cv2.circle(image, tuple(pt1[i].astype(int)), 3, (0, 0, 255), 2)
    cv2.circle(dst1, tuple(pt2[i].astype(int)), 3, (0, 0, 255), 2)
    cv2.circle(dst3, tuple(pt2[i].astype(int)), 3, (0, 0, 255), 2)

cv2.imshow("image", image)
cv2.imshow("dst1_affine", dst1)
cv2.imshow("dst2_affine_rotate", dst2)
cv2.imshow("dst3_OpenCV_affine", dst3)
cv2.imshow("dst4_OpenCV_affine_rotate", dst4)
cv2.waitKey(0)