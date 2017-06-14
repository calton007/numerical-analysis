# -*- coding:utf-8 -*-
# 题目：P32 T15 列主元法 #
# 计算机131  李观波  1206020120 #
import numpy as np


def gauss2(n):
    print 'n =', n
    A = np.mat(np.diag(3 * np.ones(n)) + np.diag(9 * np.ones(n-1), -1) + np.diag(1 * np.ones(n-1), 1), dtype=float)
    x = np.mat(np.zeros(n), dtype=float).T
    b = np.mat(13 * np.ones((n,1)), dtype=float)
    b[0, 0] = 4
    b[n - 1, 0] = 12
    for i in range(0, n - 1):
        # 选主元
        MAX = abs(A[i, i])
        r = i
        for j in range(i + 1, n):
            if MAX < abs(A[j, i]):
                MAX = abs(A[j, i])
                r = j
        # 换行
        if r != i:
            temp = np.mat(A[i, :].tolist())
            A[i, :] = A[r, :]
            A[r, :] = temp
            b[i, 0],b[r, 0] = b[r, 0],b[i, 0]
        # 消元
        for k in range(i + 1, n):
            for j in range(i + 1, n):
                A[k,j] = A[k,j] - A[i, j] * A[k, i] / A[i, i]
            b[k, 0] = b[k, 0] - b[i, 0] * A[k, i] / A[i, i]
            A[k, i] = 0
    # 回代
    x[n - 1, 0] = b[n - 1, 0] / A[n - 1, n - 1]
    for i in range(n - 2, -1, -1):
        sum = 0.0
        for j in range(i + 1, n):
            sum = sum + A[i, j] * x[j, 0]
        x[i, 0] = (b[i, 0] - sum) / A[i, i]
    print x
gauss2(10)
gauss2(100)


