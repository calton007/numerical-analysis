# -*- coding:utf-8 -*-
# 题目：P124 T16 通用程序 #
# 计算机131  李观波  1206020120 #


# Lagrange插值 #
# x, fx为已知函数值， n为分段数， t为待求点#
def lagrange(t, x, fx):
    result = 0.0
    n = len(x)
    for i in range(n):
        temp = 1
        for j in range(n):
            if i != j:
                temp = temp * (t-x[j])/(x[i]-x[j])
        temp *= fx[i]
        result += temp
    return result


# Newton 插值 #
# 差分表递归求解 #
def f(serial, x, fx):
    if len(serial) == 1:
        return fx[serial[0]]
    else:
        serial1 = serial[0:-1]
        serial2 = serial[1:]
        return f(serial2, x, fx)-f(serial1, x, fx)


# 前插开始区间 #
# 如果t小于x0，计算结果出错 #
def where_to_begin(t, x):
    for i in range(1, len(x)):
        if x[i - 1] <= t <= x[i]:
            break
    return i - 1


#  后插结束区间 #
# 如果t大于xn，计算结果出错 #
def where_to_end(t, x):
    for i in range(len(x)-1, 1, -1):
        if x[i - 1] <= t <= x[i]:
            break
    return i


# 牛顿向前插值 #
def newton_forward(t, x, fx, h):
    end = len(x)
    begin = where_to_begin(t, x) # 开始区间
    t = (t - x[begin]) / h
    temp = 1
    result = fx[begin]
    for i in range(begin + 1, end):
        j = i - begin
        temp *= ((t - j + 1.0) / j)
        result += (temp * f(range(begin, begin + j + 1), x, fx))
    return result


# 牛顿向后插值 #
def newton_backward(t, x, fx, h):
    end = where_to_end(t, x) # 结束区间
    begin = 0
    t = (t - x[end]) / h
    temp = 1
    result = fx[end]
    for i in range(end, begin, -1):
        j = end - i + 1
        temp *= ((t + j - 1.0) / j)
        result += (temp * f(range(end - j, end + 1), x, fx))
    return result


