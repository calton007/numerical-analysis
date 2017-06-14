# -*- coding:utf-8 -*-
# 题目：P124 T17 (1) #
# 计算机131  李观波  1206020120 #

import numpy as np
from NA04_16 import lagrange as Ln
from NA04_16 import newton_forward as NF
from NA04_16 import newton_backward as NB
a = 1
b = 2
x = []
fx = []
h = (b - a) / 10.0
for i in range(11):
    t = a + i * h
    x.append(a + i * h)
    fx.append(np.log(t))
print 'ln1.54'
print 'Lagrange插值:', Ln(1.54, x, fx)
print 'Newton向前插值:', NF(1.54, x, fx, h)
print 'Newton向后插值:', NB(1.54, x, fx, h)
print 'ln1.98'
print 'Lagrange插值:', Ln(1.98, x, fx)
print 'Newton向前插值:', NF(1.98, x, fx, h)
print 'Newton向后插值:', NB(1.98, x, fx, h)


