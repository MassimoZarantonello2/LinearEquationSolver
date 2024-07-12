import sys
sys.path.append("library/JpegFunctions")
import JpegFunctions.JpegCompression as jpeg
import os
import cv2
import matplotlib.pyplot as plt

image_path = "immagini/"
image_names = os.listdir(image_path)
images_path = [image_path + image_name for image_name in image_names]
images = [cv2.imread(image_path) for image_path in images_path]
i = 0
for image in images:
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    compressed_image = jpeg.jpeg_compression(gray_image, 8, 4)

    plt.figure()
    plt.subplot(1, 2, 1)
    plt.imshow(gray_image, cmap='gray')
    plt.title('Original Image')
    plt.axis('off')
    plt.subplot(1, 2, 2)
    plt.imshow(compressed_image, cmap='gray')
    plt.title('Compressed Image')
    plt.axis('off')

    plt.savefig(f'compressed_images/{image_names[i]}_compressed.png')