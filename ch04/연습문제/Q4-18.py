import numpy as np
import cv2

red, blue, white = (0, 0, 255), (255, 0, 0), (255 ,255, 255)
image = np.full((600, 900, 3), white, np.uint8)

center = (450, 300)

# 타원의 중점 표시
cv2.ellipse(image, center, (150, 150), 0, 0, 180, blue, cv2.FILLED)
cv2.ellipse(image, center, (150, 150), 0, 180, 360, red, cv2.FILLED)
cv2.circle(image, (375, 300), 75, (0, 0, 255), cv2.FILLED)
cv2.circle(image, (525, 300), 75, (255, 0, 0), cv2.FILLED)

cv2.imshow("Draw Taegeuk", image)
cv2.waitKey()
