import numpy as np
from math import exp


def fun_5_1(x, order=0):
    x = np.asarray(x)
    x1 = x[0]
    x2 = x[1]
    value = 2 * x1 ** 2 - 2 * x1 * x2 + 2 * x1 + x2 ** 2 - 2 * x2
    if order == 0:
        return value
    elif order == 1:
        gradient = np.zeros((2, 1))
        gradient[0, 0] = 4 * x1 - 2 * x2 + 2
        gradient[1, 0] = 2 * x2 - 2 * x1 - 2
        return value, gradient
    elif order == 2:
        gradient = np.zeros((2, 1))
        gradient[0, 0] = 4 * x1 - 2 * x2 + 2
        gradient[1, 0] = 2 * x2 - 2 * x1 - 2
        #        gradient = H.dot( x) + b
        hessian = np.zeros((2, 2))
        hessian[0, 0] = 4
        hessian[0, 1] = -2
        hessian[1, 0] = -2
        hessian[1, 1] = 2

        return value, gradient, hessian
    else:
        raise ValueError("The argument \"order\" should be 0, 1 or 2")


def fun_5_5(x, order=0):
    x = np.asarray(x)
    x1 = x[0]
    x2 = x[1]
    x3 = x[2]
    value = (x1 + 5) ** 2 + (x2 + 8) ** 2 + (x3 + 7) ** 2 + 2 * (x1 ** 2) * (x2 ** 2) + 4 * (x1 ** 2) * (x3 ** 2)
    if order == 0:
        return value
    elif order == 1:
        gradient = np.zeros((3, 1))
        gradient[0, 0] = 4 * x1 * (x2 ** 2) + 8 * x1 * (x3 ** 2) + 2 * x1 + 10
        gradient[1, 0] = 4 * x2 * (x1 ** 2) + 2 * x2 + 16
        gradient[2, 0] = 8 * x3 * (x1 ** 2) + 2 * x3 + 14
        return value, gradient
    elif order == 2:
        gradient = np.zeros((3, 1))
        gradient[0, 0] = 4 * x1 * (x2 ** 2) + 8 * x1 * (x3 ** 2) + 2 * x1 + 10
        gradient[1, 0] = 4 * x2 * (x1 ** 2) + 2 * x2 + 16
        gradient[2, 0] = 8 * x3 * (x1 ** 2) + 2 * x3 + 14
        #        gradient = H.dot( x) + b
        hessian = np.zeros((3, 3))
        hessian[0, 0] = 4 * x2 ** 2 + 8 * x3 ** 2 + 2
        hessian[0, 1] = 8 * x1 * x2
        hessian[0, 2] = 16 * x1 * x3
        hessian[1, 0] = 8 * x1 * x2
        hessian[1, 1] = 4 * x1 ** 2 + 2
        hessian[1, 2] = 0
        hessian[2, 0] = 16 * x1 * x3
        hessian[2, 1] = 0
        hessian[2, 2] = 8 * x1 ** 2 + 2
        return value, gradient, hessian
    else:
        raise ValueError("The argument \"order\" should be 0, 1 or 2")


def fun_5_7(x, order=0):
    x = np.asarray(x)
    x1 = x[0]
    x2 = x[1]
    value = (x1 ** 2 + x2 ** 2 - 1) ** 2 + (x1 + x2 - 1) ** 2
    if order == 0:
        return value
    elif order == 1:
        gradient = np.zeros((2, 1))
        gradient[0, 0] = 2 * x1 + 2 * x2 + 4 * x1 * (x1 ** 2 + x2 ** 2 - 1) - 2
        gradient[1, 0] = 2 * x1 + 2 * x2 + 4 * x2 * (x1 ** 2 + x2 ** 2 - 1) - 2
        return value, gradient
    elif order == 2:
        gradient = np.zeros((2, 1))
        gradient[0, 0] = 2 * x1 + 2 * x2 + 4 * x1 * (x1 ** 2 + x2 ** 2 - 1) - 2
        gradient[1, 0] = 2 * x1 + 2 * x2 + 4 * x2 * (x1 ** 2 + x2 ** 2 - 1) - 2
        #        gradient = H.dot( x) + b
        hessian = np.zeros((2, 2))
        hessian[0, 0] = 12 * x1 ** 2 + 4 * x2 ** 2 - 2
        hessian[0, 1] = 8 * x1 * x2 + 2
        hessian[1, 0] = 8 * x1 * x2 + 2
        hessian[1, 1] = 4 * x1 ** 2 + 12 * x2 ** 2 - 2
        return value, gradient, hessian
    else:
        raise ValueError("The argument \"order\" should be 0, 1 or 2")


def fun_5_9(x, order=0):
    x = np.asarray(x)
    x1 = x[0]
    x2 = x[1]
    value = -(x2 ** 2) * exp(1 - x1 ** 2 - 20 * (x1 - x2) ** 2)
    if order == 0:
        return value
    elif order == 1:
        gradient = np.zeros((2, 1))
        gradient[0, 0] = (x2 ** 2) * exp(1 - x1 ** 2 - 20 * (x1 - x2) ** 2) * (42 * x1 - 40 * x2)
        gradient[1, 0] = - 2 * x2 * exp(1 - x1 ** 2 - 20 * (x1 - x2) ** 2) - (x2 ** 2) * exp(
            1 - x1 ** 2 - 20 * (x1 - x2) ** 2) * (40 * x1 - 40 * x2)
        return value, gradient
    elif order == 2:
        gradient = np.zeros((2, 1))
        gradient[0, 0] = (x2 ** 2) * exp(1 - x1 ** 2 - 20 * (x1 - x2) ** 2) * (42 * x1 - 40 * x2)
        gradient[1, 0] = - 2 * x2 * exp(1 - x1 ** 2 - 20 * (x1 - x2) ** 2) - (x2 ** 2) * exp(
            1 - x1 ** 2 - 20 * (x1 - x2) ** 2) * (40 * x1 - 40 * x2)
        #        gradient = H.dot( x) + b
        hessian = np.zeros((2, 2))
        hessian[0, 0] = 42 * x2 ** 2 * exp(1 - x1 ** 2 - 20 * (x1 - x2) ** 2) - x2 ** 2 * exp(
            1 - x1 ** 2 - 20 * (x1 - x2) ** 2) * (42 * x1 - 40 * x2) ** 2
        hessian[0, 1] = 2 * x2 * exp(1 - x1 ** 2 - 20 * (x1 - x2) ** 2) * (42 * x1 - 40 * x2) - 40 * x2 ** 2 * exp(
            1 - x1 ** 2 - 20 * (x1 - x2) ** 2) + x2 ** 2 * exp(1 - x1 ** 2 - 20 * (x1 - x2) ** 2) * (
                                    40 * x1 - 40 * x2) * (42 * x1 - 40 * x2)
        hessian[1, 0] = hessian[0, 1]
        hessian[1, 1] = 40 * x2 ** 2 * exp(1 - x1 ** 2 - 20 * (x1 - x2) ** 2) - 2 * exp(
            1 - x1 ** 2 - 20 * (x1 - x2) ** 2) - x2 ** 2 * exp(1 - x1 ** 2 - 20 * (x1 - x2) ** 2) * (
                                    40 * x1 - 40 * x2) ** 2 - 4 * x2 * exp(1 - x1 ** 2 - 20 * (x1 - x2) ** 2) * (
                                    40 * x1 - 40 * x2)

        return value, gradient, hessian
    else:
        raise ValueError("The argument \"order\" should be 0, 1 or 2")
