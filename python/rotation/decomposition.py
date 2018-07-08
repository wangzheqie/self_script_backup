#!/usr/bin/env python
# coding=utf-8

import numpy as np


def X(phi):
    Rx = np.array([[1, 0, 0],
                   [0, np.cos(phi), -np.sin(phi)],
                   [0, np.sin(phi), np.cos(phi)]])
    return Rx


def Y(theta):
    Ry = np.array([[np.cos(theta), 0, np.sin(theta)],
                   [0, 1, 0],
                   [-np.sin(theta), 0, np.cos(theta)]])
    return Ry


def Z(psi):
    Rz = np.array([[np.cos(psi), -np.sin(psi), 0],
                   [np.sin(psi), np.cos(psi), 0],
                   [0, 0, 1]])
    return Rz


if __name__ == "__main__":
    v_r = np.array([0, 0, 1]).reshape(1, 3)  # row vector
    v_c = np.array([0, 0, 1]).reshape(3, 1)  # column vector
    print(v_r)
    print(v_c)
    print(v_r.shape, v_c.shape)
    r1 = -np.pi / 3
    r2 = np.pi / 6
    r3 = np.pi / 4

    # intrinsic elements rotation decomposition
    # around x-y'-z'' axes, angles r1-r2-r3 in order
    Rin_post = Z(r3).dot(Y(r2)).dot(X(r1))
    v_in_post = v_r.dot(Rin_post.T)
    print(v_in_post)
    Rin_pre = X(r1).dot(Y(r2)).dot(Z(r3))
    v_in_pre = Rin_pre.dot(v_c)
    print(v_in_pre)
    print(v_r.dot(Rin_pre.T))

    # extrinsic
    # z-y-x, r3-r2-r1 order
    Rext_post = Z(r3).dot(Y(r2)).dot(X(r1))
    v_ext_pre = v_r.dot(Rext_post)
    print(v_ext_pre)
    Rext_pre = X(r1).dot(Y(r2)).dot(Z(r3))
    v_ext_pre = Rext_pre.dot(v_c)
    print(v_ext_pre)

    # inverse direction transformation
    R = Y(r3)
    v1=R.dot(v_c)
    v2=v_r.dot(np.linalg.inv(R))
    v3=v_r.dot(R.T)
    v4=np.linalg.inv(R).dot(v_c)
    v5=R.T.dot(v_c)
    print(v1)
    print(v2)
    print(v3)
    print(v4)
    print(v5)

    # inverse direction transformation
    R1=Y(r3)
    R2=Z(r3)
    v6=R2.dot(R1).dot(v_c)
    v7=(R2.T).dot(R1).dot(v_c)
    v8 = R2.dot(R2.dot(R1).dot(v_c))
    v9 = R2.dot((R2.T).dot(R1).dot(v_c))
    print(v6)
    print(v7)
    print(v8)
    print(v9)

    # inverse equal transpose
    print(X(r3).T)
    print(np.linalg.inv(X(r3)))
    print(X(r3).T == np.linalg.inv(X(r3)))






