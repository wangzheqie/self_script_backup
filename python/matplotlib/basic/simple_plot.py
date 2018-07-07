#!/usr/bin/env python
# coding=utf-8
import  matplotlib.pyplot as plt 
import numpy as np 
import matplotlib 

t = np.arange(0.0, 2.0, 0.01)
s = 1+np.sin(2*np.pi*t)

fig, ax = plt.subplots()
ax.plot(t,s)
ax.set(xlabel="time (s)", ylabel="voltabe (mV)", title="about simple")
ax.grid()
fig.savefig("simple.png")


plt.show()
#matplotlib.axes.Axes.plot 
#matplotlib.pyplot.plot 
#matplotlib.pyplot.subplots 
#matplotlib.figure.Figure.savefig
