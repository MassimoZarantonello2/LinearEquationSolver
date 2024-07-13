import cv2
import os
import sys
sys.path.append('library/JpegFunctions')
import JpegCompression as jpeg
import matplotlib.pyplot as plt
import time

def test_jpeg_compression(F, d):
    images_path = 'immagini'
    images_name = os.listdir("immagini")

    for image_name in images_name:
        print_name = image_name.replace('.bmp', '')
        print(f'Compressing image {print_name}')
        image = cv2.imread(f'{images_path}/{image_name}')
        compressed_image = jpeg.jpeg_compression(image, F, d)

        plt.figure(figsize=(10,10))
        plt.subplot(1, 2, 1)
        plt.imshow(image, cmap='gray')
        plt.title('Original image')
        plt.axis('off')

        plt.subplot(1, 2, 2)
        plt.imshow(compressed_image, cmap='gray')
        plt.title('Compressed image')
        plt.axis('off')

        plt.suptitle(f'{print_name} compression')
        plt.savefig(f'test/compare_images/{print_name}.png')
        plt.close()

        plt.figure(figsize=(10,10))
        plt.imshow(compressed_image, cmap='gray')
        plt.title(f'{print_name}.png')
        plt.axis('off')
        plt.savefig(f'test/compressed_images/{print_name}.png')

def time_jpeg_F_values(Fs):
    d = 2
    small_image = cv2.imread('immagini/shoe.bmp')
    large_image = cv2.imread('immagini/deer.bmp')
    start = time.time()
    small_times = []
    large_times = []

    plt.figure(figsize=(10,10))
    for F in Fs:
        print(f'Compressing image with F={F} and d={d}')
        small_start = time.time()
        small_compressed_image = jpeg.jpeg_compression(small_image, F, d)
        small_time = time.time() - small_start
        small_times.append(small_time)
        large_start = time.time()
        large_compressed_image = jpeg.jpeg_compression(large_image, F, d)
        large_time = time.time() - large_start
        large_times.append(large_time)

    plt.plot(Fs, small_times, linestyle='dashed', label='small image')
    plt.plot(Fs, large_times, linestyle='dashed', label='large image')
    plt.xlabel('F')
    plt.ylabel('Time')
    plt.legend()
    plt.savefig('test/compression_time_plot.png')


def test_jpeg_compression(ds):
    image = cv2.imread('immagini/deer.bmp')
    F = 8
    plt.figure(figsize=(10,10))
    for i in range(4):
        plt.subplot(2, 2, i+1)
        compressed_image = jpeg.jpeg_compression(image, F, ds[i])
        plt.imshow(compressed_image, cmap='gray')
        plt.title(f'd={ds[i]}')
        plt.axis('off')
    plt.suptitle('Compression with different d values')
    plt.savefig('test/compression_d_values.png')
if __name__ == '__main__':
    Fs = [2, 4, 8, 16]
    ds = [1, 2, 3, 5]
    #time_jpeg_F_values(Fs)
    test_jpeg_compression(ds)