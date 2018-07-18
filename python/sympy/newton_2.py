#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import os
import sys
import numpy as np
import sympy as sp

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

a, b, c, d = sp.symbols('a,b,c,d', real=True)
f = 1 + a ** 2 + a * b + a * c + a * d + b ** 2 + b * c + b * d + c ** 2 + c * d + d ** 2
F = sp.Matrix([f])
J = F.jacobian([a, b, c, d])
H = J.jacobian([a, b, c, d])

print(F)
print (J)
print (H)


def Jfxn(xn):
    a = xn[0]
    b = xn[1]
    c = xn[2]
    d = xn[3]
    J = np.array([[2 * a + b + c + d],
                  [a + 2 * b + c + d],
                  [a + b + 2 * c + d],
                  [a + b + c + 2 * d]])
    return J


def Hfxn():
    H = np.array([[2, 1, 1, 1],
                  [1, 2, 1, 1],
                  [1, 1, 2, 1],
                  [1, 1, 1, 2]])
    return H


A = np.random.random((11, 11))
# print(A)
xn = np.ones(11).reshape(11, 1)
# ax=b
a = A + A.T
b = (A + A.T).dot(xn)
x = np.linalg.solve(a, b)
print(x)


########## for test
# f =  x**3 , local minimum
def t_x3(start, steps):
    xn = start
    x_list = []
    for i in range(steps):
        a = 6.0 * xn
        b = 3.0 * (xn ** 2)
        # delta_x = np.linalg.solve([a], [b])
        delta_x = b / a
        x_list.append(delta_x)
        xn = xn - delta_x

    return x_list


print t_x3(start=1, steps=100)
