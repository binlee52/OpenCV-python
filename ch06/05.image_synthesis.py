import numpy as np, cv2

image1 = cv2.imread("images/add1.jpg")
image2 = cv2.imread("images/add2.jpg")
if image1 is None or image2 is None:
    raise Exception("영상파일 읽기 오류")

print(image1.shape, image2.shape)
# 영상 합성 방법
alpha, beta = 0.6, 0.7
add_img1 = cv2.add(image1, image2)
add_img2 = cv2.add(image1 * alpha, image2 * beta)
add_img2 = np.clip(add_img2, 0, 255).astype('uint8')
add_img3 = cv2.addWeighted(image1, alpha, image2, beta, 0)

titles = ["image1", "image2", "add_img1", "add_img2", "add_img3"]
for t in titles:
    cv2.imshow(t, eval(t))

cv2.waitKey(0)
cv2.destroyAllWindows()
