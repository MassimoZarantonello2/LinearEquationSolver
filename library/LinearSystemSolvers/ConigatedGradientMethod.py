import numpy as np

def solve(A, b, x_0, tol, max_iter):
    '''
    Risolve il sistema lineare Ax = b usando il metodo del gradiente coniugato.
    '''
    x = x_0
    r = b - np.dot(A, x)
    d = r
    for k in range(max_iter):
        y = np.dot(A, d)
        alpha = np.dot(d, r) / np.dot(d, y)
        x_new = x + alpha * d

        tollerance = np.linalg.norm(r) / np.linalg.norm(b)
        if tollerance < tol:
            return x_new, k, tollerance
        
        r_new = b - np.dot(A, x_new)
        w = np.dot(A, r_new)
        beta = np.dot(d, w) / np.dot(d, y)
        d = r_new - beta * d

        x = x_new
        r = r_new

    raise Exception("Metodo del Gradiente Coniugato non converge dopo il numero massimo di iterazioni")
