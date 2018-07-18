#!/usr/bin/env python
# coding=utf-8

import sympy as sp 
import numpy as np 
from numpy.linalg import solve

x,y = sp.symbols('x,y', real=True)

f =1 +  x**2 + x*y + y**2 
F = sp.Matrix([f])
J = F.jacobian([x,y])
H = J.jacobian([x,y])

print(F)
print(J)
print(H)

# H(f(xn))* delta_x = J(f(xn)) 
# delta_x \in R 2X1 
def Jfxn(xn):
    x=xn[0]
    y=xn[1]
    return np.array([2*x + y, x+2*y])

def Hfxn (xn):
    x=xn[0]
    y=xn[1]
    return np.array([[2,1],[1,2]])
xn = np.array([-10,22]).reshape(2,1)
Jxn = Jfxn(xn)
Hxn =  Hfxn(xn)
print(Jxn)
print(Hxn)

delta_x = solve(Hxn, Jxn)
print(delta_x)
xn_min = xn-delta_x 
print(xn_min)
