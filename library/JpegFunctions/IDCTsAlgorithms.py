import numpy as np

def IDCT(X):
    """
    Calcola l'inversa della trasformata discreta del coseno (IDCT) di un vettore X.
    
    Parameters:
    X (numpy array): Vettore di input di lunghezza N.
    
    Returns:
    numpy array: Vettore contenente l'IDCT di X.
    """
    N = len(X)
    x = np.zeros(N)
    for n in range(N):
        sum_value = 0
        for k in range(N):
            if k == 0:
                alpha_k = np.sqrt(1/N)
            else:
                alpha_k = np.sqrt(2/N)
            sum_value += alpha_k * X[k] * np.cos(np.pi * k * (2*n + 1) / (2 * N))
        x[n] = sum_value
    return x

def IDCT2(X):
    """
    Calcola l'inversa della trasformata discreta del coseno bidimensionale (IDCT2) di una matrice X.
    
    Parameters:
    X (numpy array): Matrice di input di dimensioni (N, M).
    
    Returns:
    numpy array: Matrice contenente l'IDCT2 di X.
    """
    N, M = X.shape
    x = np.zeros((N, M))
    
    # Applicare l'IDCT a ogni riga della matrice
    for i in range(N):
        x[i, :] = IDCT(X[i, :])
    
    # Applicare l'IDCT a ogni colonna della matrice risultante
    for j in range(M):
        x[:, j] = IDCT(x[:, j])
    
    return x