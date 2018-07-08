#!/usr/bin/env python
# coding=utf-8
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
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


def homo(data_3xn):
    return np.append(data_3xn, np.ones((1, data_3xn.shape[1])), axis=0)


def unHomo(data_4xn):
    return data_4xn[:3, :]


def makeT(R_3x3, t_3x1):
    T = np.eye(4)
    T[:3, :3] = R_3x3
    T[:3, 3:4] = t_3x1
    return T


def sphere(v_3x1, theta_range, psi_range):
    """
    extrinsic rotation
    :param v_3x1:
    :param theta_range:
    :param psi_range:
    :return:
    """
    v_rot = None
    for psi in np.arange(psi_range[0], psi_range[1], psi_range[2]):
        for theta in np.arange(theta_range[0], theta_range[1], theta_range[2]):

            R = Z(psi).dot(Y(theta))
            if (v_rot is None):
                v_rot = R.dot(v_3x1)
            else:
                v_rot = np.append(v_rot, R.dot(v_3x1), axis=1)

    return v_rot


def sphereRT(To, theta_range, psi_range):
    """
    intrinsic rotation
    :param theta_range:
    :param psi_range:
    :param movement_3x1: the translation after intrinsic rotation
    :return:
    """
    R_list = []
    T_list = []
    Ro = To[:3, :3]
    for psi in np.arange(psi_range[0], psi_range[1], psi_range[2]):
        for theta in np.arange(theta_range[0], theta_range[1], theta_range[2]):
            R = Z(psi).dot(Y(theta))
            R_rot = Ro.dot(R)
            T = makeT(R, np.zeros((3, 1)))
            T_rot = To.dot(T)
            R_list.append(R_rot)
            T_list.append(T_rot)
    return R_list, T_list


if __name__ == "__main__":
    """
    input: 
    T1 = Ttr
    T2 = TtrTct
    To = TtrTctToc, oc orthogonal with t=[0,0,r]
    theta_range 
    psi_range 
    save:
    nx6 pose data
    """
    # init some T
    r = 2
    T1 = makeT(X(np.pi).dot(Z(-np.pi / 4)), np.array([-15, -15, 15]).reshape(3, 1))
    T2 = T1.dot(makeT(np.eye(3), np.array([0, 0, 6]).reshape(3, 1)))
    To = T2.dot(makeT(np.eye(3), np.array([0, 0, 6 + r]).reshape(3, 1)))

    # init sphere point for visualization
    esp = 0.01
    theta_range = [0, np.pi / 2 + esp, np.pi / 10]
    psi_range = [0, np.pi * 2 + esp, np.pi / 10]
    v = np.array([0, 0, r]).reshape(3, 1)
    data = sphere(v, theta_range, psi_range)
    data = unHomo(To.dot(homo(data)))

    # sphere transformation
    Ri, Ti = sphereRT(To, theta_range, psi_range)
    Toi_list = []
    for T in Ti:
        Tmove = makeT(np.eye(3), np.array([0, 0, -r]).reshape(3, 1))
        Toi_temp = T.dot(Tmove)
        Toi_list.append(Toi_temp)
    Toi = Toi_list

    # axes for visualization
    x = np.array([0, 1, 0, 0, 0, 0])
    y = np.array([0, 0, 0, 1, 0, 0])
    z = np.array([0, 0, 0, 0, 0, 1])
    # x = np.array([0,0])
    # y = np.array([0,0])
    # z = np.array([0,1])
    axes = np.array([x, y, z])

    # visualization
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.scatter(0, 0, 0, c='b', marker='^')
    ax.scatter(data[0], data[1], data[2], c='r', marker='o')

    I = np.eye(4)
    for T in [I, T1, T2, To]:
        now_axes = unHomo(T.dot(homo(axes)))
        ax.plot(now_axes[0], now_axes[1], now_axes[2], c='b')
    for T in Toi:
        now_axes = unHomo(T.dot(homo(axes)))
        ax.plot(now_axes[0], now_axes[1], now_axes[2], c='y')
        plt.pause(0.1)
    plt.show()
