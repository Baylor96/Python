import time
from Backtracking_line_search import *
import math


def gradient_descent(func, initial_x, eps=1e-5, maximum_iterations=65536, linesearch=None, *linesearch_args):
    """ 
    Gradient Descent
    func:               the function to optimize It is called as "value, gradient = func( x, 1 )
    initial_x:          the starting point, should be a float
    eps:                the maximum allowed error in the resulting stepsize t
    maximum_iterations: the maximum allowed number of iterations
    linesearch:         the linesearch routine
    *linesearch_args:   the extra arguments of linesearch routine
    """

    if eps <= 0:
        raise ValueError("Epsilon must be positive")
    x = initial_x

    # initialization
    values = []
    runtimes = []
    xs = []
    start_time = time.time()
    iterations = 0

    # gradient updates
    while True:

        value, gradient = func(x, 1)
        value = np.double(value)

        # updating the logs
        values.append(value)
        runtimes.append(time.time() - start_time)
        xs.append(x)

        # direction= (TODO)
        direction = -gradient

        # if (TODO: TERMINATION CRITERION): break
        if np.linalg.norm(gradient, ord=2) ** 2 <= eps:
            break

        #        t = linesearch( func, x, direction, *linesearch_args )

        # x= (TODO: UPDATE x)
        # print(value)
        # print(gradient)
        if linesearch is None:
            t = 0.01  # 固定步长
        else:
            t = linesearch(func, x, direction, *linesearch_args)
        x = x + t * -gradient
        # print('X', x)
        iterations += 1
        if iterations >= maximum_iterations:
            break

    return x, values, runtimes, xs


def newton(func, initial_x, eps=1e-5, maximum_iterations=65536, linesearch=backtracking_line_search, *linesearch_args):
    """ 
    Newton's Method
    func:               the function to optimize It is called as "value, gradient, hessian = func( x, 2 )
    initial_x:          the starting point
    eps:                the maximum allowed error in the resulting stepsize t
    maximum_iterations: the maximum allowed number of iterations
    linesearch:         the linesearch routine
    *linesearch_args:   the extra arguments of linesearch routine
    """

    if eps <= 0:
        raise ValueError("Epsilon must be positive")
    x = np.asarray(initial_x)

    # initialization
    values = []
    runtimes = []
    xs = []
    start_time = time.time()
    iterations = 0

    # newton's method updates
    while True:

        value, gradient, hessian = func(x, 2)

        value = np.double(value)
        gradient = np.asarray(gradient)
        hessian = np.asarray(hessian)

        # updating the logs
        values.append(value)
        runtimes.append(time.time() - start_time)
        xs.append(x)

        # direction = (TODO)

        # if (TODO: TERMINATION CRITERION): break
        hessian_i = np.linalg.inv(hessian)
        direction = - (hessian_i.dot(gradient))
        delta_x = gradient.T.dot(hessian_i).dot(gradient)
        if delta_x ** 2 <= eps:
            break
        t = linesearch(func, x, direction)

        # x = (TODO: UPDATE x)
        x = x + t * (-1 * hessian_i.dot(gradient))
        iterations += 1
        if iterations >= maximum_iterations:
            break

    return x, values, runtimes, xs


###############################################################################
def msgd(func, initial_x, eps=1e-5, maximum_iterations=65536, linesearch=None, momentum=0.9, *linesearch_args):
    """ 
    Gradient Descent
    func:               the function to optimize It is called as "value, gradient = func( x, 1 )
    initial_x:          the starting point, should be a float
    eps:                the maximum allowed error in the resulting stepsize t
    maximum_iterations: the maximum allowed number of iterations
    linesearch:         the linesearch routine
    *linesearch_args:   the extra arguments of linesearch routine
    """

    if eps <= 0:
        raise ValueError("Epsilon must be positive")
    x = initial_x

    # initialization
    values = []
    runtimes = []
    xs = []
    start_time = time.time()
    iterations = 0

    v = np.zeros_like(x)
    # gradient updates
    while True:

        value, gradient = func(x, 1)
        value = np.double(value)

        # updating the logs
        values.append(value)
        runtimes.append(time.time() - start_time)
        xs.append(x)

        # direction= (TODO)

        direction = -gradient

        # if (TODO: TERMINATION CRITERION): break
        if np.linalg.norm(gradient, ord=2) ** 2 <= eps:
            break

        #        t = linesearch( func, x, direction, *linesearch_args )

        # x= (TODO: UPDATE x)
        # print(value)
        # print(gradient)
        if linesearch is None:
            t = 0.01  # 固定步长
        else:
            t = linesearch(func, x, direction, *linesearch_args)
        v *= momentum
        v += t * gradient
        x -= v
        # print('X', x)
        iterations += 1
        if iterations >= maximum_iterations:
            break

    return x, values, runtimes, xs


###############################################################################
def adam(func, initial_x, eps=1e-5, maximum_iterations=65536):
    """ 
    Gradient Descent
    func:               the function to optimize It is called as "value, gradient = func( x, 1 )
    initial_x:          the starting point, should be a float
    eps:                the maximum allowed error in the resulting stepsize t
    maximum_iterations: the maximum allowed number of iterations
    linesearch:         the linesearch routine
    *linesearch_args:   the extra arguments of linesearch routine
    """

    if eps <= 0:
        raise ValueError("Epsilon must be positive")
    x = initial_x

    # initialization
    values = []
    runtimes = []
    xs = []
    start_time = time.time()
    iterations = 0

    v = np.zeros_like(x)
    alpha = 0.01
    beta_1 = 0.9
    beta_2 = 0.999  # initialize the values of the parameters
    epsilon = 1e-8
    m_k = 0
    v_k = 0
    k = 0
    # gradient updates
    while True:

        value, gradient = func(x, 1)
        value = np.double(value)

        # updating the logs
        values.append(value)
        runtimes.append(time.time() - start_time)
        xs.append(x)

        # direction= (TODO)

        # if (TODO: TERMINATION CRITERION): break
        if np.linalg.norm(gradient, ord=2) ** 2 <= eps:
            break

        #        t = linesearch( func, x, direction, *linesearch_args )

        # x= (TODO: UPDATE x)
        # print(value)
        # print(gradient)
        #        if linesearch is None:
        #            t = 0.01 #固定步长
        #        else:
        #            t = linesearch( func, x, direction, *linesearch_args )
        k += 1
        m_k = beta_1 * m_k + (1 - beta_1) * gradient
        v_k = beta_2 * v_k + (1 - beta_2) * (gradient * gradient)
        m_cap = m_k / (1 - (beta_1 ** k))
        v_cap = v_k / (1 - (beta_2 ** k))
        #        x_prev = x
        x = x - (alpha * m_cap) / (math.sqrt(v_cap) + epsilon)
        # print('X', x)
        iterations += 1
        if iterations >= maximum_iterations:
            break

    return x, values, runtimes, xs
