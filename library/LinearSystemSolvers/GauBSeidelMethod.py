import numpy as np

def forward_substitution(L, b):
    n = L.shape[0]
    y = np.zeros(n)
    
    for i in range(n):
        y[i] = (b[i] - np.dot(L[i, :i], y[:i])) / L[i, i]
    
    return y

def solve(A, b, x_0, tol, max_iterations):
    '''
    Risolve il sistema lineare Ax = b usando il metodo di Gauss-Seidel.

    Parametri:
    'A' : numpy.ndarray
        Matrice quadrata.
    'b' : numpy.ndarray
        Vettore termine noto.
    'x_0' : numpy.ndarray, opzionale
        Vettore iniziale (default: vettore nullo).
    'tol' : float   
        Tolleranza per il criterio di arresto.
    'max_iterations' : int  
        Numero massimo di iterazioni.

    Ritorna:
    'x' : numpy.ndarray
        Vettore soluzione.   
    '''
    n = A.shape[0]
    x = x_0

    for k in range(max_iterations):
        r = b - np.dot(A, x)
        y = forward_substitution(np.tril(A), r)
        x_new = x + y
        tollerance = np.linalg.norm(r) / np.linalg.norm(b)
        if tollerance < tol:
            return x_new, k, tollerance
        
        x = x_new
    
    raise Exception("Metodo di Gauss-Seidel non converge dopo il numero massimo di iterazioni")
