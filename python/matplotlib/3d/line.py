#!/usr/bin/env python
# coding=utf-8
import matplotlib.pyplot as plt
import  numpy as np

fig = plt.figure()
x=range(6)
print(x)
plt.plot(x, [xi for xi in x])
plt.show()