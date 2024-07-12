from scipy.io import mmread
import numpy as np
import os
import sys
sys.path.append('library')
import library.LinearSystemSolver as lss
import matplotlib.pyplot as plt

matrices_path = os.listdir("matrici")
matrices = []
for m in matrices_path:
    matrices.append(mmread("matrici/"+m).toarray())

methods = ["jacobi", "gauss_seidel","gradient" ,"conjugate_gradient"]
plot_tollerances = ['1e-4','ie-5','1e-6','1e-7','1e-8','1e-9','1e-10']

tollerances = [1e-4, 1e-5, 1e-6, 1e-7, 1e-8, 1e-9, 1e-10]
max_iterations = 20000

matrices = [matrices[0]]

j = 0
for A in matrices:
    b = np.ones(A.shape[0])
    method_times = {}
    method_iterations = {}
    for method in methods:
        times = []
        iterations = []
        for tollerance in tollerances:
            print(f'Running {method} on matrix {A.shape[0]}x{A.shape[1]} with tollerance {tollerance}')
            x, k, time = lss.solve(A, b, tollerance, max_iterations, method=method)
            # I tempi di esecuzione di un metodo di una tolleranza
            times.append(time)
            iterations.append(k)

        method_times[method] = times                # jacobi: [time1, time2, time3, time4]
        method_iterations[method] = iterations      # jacobi: [iter1, iter2, iter3, iter4]

    with open(f'results_times.txt', 'a+') as f:
        for method in methods:
            f.write(f'{matrices_path[j]}_{method}_{method_times[method]}\n')

    with open(f'results_iterations.txt', 'a+') as f:
        for method in methods:
            f.write(f'{matrices_path[j]}_{method}_{method_iterations[method]}\n')

    # # Plotting
    # for method in methods:
    #     plt.plot(plot_tollerances, method_times[method], label=method)
    # plt.xlabel('Tollerance')
    # plt.ylabel('Time')
    # plt.title(f'Matrix {matrices_path[j]}')
    # plt.legend()
    # plt.savefig(f'plots/{matrices_path[j]}_time.png')
    # plt.clf()

    # for method in methods:
    #     plt.plot(plot_tollerances, method_iterations[method], label=method)
    # plt.xlabel('Tollerance')
    # plt.ylabel('Iterations')
    # plt.title(f'Matrix {matrices_path[j]}')
    # plt.legend()
    # plt.savefig(f'plots/{matrices_path[j]}_iterations.png')
    # plt.clf()

    # j += 1