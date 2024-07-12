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

if __name__ == "__main__":
    matrix = [
    [231, 32, 233, 161, 24, 71, 140, 245],
    [247, 40, 248, 245, 124, 204, 36, 107],
    [234, 202, 245, 167, 9, 217, 239, 173],
    [193, 190, 100, 167, 43, 180, 8, 70],
    [11, 24, 210, 177, 81, 243, 8, 112],
    [97, 195, 203, 47, 125, 114, 165, 181],
    [193, 70, 174, 167, 41, 30, 127, 245],
    [87, 149, 57, 192, 65, 129, 178, 228]
    ]

    matrix = np.array(matrix)
    first_row = matrix[0]
    print("DCT Vettore di input:")
    print(IDCT(DCT(first_row)))
    print("\nDCT2 della matrice:")
    print(IDCT2(DCT2(matrix)))