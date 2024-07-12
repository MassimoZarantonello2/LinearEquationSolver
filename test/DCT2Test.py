import sys
sys.path.append("./library")
import JpegFunctions.DCTsAlghorithms as DCTsAlghorithms
import os
import matplotlib.pyplot as plt
import numpy as np
import time
from scipy.fftpack import dct

matrix_dimension = 50
matrix_dimensions = []
matrix_number = 5
custom_times = []
scipy_times = []

for i in range(matrix_number):
    print(f'Iteration {i + 1}/{matrix_number}')
    matrix_dimensions.append(matrix_dimension)
    matrix = np.random.rand(matrix_dimension, matrix_dimension)
    start = time.time()
    DCTsAlghorithms.DCT2(matrix)
    end = time.time()
    custom_times.append(end - start)

    start = time.time()
    dct(dct(matrix, axis=0, norm='ortho'), axis=1, norm='ortho')
    end = time.time()
    scipy_times.append(end - start)

    matrix_dimension += 50

# Plot the graph using matplotlib and the y must be logarithmic
plt.plot(matrix_dimensions, custom_times, label='Custom DCT2')
plt.plot(matrix_dimensions, scipy_times, label='Scipy DCT2')
plt.yscale('log')
plt.xlabel('Matrix dimension')
plt.ylabel('Time (s)')
plt.title('DCT2 time comparison')
plt.legend()
plt.savefig('plots/DCT2_time_comparison.png')
