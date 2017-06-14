# -*- coding:utf-8 -*-
# 题目：P32 T14 追赶法求解方程组 #
# 计算机131  李观波  1206020120 #
import numpy as np


def chasingmethod(n):
    print 'n =', n
    A = np.mat(np.diag(-4 * np.ones(n)) + np.diag(1 * np.ones(n-1), -1) + np.diag(1 * np.ones(n-1), 1), dtype=float)
    x = np.mat(np.zeros(n), dtype=float).T
    L = np.mat(np.eye(n), dtype=float)
    U = np.mat(np.zeros((n, n)), dtype=float)
    b = np.mat(-15 * np.ones((n, 1)))
    b[0, 0] = -27
    # 矩阵可逆
    if np.linalg.matrix_rank(A) == n:
        # LU分解
        U[0, 0] = A[0, 0]
        for i in range(1, n):
            U[i - 1, i] = A[i - 1, i]
            L[i, i - 1] = A[i, i - 1] / U[i - 1, i - 1]
            U[i, i] = A[i, i] - L[i, i - 1] * U[i - 1, i]
        # 解Ly = b
        y = np.mat(np.zeros((n, 1)))
        y[0, 0] = b[0, 0]
        for i in range(1, n):
            y[i, 0] = b[i, 0] - L[i, i - 1] * y[i - 1, 0]
        # 解Ux = y
        x[n - 1, 0] = y[n - 1, 0] / U[n - 1, n - 1]
        for i in range(n - 1, 0, -1):
            x[i - 1] = (y[i - 1, 0] - U[i-1, i] * x[i, 0]) / U[i - 1, i - 1]
        print x
    else:
        print '系数矩阵A不可逆'
chasingmethod(10)
chasingmethod(100)


