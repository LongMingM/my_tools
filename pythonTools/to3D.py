import numpy as np
import cv2
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D


#img_path = "C:/Users/z/Desktop/image/1.png"
img_path = input("input image path:")

gray_img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

height, width = gray_img.shape

x = np.arange(0, width, 1)
y = np.arange(0, height, 1)
x, y = np.meshgrid(x, y)

z = gray_img

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')

surf = ax.plot_surface(x, y, z, cmap = 'gray')

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Value")

fig.colorbar(surf, shrink = 0.5, aspect = 5)

plt.show()