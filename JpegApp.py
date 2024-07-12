import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import cv2
import sys
sys.path.append("library/JpegFunctions")
import library.JpegFunctions.JpegCompression as jc


# Funzione per caricare l'immagine
def load_image():
    file_path = filedialog.askopenfilename(filetypes=[
        ("BMP files", "*.bmp"),
        ("JPEG files", "*.jpg;*.jpeg"),
        ("PNG files", "*.png"),
        ("TIFF files", "*.tiff"),
        ("All files", "*.*")
    ])
    if file_path:
        global img, img_display, gray_image
        img = cv2.imread(file_path)
        gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img_display = ImageTk.PhotoImage(Image.fromarray(gray_image))
        original_panel.config(image=img_display)
        original_panel.image = img_display

# Funzione per eseguire la compressione e visualizzare l'immagine compressa
def compress_image():
    global gray_image, img_display
    if gray_image is not None:
        try:
            F = int(F_entry.get())
            d = int(d_entry.get())
            compressed_image = jc.jpeg_compression(gray_image, F, d)
            img_display = ImageTk.PhotoImage(Image.fromarray(compressed_image))
            compressed_panel.config(image=img_display, width=img_display.width(), height=img_display.height())
            compressed_panel.image = img_display
        except ValueError:
            messagebox.showerror("Errore", "F e d devono essere numeri interi")
    else:
        messagebox.showerror("Errore", "Nessuna immagine caricata")

# Creazione dell'interfaccia grafica con Tkinter
root = tk.Tk()
root.title("Compressore JPEG")

# Pannello per visualizzare l'immagine
original_panel = tk.Label(root, text="Immagine originale")
original_panel.pack()

compressed_panel = tk.Label(root, text="Immagine compressa")
compressed_panel.pack()

# Frame per input F e d
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

tk.Label(input_frame, text="F:").grid(row=0, column=0)
F_entry = tk.Entry(input_frame)
F_entry.grid(row=0, column=1)

tk.Label(input_frame, text="d:").grid(row=1, column=0)
d_entry = tk.Entry(input_frame)
d_entry.grid(row=1, column=1)

# Pulsante per caricare l'immagine
btn_load = tk.Button(root, text="Carica Immagine", command=load_image)
btn_load.pack(side="left", padx=10, pady=10)

# Pulsante per comprimere l'immagine
btn_compress = tk.Button(root, text="Comprimi Immagine", command=compress_image)
btn_compress.pack(side="right", padx=10, pady=10)

# Variabili globali
img = None
gray_image = None
img_display = None

# Avvia l'interfaccia grafica
root.mainloop()