# -*- coding:utf-8 -*-
# 题目：P147 T18 #
# 计算机131  李观波  1206020120 #


# 复合Gauss求积公式 #
# f:被积函数 a:积分下限 b:积分上限 e:精度值#
# 区间分段以m以2的n次方增加 #
def gauss2(f, a, b, e):
    result = [0, ]
    n = 1
    m = 1
    while True:
        h = (b - a) * 1.0 / m
        s = h / 2 * (f(a) + f(b))
        for i in range(1, m):
            xk = a + i * h
            s += h * f(xk)
        result.append(s)
        if abs(result[n] - result[n - 1]) < e:
            break
        n += 1
        m *= 2
    print result
    return result[n]

# 复合Gauss求积公式 #
# f:被积函数 a:积分下限 b:积分上限 e:精度值#
# 区间分段逐次增加1 #
def gauss1(f, a, b, e):
    result = [0, ]
    m = 1
    while True:
        h = (b - a) * 1.0 / m
        s = h / 2 * (f(a) + f(b))
        for i in range(1, m):
            xk = a + i * h
            s += h * f(xk)
        result.append(s)
        if abs(result[m] - result[m - 1]) < e:
            break
        m += 1
    print result
    return result[m]


def fx(x):
    x2 = x**2 / 3.0  # x = x / math.sqrt(3)
    return 4.0/(1+x2)

print gauss1(fx, 0, 2, 0.00001)
print gauss2(fx, 0, 2, 0.00001)
