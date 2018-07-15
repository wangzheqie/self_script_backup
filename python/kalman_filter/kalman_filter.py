#!/usr/bin/env python
# coding=utf-8

import numpy as np
from epnp import EPnP

class KalmanFilter(object):
    def _init__(self):
        self.y = 0
        self.F=self.matZeros(4,4)
        self.K = 0
        self.P = self.matZeros(4,4)
        self.S = 0
        self.v = 0
        self.w = 0

    def predict(self, points_4x4, ):
        pass

    def update(self):
        pass

    def covMatrix(self):
        pass

    def residual(self):
        pass

    def gain(self):
        pass

    def mathExpected(self):
        pass

    def gaussNoise(self):
        pass

    def matZeros(self, d1_int, d2_int, d3_int=None):
        if d3_int is None:
            return np.zeros((d1_int, d2_int))
        else:
            return np.zeros((d1_int, d2_int, d3_int))
