import numpy as np

class ConjugateGradientSolver:
    def __init__(self, A, b, x0=None, tol=1e-10, max_iter=None):
        self.A = A
        self.b = b
        self.n = len(b)
        self.x = x0 if x0 is not None else np.zeros(self.n)
        self.tol = tol
        self.max_iter = max_iter if max_iter is not None else self.n

    def solve(self):
        A, b, x = self.A, self.b, self.x
        r = b - A @ x
        d = r.copy()
        iterations = 0
        residual_norm = np.linalg.norm(r)
        
        while residual_norm > self.tol and iterations < self.max_iter:
            Ad = A @ d
            alpha = r @ r / (d @ Ad)
            x = x + alpha * d
            r_new = r - alpha * Ad
            
            if np.linalg.norm(r_new) < self.tol:
                break
            
            beta = (r_new @ r_new) / (r @ r)
            d = r_new + beta * d
            r = r_new
            residual_norm = np.linalg.norm(r)
            iterations += 1

        return x, iterations, residual_norm

