# -*- coding:utf-8 -*-
# 题目：P147 T17 (1) #
# 计算机131  李观波  1206020120 #
import numpy as np
import math


# Romberg方法 #
# f:被积函数  a:积分下限  b:积分上限  e:精度值 #
def romberg(f, a, b, e):
    n = 1  # 二分次数
    while True:
        R = np.mat(np.zeros((n + 1, n + 1)), dtype=float)
        R[0, 0] = (b - a) / 2.0 * (f(a) + f(b))
        for i in range(1, n + 1):  # 求第一列
            h = (b - a) * 1.0 / 2**i
            s = 0
            for k in range(1, 2**(i-1) + 1):
                s = s + f(a + (2 * k - 1) * h)
            R[i, 0] = R[i - 1, 0] / 2 + h * s

        for j in range(1, n + 1):
            fac = 1.0 / (4**j - 1)
            for m in range(j, n + 1):
                R[m, j] = R[m, j - 1] + fac * (R[m, j - 1] - R[m - 1, j - 1])
        if abs(R[n - 1, n - 1] - R[n, n]) < e:
            break
        n += 1
    print R
    return R[n, n]

# 被积函数 #
def fx(x):
    return math.e**x * math.sin(x)

print romberg(fx, 0, 3, 0.000001)

