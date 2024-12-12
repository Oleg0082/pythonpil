from JVImagen import *
import tkinter as tk

def abrirImagen():
    print("Vamos a abrir la imagen")

def guardarImagen():
    print("Vamos a guardar la imagen")

def procesaImagen():
    print("Vamos a procesar la imagen")

ventana = tk.Tk()

tk.Button(
    ventana,
    text="Seleciona la imagen de entrada",
    command = abrirImagen
    ).pack(padx=20,pady=20)

tk.Button(
    ventana,
    text="Seleciona la imagen de salida",
    command = guardarImagen
    ).pack(padx=20,pady=20)

tk.Button(
    ventana,
    text="Procesar",
    command = procesaImagen
    ).pack(padx=20,pady=20)

ventana.mainloop()


