import numpy as np
import time


def dfp(func, initial_x, initial_inv_h, eps=1e-5, maximum_iterations=65536, linesearch=None, *linesearch_args):
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
    x = np.asarray(initial_x)

    if np.isscalar(initial_inv_h):
        H_k = initial_inv_h * np.identity(x.size)
    else:
        H_k = np.asarray(initial_inv_h)

    # initialization
    values = []
    runtimes = []
    xs = []
    start_time = time.time()
    iterations = 0

    # gradient updates
    x_k = x
    while True:

        f_k, g_k = func(x_k, 1)
        f_k = np.double(f_k)
        g_k = np.asarray(g_k)
        p_k = - 1.0 * np.asarray(H_k).dot(g_k)

        if linesearch is None:
            t = 0.01  # 固定步长
        else:
            t = linesearch(func, x, p_k, *linesearch_args)
        # updating the logs
        values.append(f_k)
        x_k_old = x_k.copy()
        x_k += p_k * t

        g_k_old = g_k
        f_k_old = f_k
        f_k, g_k = func(x_k, 1)
        s_k = x_k - x_k_old
        y_k = g_k - g_k_old
        if s_k.T.dot(y_k) > 0:
            H_k = H_k - 1.0 * (H_k.dot(y_k).dot(y_k.T).dot(H_k)) / (y_k.T.dot(H_k).dot(y_k)) \
                  + 1.0 * (s_k.dot(s_k.T)) / (y_k.T.dot(s_k))

        runtimes.append(time.time() - start_time)
        xs.append(x_k)

        if np.linalg.norm(g_k) ** 2 <= eps:
            break

        # print('X', x)
        iterations += 1
        if iterations >= maximum_iterations:
            break

    return x, values, runtimes, xs
