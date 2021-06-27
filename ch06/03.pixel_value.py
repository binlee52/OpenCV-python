import cv2

image = cv2.imread("../ch07/images/bright.png", cv2.IMREAD_GRAYSCALE)
if image is None:
    raise Exception("영상파일 읽기 오류")

(x, y), (w, h) = (180, 37), (15, 10)    # 좌표는 x, y
roi_img = image[y:y+h, x:x+w]   # 행렬 접근은 y, x

print("[roi_img] =")
for row in roi_img:
    for p in row:
        print("{:4d}".format(p), end=" ")

cv2.rectangle(image, (x, y, w, h), 255, 1)
cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
