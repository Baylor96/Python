import numpy as np
import time
from Backtracking_line_search import backtracking_line_search


def bfgs(func, initial_x, initial_inv_h, eps=1e-5, maximum_iterations=65536, linesearch=backtracking_line_search,
         *linesearch_args):
    """ 
    BFGS Algorithm
    func:               the function to optimize It is called as "value, gradient, hessian = func( x, 2 )
    initial_x:          the starting point
    initial_inv_h:      the initialization for the inverse hessian
    eps:                the maximum allowed error in the resulting stepsize t
    maximum_iterations: the maximum allowed number of iterations
    linesearch:         the linesearch routine
    *linesearch_args:   the extra arguments of linesearch routine
    """

    if eps <= 0:
        raise ValueError("Epsilon must be positive")
    x = np.double(np.asarray(initial_x))

    if np.isscalar(initial_inv_h):
        inv_h = initial_inv_h * np.identity(x.size)
    else:
        inv_h = np.asarray(initial_inv_h.copy())

    # initialization
    values = []
    runtimes = []
    xs = []
    start_time = time.time()
    m = len(x)
    iterations = 0
    old_x = np.zeros(x.shape)
    old_gradient = np.zeros(x.shape)
    direction = np.zeros(x.shape)

    # BFGS gradient updatesa
    inv_h = initial_inv_h
    while True:

        value, gradient = func(x, 1)
        value = np.double(value)
        gradient = np.asarray(gradient)

        # updating the logs
        values.append(value)
        runtimes.append(time.time() - start_time)
        xs.append(x.copy())

        # TODO: code the entire bfgs algorithm
        if np.linalg.norm(gradient) ** 2 <= eps:
            break

        p_k = -inv_h.dot(gradient)
        alpha_k = linesearch(func, x, p_k)
        old_x = x
        x = old_x + alpha_k * p_k

        _, gradient_k1 = func(x, 1)
        gradient_k1 = np.asarray(gradient_k1)

        s_k = x - old_x
        y_k = gradient_k1 - gradient

        condition = np.asscalar(y_k.T.dot(s_k))

        if condition >= 1e-9:
            rho_k = 1 / condition
            inv_h = (np.identity(s_k.shape[0]) - rho_k * s_k.dot(y_k.T)).dot(inv_h).dot(
                (np.identity(y_k.shape[0]) - rho_k * y_k.dot(s_k.T))) + rho_k * s_k.dot(s_k.T)

        iterations += 1
        if iterations >= maximum_iterations:
            break

    return x, values, runtimes, xs
