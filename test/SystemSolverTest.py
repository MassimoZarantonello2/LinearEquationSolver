import tracemalloc
from scipy.io import mmread
import numpy as np
import os
import sys
sys.path.append('library')
import LinearSystemSolvers.LinearSystemSolver as lss
import matplotlib.pyplot as plt

def write_results(filename, data):
    with open(f'test/{filename}', 'a+') as f:
        f.write(f'{data}\n')

def plot_results(x, y, title, xlabel, ylabel, filename):


matrices_path = os.listdir("matrici")
matrices = []
for m in matrices_path:
    matrices.append(mmread("matrici/"+m).toarray())

methods = ["jacobi", "gauss_seidel", "gradient", "conjugate_gradient"]
plot_tollerances = ['1e-4', '1e-6', '1e-8', '1e-10']

tollerances = [1e-4, 1e-6, 1e-8, 1e-10]
max_iterations = 30000

j = 0
for A in matrices:
    b = np.ones(A.shape[0])
    method_times = {}
    method_iterations = {}
    method_memory = {}
    method_errors = {}
    
    for method in methods:
        index = f'{matrices_path[j]}_{method}'       
        times = []
        iterations = []
        memory_usage = []
        errors = []
        
        for tollerance in tollerances:
            print(f'Running {method} on matrix {A.shape[0]}x{A.shape[1]} with tollerance {tollerance}')
            
            tracemalloc.start()
            
            x, k, time, tollerance = lss.solve(A, b, tollerance, max_iterations, method=method)
            
            current, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()
            
            times.append(time)
            iterations.append(k)
            memory_usage.append(peak)
            errors.append(tollerance)
        
        method_times[index] = times
        method_iterations[index] = iterations
        method_memory[index] = memory_usage
        method_errors[index] = tollerances
    
    for method in methods:
        index = f'{matrices_path[j]}_{method}'
        write_results("plots/times.txt", f'{index} {method_times[index]}')
        write_results("plots/iterations.txt", f'{index} {method_iterations[index]}')
        write_results("plots/memory.txt", f'{index} {method_memory[index]}')
        write_results("plots/errors.txt", f'{index} {method_errors[index]}')

    j += 1