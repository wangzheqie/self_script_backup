#!/usr/bin/env python
# coding=utf-8

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

n_radii = 8
n_angles = 36
radii = np.linspace(0.125, 1.0, n_radii)
angles = np.linspace(0, 2*np.pi, n_angles, endpoint=False)
print(radii)
print(angles)
