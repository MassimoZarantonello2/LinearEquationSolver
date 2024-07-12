import cv2
import os
import sys
sys.path.append('library')
import JpegFunctions.JpegCompression as jpeg
import matplotlib.pyplot as plt

images_path = 'immagini'
images_name = os.listdir("immagini")

for image_name in images_name:
    image = cv2.imread(f'{images_path}/{image_name}')
    compressed_image = jpeg.jpeg_compression(image, 8, 4)

    plt.figure(figsize=(10,10))
    plt.subplot(1, 2, 1)
    plt.imshow(image)
    plt.title('Original image')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(compressed_image)
    plt.title('Compressed image')
    plt.axis('off')

    plt.suptitle(f'{image_name} compression')
    plt.savefig(f'test/compare_images/{image_name}.png')
    plt.close()

    plt.figure(figsize=(10,10))
    plt.imshow(compressed_image)
    plt.title(f'test/compressed_images/{image_name}.png')


