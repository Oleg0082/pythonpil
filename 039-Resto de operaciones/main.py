import tkinter as tk
from tkinter import Tk, filedialog
from PIL import Image, ImageTk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from JVImagen import *

entrada = ""
salida = ""
brillo = 0
contraste = 1.0
original_image = None
preview_image = None

# Function to open an image and display it in the preview pane
def abrirImagen():
    global entrada, original_image, preview_image
    entrada = filedialog.askopenfilename(
        title="Selecciona imagen de origen",
        filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")]
    )
    if entrada:
        original_image = Image.open(entrada)
        preview_image = original_image.copy()
        actualizarVista()

# Function to save the processed image
def guardarImagen():
    global salida
    salida = filedialog.asksaveasfilename(
        title="Selecciona imagen de destino",
        defaultextension=".jpg",
        filetypes=[("JPEG files", "*.jpg"), ("PNG files", "*.png"), ("BMP files", "*.bmp"), ("GIF files", "*.gif")]
    )

# Function to update the preview pane
def actualizarVista():
    global preview_image
    if preview_image:
        img_resized = preview_image.resize((300, 300))
        img_tk = ImageTk.PhotoImage(img_resized)
        preview_label.config(image=img_tk)
        preview_label.image = img_tk

# Function to re-scale the image
def reescalar():
    global entrada, preview_image
    nuevaanchura = int(entry_anchura.get())
    nuevaaltura = int(entry_altura.get())
    if entrada:
        imagen = JVImagen(entrada, salida)
        imagen.reescalar(nuevaanchura, nuevaaltura)
        preview_image = imagen.imagen.copy()
        actualizarVista()

# Function to crop the image
def recortar():
    global entrada, preview_image
    x1, y1, x2, y2 = map(int, (entry_x1.get(), entry_y1.get(), entry_x2.get(), entry_y2.get()))
    if entrada:
        imagen = JVImagen(entrada, salida)
        imagen.recortar(x1, y1, x2, y2)
        preview_image = imagen.imagen.copy()
        actualizarVista()

# Function to crop the image at the center
def recortarCentro():
    global entrada, preview_image
    cx, cy, anchura, altura = map(int, (entry_cx.get(), entry_cy.get(), entry_anchura_centro.get(), entry_altura_centro.get()))
    if entrada:
        imagen = JVImagen(entrada, salida)
        imagen.recortarCentro(cx, cy, anchura, altura)
        preview_image = imagen.imagen.copy()
        actualizarVista()

# Function to change brightness
def cambiaBrillo(value):
    global brillo
    brillo = int(value)
    aplicarCambios()

# Function to change contrast
def cambiaContraste(value):
    global contraste
    contraste = float(value)
    aplicarCambios()

# Function to apply changes to preview image
def aplicarCambios():
    global original_image, preview_image, brillo, contraste
    if original_image:
        imagen_temp = JVImagen(entrada, salida)
        imagen_temp.brillo(brillo)
        imagen_temp.contraste(contraste)
        preview_image = imagen_temp.imagen.copy()
        actualizarVista()

# Function to apply processing
def procesaImagen():
    global entrada, salida
    if entrada and salida:
        imagen = JVImagen(entrada, salida)
        imagen.negativo()
        imagen.guarda()
        retroalimentacion.config(text="Imagen guardada correctamente")
    else:
        retroalimentacion.config(text="Selecciona entrada y salida")

ventana = ttk.Window(themename="cosmo")
ventana.geometry("1000x600")
ventana.title("JVShop")

# Controls frame on the left
controls_frame = tk.Frame(ventana)
controls_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nw")

# Preview frame on the right
preview_frame = tk.Frame(ventana)
preview_frame.grid(row=0, column=1, padx=20, pady=20, sticky="ne")

# Buttons and controls
btn_abrir = tk.Button(controls_frame, text="Selecciona la imagen de entrada", command=abrirImagen)
btn_abrir.grid(row=0, column=0, pady=10)

btn_guardar = tk.Button(controls_frame, text="Selecciona la imagen de salida", command=guardarImagen)
btn_guardar.grid(row=1, column=0, pady=10)

# Rescale controls
tk.Label(controls_frame, text="Reescalar").grid(row=2, column=0, sticky="w")
tk.Label(controls_frame, text="Ancho:").grid(row=3, column=0, sticky="w")
entry_anchura = tk.Entry(controls_frame)
entry_anchura.grid(row=3, column=1, sticky="w")
tk.Label(controls_frame, text="Alto:").grid(row=4, column=0, sticky="w")
entry_altura = tk.Entry(controls_frame)
entry_altura.grid(row=4, column=1, sticky="w")
btn_reescalar = tk.Button(controls_frame, text="Reescalar", command=reescalar)
btn_reescalar.grid(row=5, column=0, pady=10)

# Crop controls
tk.Label(controls_frame, text="Recortar").grid(row=6, column=0, sticky="w")
entry_x1 = tk.Entry(controls_frame)
entry_x1.grid(row=7, column=1, sticky="w")
entry_y1 = tk.Entry(controls_frame)
entry_y1.grid(row=8, column=1, sticky="w")
entry_x2 = tk.Entry(controls_frame)
entry_x2.grid(row=9, column=1, sticky="w")
entry_y2 = tk.Entry(controls_frame)
entry_y2.grid(row=10, column=1, sticky="w")
btn_recortar = tk.Button(controls_frame, text="Recortar", command=recortar)
btn_recortar.grid(row=11, column=0, pady=10)

# Center Crop controls
tk.Label(controls_frame, text="Recortar Centro").grid(row=12, column=0, sticky="w")
entry_cx = tk.Entry(controls_frame)
entry_cx.grid(row=13, column=1, sticky="w")
entry_cy = tk.Entry(controls_frame)
entry_cy.grid(row=14, column=1, sticky="w")
entry_anchura_centro = tk.Entry(controls_frame)
entry_anchura_centro.grid(row=15, column=1, sticky="w")
entry_altura_centro = tk.Entry(controls_frame)
entry_altura_centro.grid(row=16, column=1, sticky="w")
btn_recortar_centro = tk.Button(controls_frame, text="Recortar Centro", command=recortarCentro)
btn_recortar_centro.grid(row=17, column=0, pady=10)

# Brightness controls
tk.Label(controls_frame, text="Brillo").grid(row=18, column=0, sticky="w")
brillo_slider = tk.Scale(controls_frame, from_=-200, to=200, orient="horizontal", command=cambiaBrillo)
brillo_slider.grid(row=19, column=0, sticky="w")

# Contrast controls
tk.Label(controls_frame, text="Contraste").grid(row=20, column=0, sticky="w")
contraste_slider = tk.Scale(controls_frame, from_=0.1, to=4, resolution=0.1, orient="horizontal", command=cambiaContraste)
contraste_slider.grid(row=21, column=0, sticky="w")

# Process button
btn_procesar = tk.Button(controls_frame, text="Procesar Negativo", command=procesaImagen)
btn_procesar.grid(row=22, column=0, pady=10)

# Feedback label
retroalimentacion = tk.Label(controls_frame, text="")
retroalimentacion.grid(row=23, column=0, pady=10)

# Preview label
preview_label = tk.Label(preview_frame)
preview_label.pack()

ventana.mainloop()