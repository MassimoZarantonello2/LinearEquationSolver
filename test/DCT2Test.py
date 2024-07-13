import os
import sys
sys.path.append("./library")
import JpegFunctions.DCTsAlgorithms as DCTsAlgorithms
import JpegFunctions.IDCTsAlgorithms as IDCTsAlgorithms
import matplotlib.pyplot as plt
import numpy as np
import time
from scipy.fftpack import dct

def plot_dct2_time_comparison():
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
        DCTsAlgorithms.DCT2(matrix)
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
    print(IDCTsAlgorithms.IDCT(DCTsAlgorithms.DCT(first_row)))
    print("\nDCT2 della matrice:")
    print(IDCTsAlgorithms.IDCT2(DCTsAlgorithms.DCT2(matrix)))

    if os.path.exists('plots/DCT2_time_comparison.png') == False:
        plot_dct2_time_comparison()
