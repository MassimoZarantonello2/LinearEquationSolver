import numpy as np

def gradient_method(A, b, x0, tol=1e-8, max_iter=1000):
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
    x = x0
    r = b - A @ x
    k = 0
    
    while np.linalg.norm(r) > tol and k < max_iter:
        Ar = A @ r
        alpha_k = (r.T @ r) / (r.T @ Ar)
        x = x + alpha_k * r
        r = b - A @ x
        k += 1
    
    return x, k
