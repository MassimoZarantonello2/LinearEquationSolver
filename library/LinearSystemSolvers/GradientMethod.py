import numpy as np

def solve(A, b, x_0, tol, max_iter):
    """
    Risolve il sistema lineare Ax = b usando il metodo del gradiente.
    
    Parametri:
    A : numpy.ndarray
        Matrice quadrata simmetrica e definita positiva.
    b : numpy.ndarray
        Vettore termine noto.
    x0 : numpy.ndarray
        Vettore iniziale.
    tol : float, opzionale
        Tolleranza per il criterio di arresto (default: 1e-8).
    max_iter : int, opzionale
        Numero massimo di iterazioni (default: 1000).
    
    Ritorna:
    x : numpy.ndarray
        Vettore soluzione.
    k : int
        Numero di iterazioni eseguite.
    """
    x = x_0
    for k in range(max_iter):
        r = b - np.dot(A, x)
        y = np.dot(A, r)
        alpha = np.dot(r.T, r)
        beta = np.dot(r.T, y)

        alpha_k = alpha / beta
        x_new = x + alpha_k * r

        if np.linalg.norm(x_new - x) < tol:
            return x_new, k
        
        x = x_new

