# -*- coding:utf-8 -*-
# 题目：P92 T8 乘幂法 #
# 计算机131  李观波  1206020120 #
import numpy as np
def power(A, n):
    x = np.mat(np.eye(n), dtype=float)
    y = x / abs(x).max()
    x = A * y
    for i in range(25):
        y = x / abs(x).max()
        x = A * y
    print '主特征值为:', x.max()
A1 = np.mat([[49.0/8,-131.0/8,-43.0/4],[11.0/8,-17.0/8,-9.0/4],[-1.0/2,7.0/2,3.0]],dtype=float)
A2 = np.mat([[7,3,-2],[3,4,-1],[-2,-1,3]],dtype=float)
power(A1, 3)
power(A2, 3)
