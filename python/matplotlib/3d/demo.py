#!/usr/bin/env python
# coding=utf-8
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

fig = plt.figure()
ax = Axes3D(fig)
n = 256
x=np.arange(-4,4,0.25)
y=np.arange(-4,4,0.25)
# x = np.arange(-1, 1, 0.5)
# y = np.arange(-1, 1, 0.5)
print (x)
print(y)
X, Y = np.meshgrid(x, y)
print(X, Y)
R = np.sqrt(X ** 2 + Y ** 2)
Z = np.sin(R)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.get_cmap('rainbow'))
ax.contour(X, Y, Z, zdim='z', offset=-2, cmap='rainbow')
ax.set_zlim(-2, 2)
plt.show()
