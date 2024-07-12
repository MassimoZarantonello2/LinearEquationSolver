import cv2
import matplotlib.pyplot as plt
import DCTsAlghorithms as dctalg
import os

def jpeg_compression(input_image, F, d):
    """
    Comprime un'immagine utilizzando la trasformata discreta del coseno (DCT).
    
    Parameters:
    'input_image' (numpy array): Immagine di input.
    'F' (int): Dimensione del blocco.
    'd' (int): Numero di coefficienti da mantenere.
    
    Returns:
    'compressed_image': Immagine compressa.
    """
    # converto l'immagine in float e la normalizzo in modo che i valori siano compresi tra -128 e 127
    input_image = input_image.astype(float) - 128
    N, M = input_image.shape

    # calcolo il numero di blocchi
    n_blocks = N // F
    
    compressed_image = input_image.copy()
    count = 0
    
    for i in range(n_blocks):
        for j in range(n_blocks):
            # Estraggo il blocco di dimensione FxF
            block = input_image[i*F:(i+1)*F, j*F:(j+1)*F]
            # Applico la DCT2 al blocco
            dct_block = dctalg.DCT2(block)
            
            dct_block[:F, d:] = 0
            dct_block[d:, :F] = 0
            
            # Applico la IDCT2 al blocco
            compressed_block = dctalg.IDCT2(dct_block)
            
            # Salvo il blocco compresso nell'immagine compressa
            compressed_image[i*F:(i+1)*F, j*F:(j+1)*F] = compressed_block
            count += 1
    
    return compressed_image

if __name__ == '__main__':
    image_path = "immagini/"
    image_names = os.listdir(image_path)
    images_path = [image_path + image_name for image_name in image_names]
    images = [cv2.imread(image_path) for image_path in images_path]

    for i, image in enumerate(images):
        print(f"Compressing image {image_names[i]}")
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        compressed_image = jpeg_compression(gray_image, 8, 4)

        plt.figure()
        plt.imsave(f'compressed_images/{image_names[i]}_compressed.png', compressed_image, cmap='gray')
