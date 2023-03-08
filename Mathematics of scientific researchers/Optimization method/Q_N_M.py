import numpy as np
from DFP import dfp
from BFGS import bfgs
import Functions as Func
import Functions_5 as Func_5
from Backtracking_line_search import backtracking_line_search


if __name__ == "__main__":
    # Find the (1e-4)-suboptimal solution
    eps = 1e-4
    maximum_iterations = 65536
    initial_x = np.array([[0.0]], dtype=np.float64)
    x, values, runtimes, gd_xs = dfp(Func.weird_func, initial_x, 0.001, eps, maximum_iterations,
                                     backtracking_line_search)
    print('Optimum of the weird function found by GD with inexact line search', x)

    # the hessian mat of the quadratic function
    H = np.array([[1, 0], [0, 30]], dtype=np.float64)
    # the vector of linear coefficient of the quadratic function
    b = np.array([[0], [0]], dtype=np.float64)
    # Run algorithms on the quadratic function
    # Start at (4,0.3)
    initial_x = np.array([[4.0], [0.3]], dtype=np.float64)
    # Choose the quadratic objective. This notation defines a "closure", returning
    # an oracle function which takes x (and order) as its only parameter, and calls
    # obj.quadratic with parameters H and b defined above, and the parameters of 
    # the closure (x and order)
    func = lambda x, order: Func.quadratic(H, b, x, order)
    # Find the (1e-4)-suboptimal solution
    eps = 1e-4
    maximum_iterations = 65536
    x, values, runtimes, gd_xs = dfp(func, initial_x, 0.001, eps, maximum_iterations, backtracking_line_search)
    print('Optimum of the quad function found by GD with inexact line search', x)

    initial_x = np.array([[1], [1]], dtype=np.float64)
    x, values, runtimes, gd_xs = dfp(Func_5.fun_5_9, initial_x, 1e-6, maximum_iterations, backtracking_line_search)
    print('Optimum of the fun_5_9 function found by GD with inexact line search', x)

    x, values, runtimes, gd_xs = bfgs(Func_5.fun_5_9, initial_x, 1e-6, maximum_iterations, backtracking_line_search)
    print('Optimum of the fun_5_9 function found by GD with inexact line search', x)
