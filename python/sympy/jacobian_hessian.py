#!/usr/bin/env python
# coding=utf-8

import sympy as sp 
from sympy import * 
import numpy as np 
x,y = sp.symbols('x,y', real=True)
a,b,c,d = sp.symbols('a,b,c,d', real=True)
f1 = x+y
f2=x**2 + y**2 
f3 = 1 +  a**2 +a*b+a*c+a*d +b**2 +b*c +b*d + c**2 +c*d +d**2 
#F = sp.Matrix([f1,f2])
#F = sp.Matrix([f1])
#J = F.jacobian([x,y])
F=sp.Matrix([f3])
J = F.jacobian([a,b,c,d])
H = J.jacobian([a,b,c,d])
sub = J.subs([(a,0),(b,0),(c,0),(d,0)])
print(J)
print(H)
print(sub)


