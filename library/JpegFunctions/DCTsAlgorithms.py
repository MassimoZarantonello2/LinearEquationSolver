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
    cosine_matrix = np.cos(np.pi * np.outer(np.arange(N), (np.arange(N) * 2 + 1) / (2 * N)))
    alpha = np.sqrt(2 / N) * np.ones(N)
    alpha[0] = np.sqrt(1 / N)
    
    X = alpha * np.dot(cosine_matrix, x)
    
    return X

def IDCT(X):
    """
    Calcola l'inversa della trasformata discreta del coseno (IDCT) di un vettore X.
    
    Parameters:
    X (numpy array): Vettore di input di lunghezza N.
    
    Returns:
    numpy array: Vettore contenente l'IDCT di X.
    """
    N = len(X)
    cosine_matrix = np.cos(np.pi * np.outer(np.arange(N), (np.arange(N) * 2 + 1) / (2 * N)))
    alpha = np.sqrt(2 / N) * np.ones(N)
    alpha[0] = np.sqrt(1 / N)
    
    x = np.dot(cosine_matrix.T, alpha * X)
    
    return x

def DCT2(x):
    """
    Calcola la trasformata discreta del coseno bidimensionale (DCT2) di una matrice x.
    
    Parameters:
    x (numpy array): Matrice di input di dimensioni (N, M).
    
    Returns:
    numpy array: Matrice contenente la DCT2 di x.
    """
    N, M = x.shape
    X = np.apply_along_axis(DCT, 1, x)
    X = np.apply_along_axis(DCT, 0, X)
    
    return X

def IDCT2(X):
    """
    Calcola l'inversa della trasformata discreta del coseno bidimensionale (IDCT2) di una matrice X.
    
    Parameters:
    X (numpy array): Matrice di input di dimensioni (N, M).
    
    Returns:
    numpy array: Matrice contenente l'IDCT2 di X.
    """
    N, M = X.shape
    x = np.apply_along_axis(IDCT, 1, X)
    x = np.apply_along_axis(IDCT, 0, x)
    
    return x
