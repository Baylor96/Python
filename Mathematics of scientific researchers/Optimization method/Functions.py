import numpy as np
import matplotlib.pyplot as plt
import time
from math import exp


def weird_func(x, order=0):
    # f(x) = x^4 + 6x^2 + 12(x-4)e^(x-1)
    value = pow(x, 4) + 6 * pow(x, 2) + 12 * (x - 4) * exp(x - 1)

    if order == 0:
        return value
    elif order == 1:
        # f'(x) = 4x^3 + 12x + 12(x-3)e^(x-1)
        gradient = 4 * pow(x, 3) + 12 * x + 12 * (x - 3) * exp(x - 1)

        return value, gradient
    elif order == 2:
        # f'(x) = 4x^3 + 12x + 12(x-3)e^(x-1)
        gradient = 4 * pow(x, 3) + 12 * x + 12 * (x - 3) * exp(x - 1)

        # f''(x)= 12 (1 + e^(-1 + x) (-2 + x) + x^2)
        hessian = 12 * (1 + (x - 2) * exp(x - 1) + pow(x, 2))

        return value, gradient, hessian
    else:
        raise ValueError("The argument \"order\" should be 0, 1 or 2")


def quadratic(h, b, x, order=0):
    """ 
    Quadratic Objective
    H:          the Hessian matrix
    b:          the vector of linear coefficients
    x:          the current iterate
    order:      the order of the oracle. For example, order=1 returns the value of the function and its gradient while order=2 will also return the hessian
    """

    #    value = 0.5 * x.T * h * x + b.T * x
    value = 0.5 * x.T.dot(h).dot(x) + b.T.dot(x)
    if order == 0:
        return value
    elif order == 1:
        gradient = h.dot(x) + b
        #        gradient = H.dot( x) + b
        return value, gradient
    elif order == 2:
        gradient = h.dot(x) + b
        #        gradient = H.dot( x) + b
        hessian = h
        return value, gradient, hessian
    else:
        raise ValueError("The argument \"order\" should be 0, 1 or 2")


def rosenbrock(x, order=0):
    #    x = np.asmatrix(x)
    x1 = x[0]
    x2 = x[1]
    value = (x2 - x1 ** 2) ** 2 + (1 - x2) ** 2
    if order == 0:
        return value
    elif order == 1:
        gradient = np.zeros((2, 1))
        gradient[0, 0] = -4 * (x2 - x1 ** 2) * x1
        gradient[1, 0] = 4 * x2 - 2 * x1 ** 2 - 2
        return value, gradient
    elif order == 2:
        gradient = np.zeros((2, 1))
        gradient[0, 0] = -4 * (x2 - x1 ** 2) * x1
        gradient[1, 0] = 4 * x2 - 2 * x1 ** 2 - 2
        #        gradient = H.dot( x) + b
        hessian = np.zeros((2, 2))
        hessian[0, 0] = 12 * x1 ** 2 - 4 * x2
        hessian[0, 1] = -4 * x1
        hessian[1, 0] = -4 * x1
        hessian[1, 1] = 4

        return value, gradient, hessian
    else:
        raise ValueError("The argument \"order\" should be 0, 1 or 2")


def rosenbrock_func(theta):
    """Objective and gradient for the rosenbrock function"""
    x, y = theta
    obj = (1 - x) ** 2 + 100 * (y - x ** 2) ** 2

    grad = np.zeros(2)
    grad[0] = 2 * x - 400 * (x * y - x ** 3) - 2
    grad[1] = 200 * (y - x ** 2)
    return obj, grad


def sphere(theta):
    """l2-norm of the parameters"""
    return 0.5 * np.linalg.norm(theta) ** 2, theta


def matyas(theta):
    """Matyas function"""
    x, y = theta
    obj = 0.26 * (x ** 2 + y ** 2) - 0.48 * x * y
    grad = np.array([0.52 * x - 0.48 * y, 0.52 * y - 0.48 * x])
    return obj, grad


# @objective(xstar=(3, 0.5))
def beale(theta):
    """Beale's function"""
    x, y = theta
    a = 1.5 - x + x * y
    b = 2.25 - x + x * y ** 2
    c = 2.625 - x + x * y ** 3
    obj = a ** 2 + b ** 2 + c ** 2
    grad = np.array([
        2 * a * (y - 1) + 2 * b * (y ** 2 - 1) + 2 * c * (y ** 3 - 1),
        2 * a * x + 4 * b * x * y + 6 * c * x * y ** 2
    ])
    return obj, grad


# @objective(xstar=(1, 3))
def booth(theta):
    """Booth's function"""
    x, y = theta

    a = x + 2 * y - 7
    b = 2 * x + y - 5
    obj = a ** 2 + b ** 2
    grad = np.array([2 * a + 4 * b, 4 * a + 2 * b])
    return obj, grad


# @objective(xstar=(-0.5471975511965975, -1.5471975511965975))
def mccormick(theta):
    """McCormick function"""
    x, y = theta
    obj = np.sin(x + y) + (x - y) ** 2 - 1.5 * x + 2.5 * y + 1
    grad = np.array([np.cos(x + y) + 2 * (x - y) - 1.5,
                     np.cos(x + y) - 2 * (x - y) + 2.5])
    return obj, grad


# @objective(xstar=(0, 0))
def camel(theta):
    """Three-hump camel function"""
    x, y = theta
    obj = 2 * x ** 2 - 1.05 * x ** 4 + x ** 6 / 6 + x * y + y ** 2
    grad = np.array([
        4 * x - 4.2 * x ** 3 + x ** 5 + y,
        x + 2 * y
    ])
    return obj, grad


# @objective(xstar=(2.2029055201726027, 1.5707963267948954))
def michalewicz(theta):
    """Michalewicz function"""
    x, y = theta
    obj = - np.sin(x) * np.sin(x ** 2 / np.pi) ** 20 - np.sin(y) * np.sin(2 * y ** 2 / np.pi) ** 20

    grad = np.array([
        - np.cos(x) * np.sin(x ** 2 / np.pi) ** 20 - (40 / np.pi) * x *
        np.sin(x) * np.sin(x ** 2 / np.pi) ** 19 * np.cos(x ** 2 / np.pi),
        - np.cos(y) * np.sin(2 * y ** 2 / np.pi) ** 20 - (80 / np.pi) * y * np.sin(y) *
        np.sin(2 * y ** 2 / np.pi) ** 19 * np.cos(2 * y ** 2 / np.pi),
    ])

    return obj, grad


# @objective(xstar=(0, 0))
def bohachevsky1(theta):
    """One of the Bohachevsky functions"""
    x, y = theta
    obj = x ** 2 + 2 * y ** 2 - 0.3 * np.cos(3 * np.pi * x) - 0.4 * np.cos(4 * np.pi * y) + 0.7
    grad = np.array([
        2 * x + 0.3 * np.sin(3 * np.pi * x) * 3 * np.pi,
        4 * y + 0.4 * np.sin(4 * np.pi * y) * 4 * np.pi,
    ])
    return obj, grad


# @objective(xstar=(0, 0))
def zakharov(theta):
    """Zakharov function"""
    x, y = theta
    obj = x ** 2 + y ** 2 + (0.5 * x + y) ** 2 + (0.5 * x + y) ** 4
    grad = np.array([
        2.5 * x + y + 2 * (0.5 * x + y) ** 3,
        4 * y + x + 4 * (0.5 * x + y) ** 3,
    ])
    return obj, grad


# @objective(xstar=(1, 1 / np.sqrt(2)))
def dixon_price(theta):
    """Dixon-Price function"""
    x, y = theta
    obj = (x - 1) ** 2 + 2 * (2 * y ** 2 - x) ** 2
    grad = np.array([
        2 * x - 2 - 4 * (2 * y ** 2 - x),
        16 * (2 * y ** 2 - x) * y,
    ])
    return obj, grad


# @objective(xstar=(0, -1))
def goldstein_price(theta):
    """Goldstein-Price function"""
    x, y = theta
    obj = (1 + (x + y + 1) ** 2 * (19 - 14 * x + 3 * x ** 2 - 14 * y + 6 * x * y + 3 * y ** 2)) * \
          (30 + (2 * x - 3 * y) ** 2 *
           (18 - 32 * x + 12 * x ** 2 + 48 * y - 36 * x * y + 27 * x ** 2))
    grad = np.array([
        ((2 * x - 3 * y) ** 2 * (78 * x - 36 * y - 32) + (8 * x - 12 * y) *
         (39 * x ** 2 - 36 * x * y - 32 * x + 48 * y + 18)) *
        ((x + y + 1) ** 2 * (3 * x ** 2 + 6 * x * y - 14 * x + 3 * y ** 2 - 14 * y + 19) + 1) +
        ((2 * x - 3 * y) ** 2 * (39 * x ** 2 - 36 * x * y - 32 * x + 48 * y + 18) + 30) *
        ((x + y + 1) ** 2 *
         (6 * x + 6 * y - 14) + (2 * x + 2 * y + 2) *
         (3 * x ** 2 + 6 * x * y - 14 * x + 3 * y ** 2 - 14 * y + 19)),
        ((-36 * x + 48) * (2 * x - 3 * y) ** 2 + (-12 * x + 18 * y) *
         (39 * x ** 2 - 36 * x * y - 32 * x + 48 * y + 18)) *
        ((x + y + 1) ** 2 * (3 * x ** 2 + 6 * x * y - 14 * x + 3 * y ** 2 - 14 * y + 19) + 1) +
        ((2 * x - 3 * y) ** 2 * (39 * x ** 2 - 36 * x * y - 32 * x + 48 * y + 18) + 30) *
        ((x + y + 1) ** 2 * (6 * x + 6 * y - 14) + (2 * x + 2 * y + 2) *
         (3 * x ** 2 + 6 * x * y - 14 * x + 3 * y ** 2 - 14 * y + 19)),
    ])
    return obj, grad


# @objective(xstar=(-2.903534, -2.903534))
def styblinski_tang(theta):
    """Styblinski-Tang function"""
    x, y = theta
    obj = 0.5 * (x ** 4 - 16 * x ** 2 + 5 * x + y ** 4 - 16 * y ** 2 + 5 * y)
    grad = np.array([
        2 * x ** 3 - 16 * x + 2.5,
        2 * y ** 3 - 16 * y + 2.5,
    ])
    return obj, grad


def draw_contour(func, gd_xs, newton_xs, fig, levels=np.arange(5, 1000, 10), x=np.arange(-5, 5.1, 0.05),
                 y=np.arange(-5, 5.1, 0.05)):
    """ 
    Draws a contour plot of given iterations for a function
    func:       the contour levels will be drawn based on the values of func
    gd_xs:      gradient descent iterates
    newton_xs:  Newton iterates
    fig:        figure index
    levels:     levels of the contour plot
    x:          x coordinates to evaluate func and draw the plot
    y:          y coordinates to evaluate func and draw the plot
    """
    z = np.zeros((len(x), len(y)))

    for i in range(len(x)):
        for j in range(len(y)):
            z[i, j] = func(np.matrix([x[i], y[j]]).T, 0)

    plt.figure(fig)
    plt.contour(x, y, z.T, levels, colors='0.75')
    plt.ion()
    plt.show()

    line_gd, = plt.plot(gd_xs[0][0, 0], gd_xs[0][1, 0], linewidth=2, color='r', marker='o', label='GD')
    line_newton, = plt.plot(newton_xs[0][0, 0], newton_xs[0][1, 0], linewidth=2, color='m', marker='o', label='Newton')

    legend = plt.legend(handles=[line_gd, line_newton])
    plt.draw()
    time.sleep(1)

    for i in range(1, max(len(gd_xs), len(newton_xs))):
        line_gd.set_xdata(np.append(line_gd.get_xdata(), gd_xs[min(i, len(gd_xs) - 1)][0, 0]))
        line_gd.set_ydata(np.append(line_gd.get_ydata(), gd_xs[min(i, len(gd_xs) - 1)][1, 0]))

        line_newton.set_xdata(np.append(line_newton.get_xdata(), newton_xs[min(i, len(newton_xs) - 1)][0, 0]))
        line_newton.set_ydata(np.append(line_newton.get_ydata(), newton_xs[min(i, len(newton_xs) - 1)][1, 0]))

        legend.get_texts()[0].set_text(" GD, %d iterations" % min(i, len(gd_xs) - 1))
        legend.get_texts()[1].set_text(" Newton, %d iterations" % min(i, len(newton_xs) - 1))

        plt.draw()
        input("Press Enter to continue...")
