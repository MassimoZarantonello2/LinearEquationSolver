import cv2
import os
import sys
sys.path.append('library/JpegFunctions')
import JpegCompression as jpeg
import matplotlib.pyplot as plt

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


if __name__ == '__main__':
    F = 8
    d = 2
    test_jpeg_compression(F, d)