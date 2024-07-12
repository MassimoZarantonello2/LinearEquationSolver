import numpy as np

def solve(A, b, x_0, tol, max_iter):
    x = x_0
    r = b - np.dot(A, x)
    d = r
    for k in range(max_iter):
        y = np.dot(A, d)
        alpha = np.dot(d, r) / np.dot(d, y)
        x_new = x + alpha * d

        if np.linalg.norm(x_new - x, np.inf) < tol:
            return x_new, k

        r_new = b - np.dot(A, x_new)
        w = np.dot(A, r_new)
        beta = np.dot(d, w) / np.dot(d, y)
        d = r_new + beta * d

        x = x_new
        r = r_new

    raise Exception("Metodo del Gradiente Coniugato non converge dopo il numero massimo di iterazioni")

# Esempio di utilizzo:
A = np.array([[4, 1], [1, 3]])
b = np.array([1, 2])
x_0 = np.array([2, 1])
tol = 1e-6
max_iter = 1000

sol, iterations = solve(A, b, x_0, tol, max_iter)
print("Soluzione:", sol)
print("Iterazioni:", iterations)
