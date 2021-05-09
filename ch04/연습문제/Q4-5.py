import numpy as np
import cv2

image = np.zeros((300, 400), np.uint8)
image[:] = 180

title = 'Window'
cv2.namedWindow(title, cv2.WINDOW_NORMAL)
cv2.moveWindow(title, 100, 200)
cv2.imshow(title, image)
cv2.waitKey(0)
cv2.destroyAllWindows()