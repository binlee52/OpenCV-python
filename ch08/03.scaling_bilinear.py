import numpy as np, cv2
from Common.interpolation import scaling_nearest

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

def scaling_bilinear(img, size):
    ratioY, ratioX = np.divide(size[::-1], img.shape[:2])
    dst = [[ bilinear_value(img, (j/ratioX, i/ratioY))
             for j in range(size[0])]
           for i in range(size[1])]
    return np.array(dst, img.dtype)


image = cv2.imread("images/aircraft.jpg", cv2.IMREAD_GRAYSCALE)
if image is None:
    raise Exception("영상파일 읽기 에러")

size = (800, 600)
dst1 = scaling_bilinear(image, size)    # 양선형 보간
dst2 = scaling_nearest(image, size)     # 최근접 보간
dst3 = cv2.resize(image, size, 0, 0, cv2.INTER_LINEAR)      # 양선형 보간
dst4 = cv2.resize(image, size, 0, 0, cv2.INTER_NEAREST)     # 최근접 보간

cv2.imshow("image", image)
# cv2.imshow("User_bilinear", dst1)
cv2.imshow("User_Nearest", dst2)
cv2.imshow("OpenCV_bilinear", dst3)
cv2.imshow("OpenCV_Nearest", dst4)
cv2.waitKey(0)


            

