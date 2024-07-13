import cv2
import matplotlib.pyplot as plt
import DCTsAlgorithms as dctalg
import IDCTsAlgorithms as idctalg


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
    # converto l'immagine in scala di grigi
    if len(input_image.shape) == 3:
        input_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)
    # converto l'immagine in float e la normalizzo in modo che i valori siano compresi tra -128 e 127
    input_image = input_image.astype(float) - 128
    N, M = input_image.shape

    # calcolo il numero di blocchi
    n_blocks = N // F
    
    compressed_image = input_image.copy()
    count = 0
    total_blocks = n_blocks**2
    
    for i in range(n_blocks):
        for j in range(n_blocks):
            progress = (count/total_blocks)*100
            print(f'Compression progress: {round(progress,2)}%', end='\r')
            # Estraggo il blocco di dimensione FxF
            block = input_image[i*F:(i+1)*F, j*F:(j+1)*F]
            # Applico la DCT2 al blocco
            dct_block = dctalg.DCT2(block)
            
            dct_block[:F, d:] = 0
            dct_block[d:, :F] = 0

            compressed_block = idctalg.IDCT2(dct_block)
            
            # Salvo il blocco compresso nell'immagine compressa
            compressed_image[i*F:(i+1)*F, j*F:(j+1)*F] = compressed_block
            count += 1
    
    # Normalizzo l'immagine compressa in modo che i valori siano compresi tra 0 e 255
    print('\n')
    return compressed_image