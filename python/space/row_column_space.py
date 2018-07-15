#!/usr/bin/env python
# coding=utf-8

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

a1 = [2,3,5]
A1=np.array(a1).reshape(1,3)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.plot([0,2],[0,3],[0,5])

x1, y1 = np.mgrid[-5:5:0.5, -5:5:0.5]
z1 = -(a1[0] * x1 + a1[1]*y1) / a1[2]
ax.plot_surface(x1,y1,z1)


plt.show()
###########################################3
# from mpl_toolkits.mplot3d.axes3d import Axes3D
# from matplotlib import cm
# import matplotlib.pyplot as plt
# import numpy as np

# fig = plt.figure()
# ax = fig.add_subplot(1, 1, 1, projection='3d')
# X=np.arange(1,10,1)
# Y=np.arange(1,20,1)
# X, Y = np.meshgrid(X, Y)
# Z = X**3 + Y**2
# surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
# cmap=cm.jet,linewidth=0, antialiased=False)
# ax.set_zlim3d(0,1000)
# fig.colorbar(surf, shrink=0.5, aspect=5)
# plt.show()