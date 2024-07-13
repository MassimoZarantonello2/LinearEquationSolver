import tracemalloc
from scipy.io import mmread
import numpy as np
import os
import sys
sys.path.append('library')
import LinearSystemSolvers.LinearSystemSolver as lss
import matplotlib.pyplot as plt

def plot_graph(times, iterations, memory, errors, matrix_name, idxs):
    matrix_name = matrix_name.replace('.mtx', '')
    for idx in idxs:
        idx = idx.replace(matrix_name, '')
    plt.figure(figsize=(10,10))
    plt.subplot(2, 2, 1)
    for idx in idxs:
        plt.plot(plot_tollerances, times[idx], label=idx)
    plt.xlabel('Tollerance')
    plt.ylabel('Time')
    plt.yscale('log')
    plt.legend()

    plt.subplot(2, 2, 2)
    for idx in idxs:
        plt.plot(plot_tollerances, iterations[idx], label=idx)
    plt.xlabel('Tollerance')
    plt.ylabel('Iterations')
    plt.yscale('log')
    plt.legend()

    plt.subplot(2, 2, 3)
    for idx in idxs:
        plt.plot(plot_tollerances, memory[idx], label=idx)
    plt.xlabel('Tollerance')
    plt.ylabel('Memory')
    plt.yscale('log')
    plt.legend()

    plt.suptitle(f'{matrix_name} results')
    plt.savefig(f'test/plots/{matrix_name}.png')
    plt.close()


matrices_path = os.listdir("matrici")
matrices = []
for m in matrices_path:
    matrices.append(mmread("matrici/"+m).toarray())

methods = ["jacobi", "gauss_seidel", "gradient", "conjugate_gradient"]
plot_tollerances = ['1e-10', '1e-8', '1e-6', '1e-4']

tollerances = [1e-10, 1e-8, 1e-6, 1e-4]
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
        index = index.replace('.mtx', '')
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
    idxs = []

    plot_graph(method_times, method_iterations, method_memory ,method_errors, matrices_path[j], idxs)
    j += 1