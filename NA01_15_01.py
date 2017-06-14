# -*- coding:utf-8 -*-
# 题目：P32 T15 顺序消元法 #
# 计算机131  李观波  1206020120 #
import numpy as np


def gauss(n):
    print 'n =', n
    A = np.mat(np.diag(3 * np.ones(n)) + np.diag(9 * np.ones(n-1), -1) + np.diag(1 * np.ones(n-1), 1), dtype=float)
    x = np.mat(np.zeros(n), dtype=float).T
    b = np.mat(13 * np.ones((n,1)), dtype=float)
    b[0, 0] = 4
    b[n - 1, 0] = 12
    flag = True
    # 判断顺序消元法是否能进行到底
    for i in range(2, n):
        if np.linalg.det(A[0:i, 0:i]) == 0:
            print 'i = ', i, '时，顺数主子式为0'
            flag = False
            break
    # 顺序消元
    if flag:
        for i in range(0,n):
                a = 1.0 / A[i, i]
                am = A[:, i]
                an = am
                an[0:i + 1] = 0
                en = np.mat(np.zeros((1, n)), dtype=float)
                en[i, 0] = 1
                Gn = np.mat(np.eye(n), dtype=float) - a * an * en
                A = Gn * A
                b = Gn * b
        print x
gauss(10)
gauss(100)




