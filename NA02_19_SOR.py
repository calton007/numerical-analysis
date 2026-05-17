# -*- coding:utf-8 -*-
# 题目：P60 T19 SOR方法 #
# 计算机131  李观波  1206020120 #
import numpy as np
def sor(A, b, x, real, w):
    D = np.matrix(np.diag(np.diag(A)))
    L = np.matrix(np.diag(np.diag(-A, -1), -1) + np.diag(np.diag(-A, -3), -3))
    U = np.matrix(np.diag(np.diag(-A, 1), 1) + np.diag(np.diag(-A, 3), 3))
    Lw = np.matrix((D - w * L) ** (-1) * ((1 - w) * D + w * U))
    f = np.matrix(w * (D - w * L) ** (-1) * b)
    n = 1
    while n <= 25:
        x = Lw * x + f
        if abs(x[0, 0]-real[0, 0]) < 0.00001:
            break
        n += 1
    print('迭代步数', n)
    print(x)
A = np.matrix('4 -1 0 -1 0 0;-1 4 -1 0 -1 0;0 -1 4 0 0 -1;-1 0 0 4 -1 0;0 -1 0 -1 4 -1;0 0 -1 0 -1 4', dtype=float)
b = np.matrix([[0, ], [5, ], [0, ], [6, ], [-2, ], [6, ]], dtype=float)
x = np.matrix([[0, ], [0, ], [0, ], [0, ], [0, ], [0, ]], dtype=float)
real = np.matrix([[1, ], [2, ], [1, ], [2, ], [1, ], [2, ]], dtype=float)
sor(A, b, x, real, 1.1)
sor(A, b, x, real, 1.2)
sor(A, b, x, real, 1.3)


