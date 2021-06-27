import numpy as np, cv2

def filter(image, mask):
    return cv2.filter2D(image, -1, mask)

# def filter(image, mask):
#     # image = np.array(image, np.float32)
#     rows, cols = image.shape[:2]
#     dst = np.zeros((rows, cols), np.float32)
#     ycenter, xcenter = rows//2, cols//2
#
#     for i in range(ycenter, rows - ycenter):
#         for j in range(xcenter, cols-xcenter):
#             y1, y2 = i - ycenter, i + ycenter + 1
#             x1, x2 = j - xcenter, j + xcenter + 1
#             roi = image[y1:y2, x1:x2].astype("float32")
#             tmp = cv2.multiply(roi, mask)
#             dst[i, j] = cv2.sumElems(tmp)[0]
#     return dst

def differential(image, data1, data2):
    # 추가
    image = np.array(image, np.float32)

    mask1 = np.array(data1, np.float32).reshape(3, 3)
    mask2 = np.array(data2, np.float32).reshape(3, 3)
    dst1 = filter(image, mask1)
    dst2 = filter(image, mask2)
    dst1, dst2 = np.abs(dst1), np.abs(dst2)
    dst = cv2.magnitude(dst1, dst2)

    dst = np.clip(dst, 0, 255).astype('uint8')
    dst1 = np.clip(dst1, 0, 255).astype('uint8')
    dst2 = np.clip(dst2, 0, 255).astype('uint8')
    return dst, dst1, dst2