from JVImagen import *
import tkinter as tk
from tkinter import Tk, filedialog
from PIL import Image, ImageTk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

entrada = ""
salida = ""
brillo = 0
contraste = 1.0
original_image = None
preview_image = None

# Function to open an image and display it in the preview pane
def abrirImagen():
    global entrada, original_image, preview_image
    print("Vamos a abrir la imagen")
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
    print("Vamos a guardar la imagen")
    salida = filedialog.asksaveasfilename(
        title="Selecciona imagen de destino",
        defaultextension=".jpg",
        filetypes=[("JPEG files", "*.jpg"), ("PNG files", "*.png"), ("BMP files", "*.bmp"), ("GIF files", "*.gif")]
    )

def cambiaBrillo(value):
    global brillo
    brillo = int(value)
    aplicarCambios()

def cambiaContraste(value):
    global contraste
    contraste = float(value)
    aplicarCambios()

# Function to apply changes to the preview image
def aplicarCambios():
    global original_image, preview_image, brillo, contraste
    if original_image:
        imagen_temp = JVImagen(entrada, salida)
        imagen_temp.brillo(brillo)
        imagen_temp.contraste(contraste)
        preview_image = Image.fromarray(imagen_temp.obtener_array())
        actualizarVista()

def procesaImagen():
    global entrada, salida, opcion
    if entrada and salida:
        print("La opcion elegida es", opcion.get())
        imagen = JVImagen(entrada, salida)
        if opcion.get() == "1":
            imagen.negativo()
        elif opcion.get() == "2":
            imagen.brillo(brillo)
        elif opcion.get() == "3":
            imagen.contraste(contraste)
        imagen.guarda()
        retroalimentacion.config(text="Imagen guardada correctamente")
    else:
        retroalimentacion.config(text="Selecciona entrada y salida")

# Function to update the preview pane
def actualizarVista():
    global preview_image
    if preview_image:
        img_resized = preview_image.resize((300, 300))
        img_tk = ImageTk.PhotoImage(img_resized)
        preview_label.config(image=img_tk)
        preview_label.image = img_tk

ventana = ttk.Window(themename="cosmo")
ventana.geometry("800x400")
ventana.title("JVShop")

opcion = tk.StringVar(value="1")

# Controls frame on the left
controls_frame = tk.Frame(ventana)
controls_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nw")

# Preview frame on the right
preview_frame = tk.Frame(ventana)
preview_frame.grid(row=0, column=1, padx=20, pady=20, sticky="ne")

# Buttons and controls
btn_abrir = tk.Button(controls_frame, text="Selecciona la imagen de entrada", command=abrirImagen, width=30)
btn_abrir.grid(row=0, column=0, pady=10)

radio_negativo = tk.Radiobutton(controls_frame, text="Negativo", variable=opcion, value=1, command=aplicarCambios)
radio_negativo.grid(row=1, column=0, sticky="w")

radio_brillo = tk.Radiobutton(controls_frame, text="Brillo", variable=opcion, value=2)
radio_brillo.grid(row=2, column=0, sticky="w")

brillo_slider = tk.Scale(controls_frame, from_=-200, to=200, orient="horizontal", command=cambiaBrillo)
brillo_slider.grid(row=3, column=0, sticky="w")

radio_contraste = tk.Radiobutton(controls_frame, text="Contraste", variable=opcion, value=3)
radio_contraste.grid(row=4, column=0, sticky="w")

contraste_slider = tk.Scale(controls_frame, from_=0.1, to=4, resolution=0.1, orient="horizontal", command=cambiaContraste)
contraste_slider.grid(row=5, column=0, sticky="w")

btn_guardar = tk.Button(controls_frame, text="Selecciona la imagen de salida", command=guardarImagen, width=30)
btn_guardar.grid(row=6, column=0, pady=10)

btn_procesar = tk.Button(controls_frame, text="Procesar", command=procesaImagen, width=30)
btn_procesar.grid(row=7, column=0, pady=10)

retroalimentacion = tk.Label(controls_frame, text="")
retroalimentacion.grid(row=8, column=0, pady=10)

# Preview label
preview_label = tk.Label(preview_frame)
preview_label.pack()

ventana.mainloop()