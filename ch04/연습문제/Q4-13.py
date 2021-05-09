import cv2

image = cv2.imread("images/read_color.jpg")
if image is None:
    raise Exception("File not found.")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("Image", gray)
cv2.imwrite("images/test.jpg", image, (cv2.IMWRITE_JPEG_QUALITY, 100))
cv2.imwrite("images/test.png", image, (cv2.IMWRITE_PNG_COMPRESSION, 9))
cv2.waitKey(0)