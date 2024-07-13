# Progetto di Calcolo Scientifico

## Descrizione del Progetto

Il progetto di calcolo scientifico è suddiviso in due parti principali:

1. **Risoluzione di Sistemi Lineari**
2. **Compressione di Immagini con Algoritmo JPEG**

## Struttura del Progetto

### Risoluzione di Sistemi Lineari

Questa parte del progetto comprende tutti i file all'interno della cartella `library/LinearSystemSolvers`. Ogni file contiene script dedicati per eseguire vari metodi di risoluzione dei sistemi lineari richiesti.

### Compressione di Immagini con Algoritmo JPEG

Questa sezione comprende i file all'interno della cartella `library/JpegFunctions`. Contiene gli script relativi alla compressione delle immagini tramite l'algoritmo JPEG, che sfrutta le funzioni DCT2 e IDCT2. Questi algoritmi sono implementati in script presenti all'interno della stessa cartella.

## Cartella Test

La cartella `test` contiene tre script principali per testare le funzionalità implementate:

1. **SystemSolverTest.py**
   - Comprende i test per i risolutori di sistemi lineari.
   - Include funzionalità per plottare grafici relativi ai tempi di esecuzione, alle iterazioni e alla memoria occupata.

2. **DCT2Test.py**
   - Contiene i test per le funzioni DCT, DCT2, IDCT e IDCT2.
   - Applica queste funzioni a una matrice apposita fornita per verificare la correttezza dell'esecuzione.

3. **JpegTest.py**
   - Comprende i test per la compressione tramite l'algoritmo JPEG.
   - Genera immagini compresse e le confronta con quelle originali.
   - Crea grafici relativi ai tempi di esecuzione al variare dei parametri in input e mostra immagini compresse con varie combinazioni di essi.

## Interfaccia Utente

Nella cartella principale è presente un file chiamato `JpegApp.py`. Questo script crea un'interfaccia utente per caricare immagini ed eseguire la compressione, permettendo di selezionare i parametri desiderati. È anche possibile salvare il risultato della compressione.

## Come Iniziare

1. Clona il repository:
   ```bash
   git clone git@github.com:MassimoZarantonello2/ProgettoCalcoloScientifico.git
   cd ProgettoCalcoloScientifico
   ```

Per ulteriori informazioni, fare riferimento alla documentazione.
