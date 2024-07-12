import JacobiMethod as jm
import GauBSeidelMethod as gsm
import GradientMethod as gm
import ConigatedGradientMethod as cgm
import numpy as np
import time

def solve(A, b, tol, max_iter, method, x_0=None):

    if x_0 is None:
        x_0 = np.zeros(A.shape[0])

    start = time.time()
    if method == 'jacobi':
        x, k = jm.solve(A, b, x_0, tol, max_iter)
    elif method == 'gauss_seidel':
        x, k = gsm.solve(A, b, x_0, tol, max_iter)
    elif method == 'gradient':
        x, k = gm.solve(A, b, x_0, tol, max_iter)
    elif method == 'conjugate_gradient':
        x, k = cgm.solve(A, b, x_0, tol, max_iter)
    else:
        raise ValueError(f'Method {method} not supported')
    end = time.time()
    return x, k, end-start
    