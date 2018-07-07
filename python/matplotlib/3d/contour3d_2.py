#!/usr/bin/env python
# coding=utf-8

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

fig = plt.figure()
ax = fig.gca(projection='3d')

x, y, z = axes3d.get_test_data(0.05)
cset = ax.contour(x, y, z, extend3d=True, cmap=cm.coolwarm)
ax.clabel(cset, fontsize=0, inline=1)
plt.show()
