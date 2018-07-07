#!/usr/bin/env python
# coding=utf-8
import matplotlib.pyplot as plt 
import numpy as np 

np.random.seed(19680801)
data = np.random.random((50,50,50))
fig ,ax = plt.subplots()

print(data.shape)
print(len(data))
print(data[0])
for i in range(len(data)):
    ax.cla()
    ax.imshow(data[i])
    ax.set_title("frame {}".format(i))
    plt.pause(0.1)
