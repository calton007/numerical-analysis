# -*- coding:utf-8 -*-
# 题目：P60 T19 最速下降法 #
# 计算机131  李观波  1206020120 #
import numpy as np
def Grad(A, b, x, real):
    r = b - A * x
    t = r.T * r / (r.T * A * r)
    n = 1
    while n <= 25:
        x = x + t[0,0] * r
        t = r.T * r / (r.T * A * r)
        r = b - A * x
        if abs(x[0, 0] - real[0, 0]) < 0.00001:
            break
        n += 1
    print '迭代步数', n
    print x
A = np.mat('4 -1 0 -1 0 0;-1 4 -1 0 -1 0;0 -1 4 0 0 -1;-1 0 0 4 -1 0;0 -1 0 -1 4 -1;0 0 -1 0 -1 4', dtype=float)
b = np.mat([[0, ], [5, ], [0, ], [6, ], [-2, ], [6, ]], dtype=float)
x = np.mat([[0, ], [0, ], [0, ], [0, ], [0, ], [0, ]], dtype=float)
real = np.mat([[1, ], [2, ], [1, ], [2, ], [1, ], [2, ]], dtype=float)
Grad(A, b, x, real)


