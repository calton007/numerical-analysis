# -*- coding:utf-8 -*-
# 题目：P124 T17 (2) #
# 计算机131  李观波  1206020120 #

import numpy as np
from NA04_16 import lagrange as Ln
from NA04_16 import newton_forward as NF
from NA04_16 import newton_backward as NB
a = -1
b = 1
x = []
fx = []
h = (b - a) / 5.0
print 'n = 5'
for i in range(6):
    t = a + i * h
    x.append(a + i * h)
    fx.append(1.0/(1+25 * t * t))
for i in range(20):
    t = -0.95 + i * 0.1
    print 'i = ', i
    print '真实值:', 1.0/(1+25 * t * t)
    print 'Lagrange插值:', Ln(t, x, fx)
    print 'Newton向前插值:', NF(t, x, fx, h)
    print 'Newton向后插值:', NB(t, x, fx, h)

a = -1
b = 1
x = []
fx = []
h = (b - a) / 10.0
print 'n = 10'
for i in range(11):
    t = a + i * h
    x.append(a + i * h)
    fx.append(1.0/(1+25 * t * t))
for i in range(20):
    t = -0.95 + i * 0.1
    print 'i = ', i
    print '真实值:', 1.0/(1+25 * t * t)
    print 'Lagrange插值:', Ln(t, x, fx)
    print 'Newton向前插值:', NF(t, x, fx, h)
    print 'Newton向后插值:', NB(t, x, fx, h)


