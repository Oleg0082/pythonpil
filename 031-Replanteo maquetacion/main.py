from JVImagen import *
import tkinter as tk
from tkinter import Tk, filedialog
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

entrada = ""
salida = ""

def abrirImagen():
    global entrada
    print("Vamos a abrir la imagen")
    entrada = filedialog.askopenfilename(
        title="Selecciona imagen de origen",
        filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")]
    )

def guardarImagen():
    global salida
    print("Vamos a guardar la imagen")
    salida = filedialog.asksaveasfilename(
        title="Selecciona imagen de destino",
        defaultextension=".png",
        filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("BMP files", "*.bmp"), ("GIF files", "*.gif")]
    )

def procesaImagen():
    global entrada
    global salida
    imagen = JVImagen(entrada,salida)
    imagen.negativo()
    imagen.guarda()

#ventana = tk.Tk()
ventana = ttk.Window(themename="cosmo")
ventana.geometry("300x300")
ventana.title("JVShop")

marco = tk.Frame(ventana)
marco.pack(padx=40,pady=40)

tk.Button(
    marco,
    text="Seleciona la imagen de entrada",
    command = abrirImagen,
    width=100
    ).pack(padx=10,pady=10)

tk.Button(
    marco,
    text="Seleciona la imagen de salida",
    command = guardarImagen,
    width=100
    ).pack(padx=10,pady=10)

tk.Button(
    marco,
    text="Procesar",
    command = procesaImagen,
    width=100
    ).pack(padx=10,pady=10)

ventana.mainloop()


