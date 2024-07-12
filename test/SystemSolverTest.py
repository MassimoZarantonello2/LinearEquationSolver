import tracemalloc
from scipy.io import mmread
import numpy as np
import os
import sys
sys.path.append('library')
import LinearSystemSolvers.LinearSystemSolver as lss
import matplotlib.pyplot as plt

matrices_path = os.listdir("matrici")
matrices = []
for m in matrices_path:
    matrices.append(mmread("matrici/"+m).toarray())

methods = ["jacobi", "gauss_seidel", "gradient", "conjugate_gradient"]
plot_tollerances = ['1e-4', '1e-5', '1e-6', '1e-7', '1e-8', '1e-9', '1e-10']

tollerances = [1e-4, 1e-5, 1e-6, 1e-7, 1e-8, 1e-9, 1e-10]
max_iterations = 20000

matrices = [matrices[0]]

j = 0
for A in matrices:
    b = np.ones(A.shape[0])
    method_times = {}
    method_iterations = {}
    method_memory = {}
    
    for method in methods:
        times = []
        iterations = []
        memory_usage = []
        
        for tollerance in tollerances:
            print(f'Running {method} on matrix {A.shape[0]}x{A.shape[1]} with tollerance {tollerance}')
            
            tracemalloc.start()
            
            x, k, time = lss.solve(A, b, tollerance, max_iterations, method=method)
            
            current, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()
            
            times.append(time)
            iterations.append(k)
            memory_usage.append(peak)
        
        method_times[method] = times
        method_iterations[method] = iterations
        method_memory[method] = memory_usage
    
    with open(f'test/results_times.txt', 'a+') as f:
        for method in methods:
            f.write(f'{matrices_path[j]}_{method}_{method_times[method]}\n')

    with open(f'test/results_iterations.txt', 'a+') as f:
        for method in methods:
            f.write(f'{matrices_path[j]}_{method}_{method_iterations[method]}\n')

    with open(f'test/results_memory.txt', 'a+') as f:
        for method in methods:
            f.write(f'{matrices_path[j]}_{method}_{method_memory[method]}\n')