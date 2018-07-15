#!/usr/bin/env python
# coding=utf-8

import numpy as np
from numpy.linalg import inv, solve, lstsq


class PnP(object):
    def __init__(self):
        pass

    def generateData(self, n_int):
        x = np.array([1, 2, 3, 4]).reshape(n_int, 1)
        y = np.array([1, 3, 2, 3]).reshape(n_int, 1)
        z = np.array([2, 4, 5, 6]).reshape(n_int, 1)
        X = np.array([[x], [y], [z]]).reshape(3, -1)
        return X

    def makeT(self, R_3x3, t_3x1):
        T = np.eye(4)
        T[:3, :3] = R_3x3
        T[:3, 3:4] = t_3x1
        return T

    def homo(self, data_3xn):
        return np.append(data_3xn, np.ones((1, data_3xn.shape[1])), axis=0)

    def unHomo(self, data_4xn):
        return data_4xn[:3, :3]

    def X(self, phi):
        Rx = np.array([[1, 0, 0],
                       [0, np.cos(phi), -np.sin(phi)],
                       [0, np.sin(phi), np.cos(phi)]])
        return Rx

    def solvePnP(self):
        """
        use least square approach
        :return:
        """
        pass

    def t_data(self):
        """
        P4P is the needed
        :return:
        """
        t = np.array([1, 0, 0]).reshape(3, 1)
        T10 = self.makeT(self.X(np.pi / 4), t)
        X0 = self.generateData(4)
        X0 = self.homo(X0)
        X1 = inv(T10).dot(X0)
        print(X0, X1)
        X = solve(X1.T, X0.T)
        print(X.T)


class EPnP(object):
    def __init(self):
        pass

    def choiceControlPoints(self):
        pass

    def solvePnP(self):
        pass


if __name__ == "__main__":
    pnp = PnP()
    pnp.t_data()
