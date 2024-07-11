import numpy as np

def gauss_seidel_method(A, b, x0=None, tol=1e-10, max_iterations=1000):
    n = A.shape[0]
    
    if x0 is None:
        x = np.zeros(n)
    else:
        x = x0

    for k in range(max_iterations):
        x_old = np.copy(x)
        
        for i in range(n):
            sum1 = sum(A[i, j] * x[j] for j in range(i))
            sum2 = sum(A[i, j] * x_old[j] for j in range(i + 1, n))
            x[i] = (b[i] - sum1 - sum2) / A[i, i]
        
        if np.linalg.norm(x - x_old, np.inf) < tol:
            return x, k
    
    raise Exception("Metodo di Gauss-Seidel non converge dopo il numero massimo di iterazioni")
