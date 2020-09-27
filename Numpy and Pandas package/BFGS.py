from numpy import *


# fun
def fun(x):
    return 100 * (x[0, 0] ** 2 - x[1, 0]) ** 2 + (x[0, 0] - 1) ** 2


# gfun
def gfun(x):
    result = zeros((2, 1))
    result[0, 0] = 400 * x[0, 0] * (x[0, 0] ** 2 - x[1, 0]) + 2 * (x[0, 0] - 1)
    result[1, 0] = -200 * (x[0, 0] ** 2 - x[1, 0])
    return result


def bfgs(fun, gfun, x0):
    result = []
    maxk = 500
    rho = 0.55
    sigma = 0.4
    m = shape(x0)[0]
    Bk = eye(m)
    k = 0
    while (k < maxk):
        gk = mat(gfun(x0))  # 计算梯度
        dk = mat(-linalg.solve(Bk, gk))
        m = 0
        mk = 0
        while (m < 20):
            newf = fun(x0 + rho ** m * dk)
            oldf = fun(x0)
            if (newf < oldf + sigma * (rho ** m) * (gk.T * dk)[0, 0]):
                mk = m
                break
            m = m + 1

        # BFGS校正
        x = x0 + rho ** mk * dk
        sk = x - x0
        yk = gfun(x) - gk
        if (yk.T * sk > 0):
            Bk = Bk - (Bk * sk * sk.T * Bk) / (sk.T * Bk * sk) + (yk * yk.T) / (yk.T * sk)

        k = k + 1
        x0 = x
        result.append(fun(x0))

    return result


import matplotlib.pyplot as plt

x0 = mat([[-1.2], [1]])
result = bfgs(fun, gfun, x0)

n = len(result)
ax = plt.figure().add_subplot(111)
x = arange(0, n, 1)
y = result
ax.plot(x, y)

plt.show()