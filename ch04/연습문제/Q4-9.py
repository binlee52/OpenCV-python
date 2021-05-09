import numpy as np
import cv2

red = (0, 0, 255)
image = np.ones((600, 400, 3), np.uint8) * 255

cv2.rectangle(image, (100, 100) + (200, 300), red, 3, cv2.LINE_AA)

cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()