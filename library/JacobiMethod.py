import numpy as np

def jacobi_method(input_matrix, b, x0=None, tol=1e-10, max_iterations=1000):
    '''
    Utilizza il metodo di Jacobi per risolvere il sistema lineare Ax = b.\n
    -----
    ### Parametri:
    - `input_matrix`: matrice dei coefficienti
    - `b`: vettore dei termini noti
    - `x0`: vettore iniziale (opzionale)
    - `tol`: tolleranza per il criterio di arresto (opzionale) di default 1e-10
    - `max_iterations`: numero massimo di iterazioni (opzionale) di default 1000
    '''
    n = input_matrix.shape[0]
    if x0 is None:
        x = np.zeros(n)
    else:
        x = x0

    P_inv = np.diag(1 / np.diag(input_matrix))
    A = input_matrix

    print(A)
    
    for k in range(max_iterations):
        r = b - np.dot(input_matrix, x)
        x_new = x + np.dot(P_inv, r)
        
        if np.linalg.norm(x_new - x, np.inf) < tol:
            return x_new, k
        
        x = x_new
    
    raise Exception("Metodo di Jacobi non converge dopo il numero massimo di iterazioni")
