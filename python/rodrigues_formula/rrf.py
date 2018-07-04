#!/usr/bin/env python
# coding=utf-8

import numpy as np
def getR(v, k, theta):
    kx=k[0]
    ky=k[1]
    kz=k[2]
    K = [[0, -kz, ky], [kz, 0, -kx], [-ky, kx, 0]]
    K = np.array(K)
    R = np.eye(3)  + K * np.sin(theta) + K.dot(K) * (1-np.cos(theta)) 

    return R

v = np.array([0,0,300]).reshape(3,1)
theta = np.pi /4

R1 = getR(v,[0,1,0],theta )
v1 = R1.dot(v)
R2 = getR(v1,[0,0,1], theta)
v2 = R2.dot(v1)
print(v1, v1.T.dot(v1))
print(v2, v2.T.dot(v2))

