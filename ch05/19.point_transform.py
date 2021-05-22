import numpy as np, cv2

# 라디안 각도가 필요(20도 회전)
theta = 20 * np.pi / 180
rot_mat = np.array([[np.cos(theta), -np.sin(theta)],
                    [np.sin(theta), np.cos(theta)]], np.float32)

pts1 = np.array([(250, 30), (400, 70),
                 (350, 250), (150, 200)], np.float32)

# rot_mat * pts1 을 계산하여 회전변환된 행렬을 구함
pts2 = cv2.gemm(pts1, rot_mat, 1, None, 1, flags=cv2.GEMM_2_T)

for i, (pt1, pt2) in enumerate(zip(pts1, pts2)):
    print("pts1[%d] = %s, pts2[%d]= %s" % (i, pt1, i, pt2))

image = np.full((400, 500, 3), 255, np.uint8)
cv2.polylines(image, [np.int32(pts1)], True, (0, 255, 0), 2)
cv2.polylines(image, [np.int32(pts2)], True, (255, 0, 0), 3)
cv2.imshow('image', image)
cv2.waitKey(0)
