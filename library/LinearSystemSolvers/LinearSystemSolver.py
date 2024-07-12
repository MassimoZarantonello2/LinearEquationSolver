import sys
sys.path.append('library/LinearSystemSolvers')
import LinearSystemSolvers.JacobiMethod as jm
import LinearSystemSolvers.GauBSeidelMethod as gsm
import LinearSystemSolvers.GradientMethod as gm
import LinearSystemSolvers.ConigatedGradientMethod as cgm
import numpy as np
import time

def solve(A, b, tol, max_iter, method, x_0=None):

    if x_0 is None:
        x_0 = np.zeros(A.shape[0])

    start = time.time()
    if method == 'jacobi':
        x, k, error = jm.solve(A, b, x_0, tol, max_iter)
    elif method == 'gauss_seidel':
        x, k, error = gsm.solve(A, b, x_0, tol, max_iter)
    elif method == 'gradient':
        x, k, error = gm.solve(A, b, x_0, tol, max_iter)
    elif method == 'conjugate_gradient':
        x, k, error = cgm.solve(A, b, x_0, tol, max_iter)
    else:
        raise ValueError(f'Method {method} not supported')
    end = time.time()
    return x, k, end-start, error