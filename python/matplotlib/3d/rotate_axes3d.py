#!/usr/bin/env python
# coding=utf-8

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x, y, z = axes3d.get_test_data(0.1)
ax.plot_wireframe(x, y, z, rstride=1, cstride=1)

for angle in range(0, 360):
    ax.view_init(30, angle)
    plt.draw()
    plt.pause(0.001)
plt.show()
