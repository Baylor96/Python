import numpy as np
import Functions as Func
import Functions_5 as Func_5
from Gradent_Descent import gradient_descent, newton, msgd, adam
from Backtracking_line_search import backtracking_line_search

if __name__ == "__main__":
    # Find the (1e-4)-suboptimal solution
    eps = 1e-4
    maximum_iterations = 65536
    initial_x = np.array([[0.0]])
    x, values, runtimes, gd_xs = gradient_descent(Func.weird_func, initial_x, eps,
                                                  maximum_iterations, backtracking_line_search)
    # x, values, runtimes, gd_xs = msgd(alg.weird_func, initial_x, eps,
    #                                   maximum_iterations, backtracking_line_search, momentum=0.9)
    # x, values, runtimes, gd_xs = adam(alg.weird_func, initial_x, eps, maximum_iterations)
    
    print('Optimum of the weird function found by GD with exact line search', x)

    # the hessian mat of the quadratic function
    H = np.array([[1, 0], [0, 30]])
    # the vector of linear coefficient of the quadratic function
    b = np.array([[0], [0]])
    # Run algorithms on the quadratic function
    # Start at (4,0.3)
    initial_x = np.array([[4.0], [0.3]])
    # Choose the quadratic objective. This notation defines a "closure", returning
    # an oracle function which takes x (and order) as its only parameter, and calls
    # obj.quadratic with parameters H and b defined above, and the parameters of 
    # the closure (x and order)
    func = lambda fx, order: Func.quadratic(H, b, fx, order)
    # Find the (1e-4)-suboptimal solution
    eps = 1e-4
    maximum_iterations = 65536
    x, values, runtimes, gd_xs = gradient_descent(func, initial_x, eps, maximum_iterations, backtracking_line_search)
    print('Optimum of the quad function found by GD with exact line search', x)
    
    x, values, runtimes, gd_xs = newton(func, initial_x, eps, maximum_iterations, backtracking_line_search)
    print('Optimum of the quad function found by GD with exact line search', x)   
#    initial_x = np.mat('1.0; 1.0;1.0')
    initial_x = np.array([[0], [2.0], [-12.0]])
    x, values, runtimes, gd_xs = gradient_descent(Func_5.fun_5_5, initial_x, eps,
                                                  maximum_iterations, backtracking_line_search)
    print('Optimum of the fun_5_5 function found by GD with exact line search', x)
    
    initial_x = np.array([[4], [-4]])
    x, values, runtimes, gd_xs = gradient_descent(Func_5.fun_5_7, initial_x, eps,
                                                  maximum_iterations, backtracking_line_search)
    print('Optimum of the fun_5_7 function found by GD with exact line search', x)

    initial_x = np.array([[0.8], [1]])
    x, values, runtimes, gd_xs = gradient_descent(Func_5.fun_5_9, initial_x, 1e-6,
                                                  maximum_iterations, backtracking_line_search)
    print('Optimum of the fun_5_7 function found by GD with exact line search', x)

    x, values, runtimes, gd_xs = newton(Func_5.fun_5_9, initial_x, 1e-6, maximum_iterations, backtracking_line_search)
    print('Optimum of the fun_5_7 function found by GD with exact line search', x)
