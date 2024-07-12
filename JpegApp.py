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
        global img, img_display, gray_image, compressed_image
        img = cv2.imread(file_path)
        gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img_display = ImageTk.PhotoImage(Image.fromarray(gray_image).resize((640, 640)))
        original_panel.config(image=img_display)
        original_panel.image = img_display
        compressed_image = None

# Funzione per eseguire la compressione e visualizzare l'immagine compressa
def compress_image():
    global gray_image, img_display, compressed_image
    if gray_image is not None:
        try:
            F = int(F_entry.get())
            d = int(d_entry.get())
            compressed_image = jc.jpeg_compression(gray_image, F, d)
            img_display = ImageTk.PhotoImage(Image.fromarray(compressed_image).resize((640, 640)))
            compressed_panel.config(image=img_display)
            compressed_panel.image = img_display
        except ValueError:
            messagebox.showerror("Errore", "F e d devono essere numeri interi")
    else:
        messagebox.showerror("Errore", "Nessuna immagine caricata")

# Funzione per salvare l'immagine compressa
def save_image():
    global compressed_image
    if compressed_image is not None:
        file_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[
            ("JPEG files", "*.jpg;*.jpeg"),
            ("PNG files", "*.png"),
            ("BMP files", "*.bmp"),
            ("TIFF files", "*.tiff"),
            ("All files", "*.*")
        ])
        if file_path:
            Image.fromarray(compressed_image).save(file_path)
            messagebox.showinfo("Salvataggio", "Immagine compressa salvata con successo")
    else:
        messagebox.showerror("Errore", "Nessuna immagine compressa da salvare")

# Creazione dell'interfaccia grafica con Tkinter
root = tk.Tk()
root.title("Compressore JPEG")

# Frame per visualizzare le immagini affiancate
image_frame = tk.Frame(root)
image_frame.pack()

# Pannello per visualizzare l'immagine originale
original_panel = tk.Label(image_frame, text="Immagine originale")
original_panel.grid(row=0, column=0, padx=10, pady=10)

# Pannello per visualizzare l'immagine compressa
compressed_panel = tk.Label(image_frame, text="Immagine compressa")
compressed_panel.grid(row=0, column=1, padx=10, pady=10)

# Frame per input F e d
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

tk.Label(input_frame, text="F:").grid(row=0, column=0)
F_entry = tk.Entry(input_frame)
F_entry.grid(row=0, column=1)

tk.Label(input_frame, text="d:").grid(row=1, column=0)
d_entry = tk.Entry(input_frame)
d_entry.grid(row=1, column=1)

# Frame per i pulsanti
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# Pulsante per caricare l'immagine
btn_load = tk.Button(button_frame, text="Carica Immagine", command=load_image)
btn_load.grid(row=0, column=0, padx=10)

# Pulsante per comprimere l'immagine
btn_compress = tk.Button(button_frame, text="Comprimi Immagine", command=compress_image)
btn_compress.grid(row=0, column=1, padx=10)

# Pulsante per salvare l'immagine compressa
btn_save = tk.Button(button_frame, text="Salva Immagine", command=save_image)
btn_save.grid(row=0, column=2, padx=10)

# Variabili globali
img = None
gray_image = None
compressed_image = None
img_display = None

# Avvia l'interfaccia grafica
root.mainloop()
