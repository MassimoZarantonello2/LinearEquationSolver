import cv2
import DCTsAlghorithms as dctalg

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
    N, M = input_image.shape
    n_blocks = N // F
    
    compressed_image = input_image.copy()
    count = 0
    
    for i in range(n_blocks):
        for j in range(n_blocks):
            print(f'Compressing block ({count} of {n_blocks**2})')
            block = input_image[i*F:(i+1)*F, j*F:(j+1)*F]
            dct_block = dctalg.DCT2(block)
            
            dct_block[:F, d:] = 0
            dct_block[d:, :F] = 0
            
            compressed_block = dctalg.IDCT2(dct_block)
            
            compressed_image[i*F:(i+1)*F, j*F:(j+1)*F] = compressed_block
            count += 1
    
    return compressed_image