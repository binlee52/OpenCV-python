import numpy as np, cv2

def draw_histo(hist, shape=(200, 256)):
    hist_img = np.full(shape, 255, np.uint8)    # 흰색이 배경이 되도록 초기화
    cv2.normalize(hist, hist, 0, shape[0], cv2.NORM_MINMAX)     # 최솟값이 0, 최대값이 그래프의 높이 값을 갖도록 빈도값을 조정
    gap = hist_img.shape[1]/hist.shape[0]

    for i, h in enumerate(hist):
        x = int(round(i*gap))
        w = int(round(gap))
        cv2.rectangle(hist_img, (x, 0, w, int(h)), 0, cv2.FILLED)
    return cv2.flip(hist_img, 0)