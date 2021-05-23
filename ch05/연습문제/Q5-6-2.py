import numpy as np
import cv2

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 2]
m1 = np.array(data).reshape(2, 2, 3)
r, g, b = cv2.split(m1)

print("[m1] = %s" % m1)
print("[r, g, b] = %s, %s, %s" % (r, g, b))
