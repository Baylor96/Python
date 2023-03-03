import numpy as np


def backtracking_line_search(func, x, direction, alpha=0.4, beta=0.9, maximum_iterations=65536):
    """ 
    Backtracking linesearch
    func:               the function to optimize It is called as "value, gradient = func( x, 1 )
    x:                  the current iterate
    direction:          the direction along which to perform the linesearch
    alpha:              the alpha parameter to backtracking linesearch
    beta:               the beta parameter to backtracking linesearch
    eps:                the maximum allowed error in the resulting stepsize t
    maximum_iterations: the maximum allowed number of iterations
    """

    if alpha <= 0:
        raise ValueError("Alpha must be positive")
    if alpha >= 0.5:
        raise ValueError("Alpha must be less than 0.5")
    if beta <= 0:
        raise ValueError("Beta must be positive")
    if beta >= 1:
        raise ValueError("Beta must be less than 1")

    value_0, gradient_0 = func(x, 1)
    value_0 = np.asarray(value_0)
    gradient_0 = np.asarray(gradient_0)
    value_0 = np.double(value_0)

    t = 1
    iterations = 0
    while True:        
    
        # if (TODO: TERMINATION CRITERION): break
        lvalue = func(x + t * direction, 0)
        rvalue = func(x, 0) + alpha * t * gradient_0.T.dot(direction)
        if lvalue <= rvalue:
            break
        # t = TODO: BACKTRACKING LINE SEARCH
        else:
            t = beta * t
        iterations += 1
        if iterations >= maximum_iterations:
            break
    
    return t
