import numpy as np
import cv2

image = np.zeros((200, 300), np.uint8)
image.fill(255)     # 행렬의 원소값을 255로 채운다.


title1, title2 = "AUTOSIZE", "NORMAL"
cv2.namedWindow(title1, cv2.WINDOW_AUTOSIZE)    # 행렬의 크기변경 없이 윈도우 사이즈만 변경.
cv2.namedWindow(title2, cv2.WINDOW_NORMAL)      # 크기변경을 자유롭게 할 수 있다.

cv2.imshow(title1, image)
cv2.imshow(title2, image)

cv2.resizeWindow(title1, 400, 300)              # 이미지의 크기는 변하지 않음. 윈도우 사이즈만 변함.
cv2.resizeWindow(title2, 400, 300)              # 이미지의 크기가 400*300으로 확장. 보여지는 image 사이즈는 변하지만 실제 image 사이즈는 변하지 않음.

cv2.waitKey(0)
cv2.destroyAllWindows()
