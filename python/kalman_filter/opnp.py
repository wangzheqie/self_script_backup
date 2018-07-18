#!/usr/bin/env python
# coding=utf-8

import numpy as np
import yaml


class OPnPError(Exception):
    pass


class OPnP(object):
    def __init__(self, config):
        self._config = config
        self.__maxItrNum = self._config["MaxItrNum"]
        self.__maxMu = self._config["MaxMu"]
        self.__minMu = self._config["MinMu"]
        self.__initMu = self._config["InitMu"]
        self.__greaterMuStep = self._config["GreaterMuStep"]
        self.__lessMuStep = self._config["LessMuStep"]
        self.__dimension = self._config["Dimension"]

        self._A = None
        self._Q = None
        self._V = None
        self._W = None

        self._c = 1
        self._p = None
        self._q = None
        self._v = None

    def initialData(self):
        self._A = np.loadtxt(self._config["initA"])
        rightA = self.checkA(self._A)
        if not rightA:
            raise OPnPError()

        self._V = np.loadtxt(self._config["initV"])
        self._W = np.loadtxt(self._config["initW"])
        self._Q = self._A[1:, 1:]
        self._v = self._V[1:]
        self._p = self._A[1:, 0]
        self._q = self._A[0, 1:]

    def checkA(self, A):
        """
        A is positive definite
        Parameters
        ----------
        A

        Returns
        -------

        """
        if False in (A > 0):
            return False
        else:
            return True

    def checkH(self, H):
        """
        H is positive definite
        Parameters
        ----------
        H

        Returns
        -------

        """
        # if False in (A > 0):
        #     return False
        # else:
        #     return True
        return True

    def checkR(self, R):
        """
        rotation matrix R satisfy $R^TR = I, det(R) = 1$
        Parameters
        ----------
        R

        Returns
        -------

        """
        if np.linalg.det(R) == 1 and (R.T).dot(R) == np.eye(3):
            return True
        else:
            return False

    def hessian_v(self, a, b, c, d):
        v = np.array([a ** 2, a * b, a * c, a * d, b ** 2, b * c, b * d, c ** 2, c * d, d ** 2, 1]).reshape((11, 1))
        return v

    def jacobian_v(self, a, b, c, d):
        v = np.array(
            [a ** 3, a ** 2 * b, a ** 2 * c, a ** 2 * d, a * b ** 2, a * b * c, a * b * d, a * c ** 2, a * c * d,
             a * d ** 2, a, b ** 3, b ** 2 * c, b ** 2 * d, b * c ** 2, b * c * d, b * d ** 2, b, c ** 3, c ** 2 * d,
             c * d ** 2, c, d ** 3, d]).reshape((24, 1))
        return v

    def calcObjectFunction(self, flag="original"):
        """

        Parameters
        ----------
        flag
        originaol:
        similar;

        Returns
        -------

        """
        VT = self._V.T
        V = self._V
        Q = self._Q

        v = self._v
        vT = self._v.T
        p = self._p
        q = self._q
        c = self._c

        if flag == "original":
            obj = VT.dot(Q).dot(V) + vT.dot(p) + q.dot(v) + c
        elif flag == "similar":
            obj = VT.dot(Q).dot(V) + 2 * q.dot(v)
        return obj

    def calcJacobian(self):
        a = self._W[0]
        b = self._W[1]
        c = self._W[2]
        d = self._W[3]
        # first order derivation
        v1st = self.jacobian_v(a, b, c, d)

        Q = self._Q
        Q11 = Q[0, 0]
        Q12 = Q[0, 1]
        Q13 = Q[0, 2]
        Q14 = Q[0, 3]
        Q15 = Q[0, 4]
        Q16 = Q[0, 5]
        Q17 = Q[0, 6]
        Q18 = Q[0, 7]
        Q19 = Q[0, 8]
        Q110 = Q[0, 9]
        Q21 = Q[1, 0]
        Q22 = Q[1, 1]
        Q23 = Q[1, 2]
        Q24 = Q[1, 3]
        Q25 = Q[1, 4]
        Q26 = Q[1, 5]
        Q27 = Q[1, 6]
        Q28 = Q[1, 7]
        Q29 = Q[1, 8]
        Q210 = Q[1, 9]
        Q31 = Q[2, 0]
        Q32 = Q[2, 1]
        Q33 = Q[2, 2]
        Q34 = Q[2, 3]
        Q35 = Q[2, 4]
        Q36 = Q[2, 5]
        Q37 = Q[2, 6]
        Q38 = Q[2, 7]
        Q39 = Q[2, 8]
        Q310 = Q[2, 9]
        Q41 = Q[3, 0]
        Q42 = Q[3, 1]
        Q43 = Q[3, 2]
        Q44 = Q[3, 3]
        Q45 = Q[3, 4]
        Q46 = Q[3, 5]
        Q47 = Q[3, 6]
        Q48 = Q[3, 7]
        Q49 = Q[3, 8]
        Q410 = Q[3, 9]
        Q51 = Q[4, 0]
        Q52 = Q[4, 1]
        Q53 = Q[4, 2]
        Q54 = Q[4, 3]
        Q55 = Q[4, 4]
        Q56 = Q[4, 5]
        Q57 = Q[4, 6]
        Q58 = Q[4, 7]
        Q59 = Q[4, 8]
        Q510 = Q[4, 9]
        Q61 = Q[5, 0]
        Q62 = Q[5, 1]
        Q63 = Q[5, 2]
        Q64 = Q[5, 3]
        Q65 = Q[5, 4]
        Q66 = Q[5, 5]
        Q67 = Q[5, 6]
        Q68 = Q[5, 7]
        Q69 = Q[5, 8]
        Q610 = Q[5, 9]
        Q71 = Q[6, 0]
        Q72 = Q[6, 1]
        Q73 = Q[6, 2]
        Q74 = Q[6, 3]
        Q75 = Q[6, 4]
        Q76 = Q[6, 5]
        Q77 = Q[6, 6]
        Q78 = Q[6, 7]
        Q79 = Q[6, 8]
        Q710 = Q[6, 9]
        Q81 = Q[7, 0]
        Q82 = Q[7, 1]
        Q83 = Q[7, 2]
        Q84 = Q[7, 3]
        Q85 = Q[7, 4]
        Q86 = Q[7, 5]
        Q87 = Q[7, 6]
        Q88 = Q[7, 7]
        Q89 = Q[7, 8]
        Q810 = Q[7, 9]
        Q91 = Q[8, 0]
        Q92 = Q[8, 1]
        Q93 = Q[8, 2]
        Q94 = Q[8, 3]
        Q95 = Q[8, 4]
        Q96 = Q[8, 5]
        Q97 = Q[8, 6]
        Q98 = Q[8, 7]
        Q99 = Q[8, 8]
        Q910 = Q[8, 9]
        Q101 = Q[9, 0]
        Q102 = Q[9, 1]
        Q103 = Q[9, 2]
        Q104 = Q[9, 3]
        Q105 = Q[9, 4]
        Q106 = Q[9, 5]
        Q107 = Q[9, 6]
        Q108 = Q[9, 7]
        Q109 = Q[9, 8]
        Q1010 = Q[9, 9]

        q = self._q
        q1 = q[0]
        q2 = q[1]
        q3 = q[2]
        q4 = q[3]
        q5 = q[4]
        q6 = q[5]
        q7 = q[6]
        q8 = q[7]
        q9 = q[8]
        q10 = q[9]

        j1 = [4 * Q11, 6 * Q12, 6 * Q13, 6 * Q14, 4 * Q15 + 2 * Q22, 4 * Q16 + 4 * Q23, 4 * Q17 + 4 * Q24,
              4 * Q18 + 2 * Q33, 4 * Q19 + 4 * Q34, 4 * Q110 + 2 * Q44, 4 * q1, 2 * Q25, 2 * Q26 + 2 * Q35,
              2 * Q27 + 2 * Q45, 2 * Q28 + 2 * Q36, 2 * Q29 + 2 * Q37 + 2 * Q46, 2 * Q210 + 2 * Q47, 2 * q2,
              2 * Q38, 2 * Q39 + 2 * Q48, 2 * Q310 + 2 * Q49, 2 * q3, 2 * Q410, 2 * q4];
        j2 = [2 * Q12, 4 * Q15 + 2 * Q22, 2 * Q16 + 2 * Q23, 2 * Q17 + 2 * Q24, 6 * Q25, 4 * Q26 + 4 * Q35,
              4 * Q27 + 4 * Q45, 2 * Q28 + 2 * Q36, 2 * Q29 + 2 * Q37 + 2 * Q46, 2 * Q210 + 2 * Q47, 2 * q2,
              4 * Q55, 6 * Q56, 6 * Q57, 4 * Q58 + 2 * Q66, 4 * Q59 + 4 * Q67, 4 * Q510 + 2 * Q77, 4 * q5, 2 * Q68,
              2 * Q69 + 2 * Q78, 2 * Q610 + 2 * Q79, 2 * q6, 2 * Q710, 2 * q7];
        j3 = [2 * Q13, 2 * Q16 + 2 * Q23, 4 * Q18 + 2 * Q33, 2 * Q19 + 2 * Q34, 2 * Q26 + 2 * Q35,
              4 * Q28 + 4 * Q36, 2 * Q29 + 2 * Q37 + 2 * Q46, 6 * Q38, 4 * Q39 + 4 * Q48, 2 * Q310 + 2 * Q49,
              2 * q3, 2 * Q56, 4 * Q58 + 2 * Q66, 2 * Q59 + 2 * Q67, 6 * Q68, 4 * Q69 + 4 * Q78, 2 * Q610 + 2 * Q79,
              2 * q6, 4 * Q88, 6 * Q89, 4 * Q810 + 2 * Q99, 4 * q8, 2 * Q910, 2 * q9];
        j4 = [2 * Q14, 2 * Q17 + 2 * Q24, 2 * Q19 + 2 * Q34, 4 * Q110 + 2 * Q44, 2 * Q27 + 2 * Q45,
              2 * Q29 + 2 * Q37 + 2 * Q46, 4 * Q210 + 4 * Q47, 2 * Q39 + 2 * Q48, 4 * Q310 + 4 * Q49, 6 * Q410,
              2 * q4, 2 * Q57, 2 * Q59 + 2 * Q67, 4 * Q510 + 2 * Q77, 2 * Q69 + 2 * Q78, 4 * Q610 + 4 * Q79,
              6 * Q710, 2 * q7, 2 * Q89, 4 * Q810 + 2 * Q99, 6 * Q910, 2 * q9, 4 * Q1010, 4 * q10];

        j1 = np.array(j1).reshape((1, len(j1)))
        j2 = np.array(j2).reshape((1, len(j2)))
        j3 = np.array(j3).reshape((1, len(j3)))
        j4 = np.array(j4).reshape((1, len(j4)))

        # gradient, or Jacobian matrix
        J = [j1.dot(v1st), j2.dot(v1st), j3.dot(v1st), j4.dot(v1st)]
        J = np.array(J).reshape((4, 1))
        return J

    def calcHessian(self):
        a = self._W[0]
        b = self._W[1]
        c = self._W[2]
        d = self._W[3]
        # second order derivation
        v2nd = self.hessian_v(a, b, c, d)

        Q = self._Q
        Q11 = Q[0, 0]
        Q12 = Q[0, 1]
        Q13 = Q[0, 2]
        Q14 = Q[0, 3]
        Q15 = Q[0, 4]
        Q16 = Q[0, 5]
        Q17 = Q[0, 6]
        Q18 = Q[0, 7]
        Q19 = Q[0, 8]
        Q110 = Q[0, 9]
        Q21 = Q[1, 0]
        Q22 = Q[1, 1]
        Q23 = Q[1, 2]
        Q24 = Q[1, 3]
        Q25 = Q[1, 4]
        Q26 = Q[1, 5]
        Q27 = Q[1, 6]
        Q28 = Q[1, 7]
        Q29 = Q[1, 8]
        Q210 = Q[1, 9]
        Q31 = Q[2, 0]
        Q32 = Q[2, 1]
        Q33 = Q[2, 2]
        Q34 = Q[2, 3]
        Q35 = Q[2, 4]
        Q36 = Q[2, 5]
        Q37 = Q[2, 6]
        Q38 = Q[2, 7]
        Q39 = Q[2, 8]
        Q310 = Q[2, 9]
        Q41 = Q[3, 0]
        Q42 = Q[3, 1]
        Q43 = Q[3, 2]
        Q44 = Q[3, 3]
        Q45 = Q[3, 4]
        Q46 = Q[3, 5]
        Q47 = Q[3, 6]
        Q48 = Q[3, 7]
        Q49 = Q[3, 8]
        Q410 = Q[3, 9]
        Q51 = Q[4, 0]
        Q52 = Q[4, 1]
        Q53 = Q[4, 2]
        Q54 = Q[4, 3]
        Q55 = Q[4, 4]
        Q56 = Q[4, 5]
        Q57 = Q[4, 6]
        Q58 = Q[4, 7]
        Q59 = Q[4, 8]
        Q510 = Q[4, 9]
        Q61 = Q[5, 0]
        Q62 = Q[5, 1]
        Q63 = Q[5, 2]
        Q64 = Q[5, 3]
        Q65 = Q[5, 4]
        Q66 = Q[5, 5]
        Q67 = Q[5, 6]
        Q68 = Q[5, 7]
        Q69 = Q[5, 8]
        Q610 = Q[5, 9]
        Q71 = Q[6, 0]
        Q72 = Q[6, 1]
        Q73 = Q[6, 2]
        Q74 = Q[6, 3]
        Q75 = Q[6, 4]
        Q76 = Q[6, 5]
        Q77 = Q[6, 6]
        Q78 = Q[6, 7]
        Q79 = Q[6, 8]
        Q710 = Q[6, 9]
        Q81 = Q[7, 0]
        Q82 = Q[7, 1]
        Q83 = Q[7, 2]
        Q84 = Q[7, 3]
        Q85 = Q[7, 4]
        Q86 = Q[7, 5]
        Q87 = Q[7, 6]
        Q88 = Q[7, 7]
        Q89 = Q[7, 8]
        Q810 = Q[7, 9]
        Q91 = Q[8, 0]
        Q92 = Q[8, 1]
        Q93 = Q[8, 2]
        Q94 = Q[8, 3]
        Q95 = Q[8, 4]
        Q96 = Q[8, 5]
        Q97 = Q[8, 6]
        Q98 = Q[8, 7]
        Q99 = Q[8, 8]
        Q910 = Q[8, 9]
        Q101 = Q[9, 0]
        Q102 = Q[9, 1]
        Q103 = Q[9, 2]
        Q104 = Q[9, 3]
        Q105 = Q[9, 4]
        Q106 = Q[9, 5]
        Q107 = Q[9, 6]
        Q108 = Q[9, 7]
        Q109 = Q[9, 8]
        Q1010 = Q[9, 9]

        q = self._q
        q1 = q[0]
        q2 = q[1]
        q3 = q[2]
        q4 = q[3]
        q5 = q[4]
        q6 = q[5]
        q7 = q[6]
        q8 = q[7]
        q9 = q[8]
        q10 = q[9]

        h11 = [12 * Q11, 12 * Q12, 12 * Q13, 12 * Q14, 4 * Q15 + 2 * Q22, 4 * Q16 + 4 * Q23, 4 * Q17 + 4 * Q24,
               4 * Q18 + 2 * Q33, 4 * Q19 + 4 * Q34, 4 * Q110 + 2 * Q44, 4 * q1];
        h12 = [6 * Q12, 8 * Q15 + 4 * Q22, 4 * Q16 + 4 * Q23, 4 * Q17 + 4 * Q24, 6 * Q25, 4 * Q26 + 4 * Q35,
               4 * Q27 + 4 * Q45, 2 * Q28 + 2 * Q36, 2 * Q29 + 2 * Q37 + 2 * Q46, 2 * Q210 + 2 * Q47, 2 * q2];
        h13 = [6 * Q13, 4 * Q16 + 4 * Q23, 8 * Q18 + 4 * Q33, 4 * Q19 + 4 * Q34, 2 * Q26 + 2 * Q35, 4 * Q28 + 4 * Q36,
               2 * Q29 + 2 * Q37 + 2 * Q46, 6 * Q38, 4 * Q39 + 4 * Q48, 2 * Q310 + 2 * Q49, 2 * q3];
        h14 = [6 * Q14, 4 * Q17 + 4 * Q24, 4 * Q19 + 4 * Q34, 8 * Q110 + 4 * Q44, 2 * Q27 + 2 * Q45,
               2 * Q29 + 2 * Q37 + 2 * Q46, 4 * Q210 + 4 * Q47, 2 * Q39 + 2 * Q48, 4 * Q310 + 4 * Q49, 6 * Q410,
               2 * q4];

        h22 = [4 * Q15 + 2 * Q22, 12 * Q25, 4 * Q26 + 4 * Q35, 4 * Q27 + 4 * Q45, 12 * Q55, 12 * Q56, 12 * Q57,
               4 * Q58 + 2 * Q66, 4 * Q59 + 4 * Q67, 4 * Q510 + 2 * Q77, 4 * q5];
        h23 = [2 * Q16 + 2 * Q23, 4 * Q26 + 4 * Q35, 4 * Q28 + 4 * Q36, 2 * Q29 + 2 * Q37 + 2 * Q46, 6 * Q56,
               8 * Q58 + 4 * Q66, 4 * Q59 + 4 * Q67, 6 * Q68, 4 * Q69 + 4 * Q78, 2 * Q610 + 2 * Q79, 2 * q6];
        h24 = [2 * Q17 + 2 * Q24, 4 * Q27 + 4 * Q45, 2 * Q29 + 2 * Q37 + 2 * Q46, 4 * Q210 + 4 * Q47, 6 * Q57,
               4 * Q59 + 4 * Q67, 8 * Q510 + 4 * Q77, 2 * Q69 + 2 * Q78, 4 * Q610 + 4 * Q79, 6 * Q710, 2 * q7];

        h33 = [4 * Q18 + 2 * Q33, 4 * Q28 + 4 * Q36, 12 * Q38, 4 * Q39 + 4 * Q48, 4 * Q58 + 2 * Q66, 12 * Q68,
               4 * Q69 + 4 * Q78, 12 * Q88, 12 * Q89, 4 * Q810 + 2 * Q99, 4 * q8];
        h34 = [2 * Q19 + 2 * Q34, 2 * Q29 + 2 * Q37 + 2 * Q46, 4 * Q39 + 4 * Q48, 4 * Q310 + 4 * Q49, 2 * Q59 + 2 * Q67,
               4 * Q69 + 4 * Q78, 4 * Q610 + 4 * Q79, 6 * Q89, 8 * Q810 + 4 * Q99, 6 * Q910, 2 * q9];

        h44 = [4 * Q110 + 2 * Q44, 4 * Q210 + 4 * Q47, 4 * Q310 + 4 * Q49, 12 * Q410, 4 * Q510 + 2 * Q77,
               4 * Q610 + 4 * Q79, 12 * Q710, 4 * Q810 + 2 * Q99, 12 * Q910, 12 * Q1010, 4 * q10];

        h11 = np.array(h11).reshape((1, len(h11)))
        h12 = np.array(h12).reshape((1, len(h12)))
        h13 = np.array(h13).reshape((1, len(h13)))
        h14 = np.array(h14).reshape((1, len(h14)))
        h22 = np.array(h22).reshape((1, len(h22)))
        h23 = np.array(h23).reshape((1, len(h23)))
        h24 = np.array(h24).reshape((1, len(h24)))
        h33 = np.array(h33).reshape((1, len(h33)))
        h34 = np.array(h34).reshape((1, len(h34)))
        h44 = np.array(h44).reshape((1, len(h44)))

        H = np.array([[h11.dot(v2nd), h12.dot(v2nd), h13.dot(v2nd), h14.dot(v2nd)],
                      [h12.dot(v2nd), h22.dot(v2nd), h23.dot(v2nd), h24.dot(v2nd)],
                      [h13.dot(v2nd), h23.dot(v2nd), h33.dot(v2nd), h34.dot(v2nd)],
                      [h14.dot(v2nd), h24.dot(v2nd), h34.dot(v2nd), h44.dot(v2nd)]]).reshape((4, 4))
        return H

    def errorAnalysis(self):
        pass

    def initialGuess(self):
        pass

    def solve(self):
        """

        Returns
        -------
        R, t, error,
        """
        self.initialData()
        print("initialize success!!!")
        J = self.calcJacobian()
        # print(J)
        # print("calculate jacobian matrix success!!!")
        H = self.calcHessian()
        # print(H)
        # print("calculate hessian matrix success!!!")

        itr = 0
        while itr < self.__maxItrNum:
            obj_pre = self.calcObjectFunction(flag="original")
            maxMu = self.__maxMu
            mu = self.__initMu
            while mu < maxMu:
                J = self.calcJacobian()
                H = self.calcHessian()
                rightH = self.checkH(H)

                # TODO: do rightH

                delta_w = np.linalg.inv((H + mu * np.eye(4))).dot(J)
                # TODO: change self._W

                obj_cur = self.calcObjectFunction(flag="original")
                if obj_cur >= obj_pre:
                    mu = self.__greaterMuStep * mu
                    continue
                else:
                    obj_pre = obj_cur
                    mu = self.__lessMuStep * mu
                    break

                # TODO: continue and break
                # mu>maxMu
                # mu<minMu


def loadYaml(file):
    with open(file, 'r') as stream:
        try:
            config = yaml.load(stream)
        except yaml.YAMLError as  e:
            print(e)
    return config


def auto_grobner_basis_gen(rows, cols):
    for i in range(0, rows, 1):
        for j in range(0, cols, 1):
            print ("Q" + str(i + 1) + str(j + 1) + "=Q[" + str(i) + "," + str(j) + "]")


def auto_q_gen(num):
    for i in range(0, num, 1):
        print("q" + str(i + 1) + "=q[" + str(i) + "]")


def auto_coefficients_gen():
    pass


def auto_hessian_gen(num=4):
    for i in range(1, num + 1, 1):
        for j in range(i, num + 1, 1):
            hij = "h" + str(i) + str(j)
            print(hij + "=np.array(" + hij + ").reshape((1, len(" + hij + ")))")


def t_obj_func():
    A = np.random.random((11, 11))
    V = np.random.random((11, 1))
    V[0, 0] = 1

    v = V[1:]
    c = A[0, 0]
    q = A[0, 1:]
    p = A[1:, 0]
    Q = A[1:, 1:]
    print(A, c, q, p)
    print(V, v)

    obj_pre = (V.T).dot(A).dot(V)
    obj_cur = (v.T).dot(Q).dot(v) + q.dot(v) + (v.T).dot(p) + 1
    obj_test = (v.T).dot(Q).dot(v) + 2 * q.dot(v)
    print(obj_pre)
    print(obj_cur)
    print(obj_test)


def t_OPnP(configFile):
    config = loadYaml(configFile)
    opnp = OPnP(config)
    opnp.solve()


if __name__ == "__main__":
    # t_obj_func()
    t_OPnP("opnp.yaml")
    # auto_grobner_basis_gen(10, 10)
    # auto_q_gen(10)
    # auto_hessian_gen(4)
