import numpy as np

def DCT(x):
    """
    Calcola la trasformata discreta del coseno (DCT) di un vettore x.
    
    Parameters:
    x (numpy array): Vettore di input di lunghezza N.
    
    Returns:
    numpy array: Vettore contenente la DCT di x.
    """
    N = len(x)
    X = np.zeros(N)
    for k in range(N):
        sum_value = 0
        for n in range(N):
            sum_value += x[n] * np.cos(np.pi * k * (2*n + 1) / (2 * N))
        if k == 0:
            alpha_k = np.sqrt(1/N)
        else:
            alpha_k = np.sqrt(2/N)
        X[k] = alpha_k * sum_value
    return X

def DCT2(x):
    """
    Calcola la trasformata discreta del coseno bidimensionale (DCT2) di una matrice x.
    
    Parameters:
    x (numpy array): Matrice di input di dimensioni (N, M).
    
    Returns:
    numpy array: Matrice contenente la DCT2 di x.
    """
    N, M = x.shape
    X = np.zeros((N, M))
    
    # Applicare la DCT a ogni riga della matrice
    for i in range(N):
        X[i, :] = DCT(x[i, :])
    
    # Applicare la DCT a ogni colonna della matrice risultante
    for j in range(M):
        X[:, j] = DCT(X[:, j])
    
    return X