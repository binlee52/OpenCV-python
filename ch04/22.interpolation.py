import matplotlib.pyplot as plt
import numpy as np

methods = ['none', 'nearest', 'bilinear', 'bicubic', 'spline16', 'spline36']
grid = np.random.rand(5, 5)

fig, axs = plt.subplots(nrows=2, ncols=3, figsize=(8, 6))       # 서프 플롯 생성 2행 3열

for ax, method in zip(axs.flat, methods):
    ax.imshow(grid, interpolation=method, cmap='gray')
    ax.set_title(method)

plt.tight_layout()  # 여백 없음
plt.show()
