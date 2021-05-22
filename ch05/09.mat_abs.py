import numpy as np
import cv2

image1 = cv2.imread("images/flip_test.png", cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread("images/bit_test.png", cv2.IMREAD_GRAYSCALE)
if image1 is None or image2 is None:
    raise Exception("영상파일 읽기 오류")

image2 = cv2.resize(image2, dsize=image1.shape[:2])

dif_img1 = cv2.subtract(image1, image2)                             # 차분 연산
dif_img2 = cv2.subtract(np.int16(image1), np.int16(image2))        # 음수결과 보존
abs_dif1 = np.absolute(dif_img2).astype('uint8')
abs_dif2 = cv2.absdiff(image1, image2)                              # 차분 절댓값 계산

x, y, w, h = 100, 150, 7, 3
print("[dif_img1(roi) uint8] = \n%s\n" % dif_img1[y:y+h, x:x+w])
print("[dif_img2(roi) int16] = \n%s\n" % dif_img2[y:y+h, x:x+w])
print("[abs_dif1(roi)] = \n%s\n" % abs_dif1[y:y+h, x:x+w])
print("[abs_dif2(roi)] = \n%s\n" % abs_dif2[y:y+h, x:x+w])

titles = ['image1', 'image2', 'dif_img1', 'abs_dif1', 'abs_dif2']
for title in titles:
    cv2.imshow(title, eval(title))

cv2.waitKey(0)
cv2.destroyAllWindows()
