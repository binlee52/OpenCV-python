import numpy as np
import cv2

x = np.random.normal(0, 1, (3, 6))

# 행 단위(가로 방향)으로 감축
row = cv2.reduce(x, dim=1, rtype=cv2.REDUCE_AVG)
# 열 단위(세로 방향)으로 감축
col = cv2.reduce(x, dim=0, rtype=cv2.REDUCE_AVG)

print("row : \n {}".format(row))
print("col : \n {}".format(col))
