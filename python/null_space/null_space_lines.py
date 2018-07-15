#!/usr/bin/env python
# coding=utf-8

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

# x = np.linspace(-10, 10, 20).reshape(1,20)
# y = np.linspace(-10, 10, 20).reshape(1,20)
# z1 = -(2 * x + 3 * y) / 5
# z2 = -(-4 * x + 2 * y) / 3

# x,y = np.mgrid[-10:11:0.1, -10:11:0.1]
# z1 = -(2*x +3*y) /5
# z2 = -(-4*x + 2*y) /3
#
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')
#
# ax.contour(x, y, z1, 10 , offset= -1, lw=3, colors="k", linestyles="solid", alpha=1.0)
# ax.contour(x, y, z2, 10 , offset= -1, lw=3, colors="r", linestyles="solid", alpha=1.0)
# # ax.contour(x,y, z2)
# plt.show()

point1 = np.array([2, 2, -2])
normal1 = np.array([2, 3, 5])

point2 = np.array([3, 3, 2])
normal2 = np.array([-4, 2, 3])
d1 = 0
d2 = 0
# d = -point.dot(normal)

# xx,yy = np.meshgrid(range(10), range(10))
xx, yy = np.mgrid[-10:10:1, -10:10:1]
z1 = -(normal1[0] * xx + normal1[1] * yy) / normal1[2]
z2 = -(-normal2[0] * xx + normal2[2] * yy) / normal2[2]

# -1, 1
x = [1, -1]
y = [26, -26]
z = [-16, 16]

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.plot_surface(xx, yy, z1, color="b")
ax.plot_surface(xx, yy, z2, color="r")
ax.plot(x, y, z, color="k")
ax.plot([-20, 20],[-30, 30], [-50, 50], color="b")
ax.plot([40, -40],[-20, 20], [-30, 30], color="r")
plt.show()
