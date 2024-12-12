from JVImagen import *
import tkinter as tk
from tkinter import Tk, filedialog
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

entrada = ""
salida = ""
brillo = ""
contraste = ""

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
        defaultextension=".jpg",
        filetypes=[("JPEG files", "*.jpg"),("PNG files", "*.png"),  ("BMP files", "*.bmp"), ("GIF files", "*.gif")]
    )
def cambiaBrillo(value):
    global brillo
    brillo = value
def cambiaContraste(value):
    global contraste
    contraste = value
def procesaImagen():
    global entrada
    global salida
    global opcion
    global brillo
    global contraste
    print("La opcion elegida es ",opcion.get())
    imagen = JVImagen(entrada,salida)
    if opcion.get() == "1":
        imagen.negativo()
    elif opcion.get() == "2":
        imagen.brillo(int(brillo))
    elif opcion.get() == "3":
        imagen.contraste(int(contraste))
    imagen.guarda()
    retroalimentacion.config(text="Imagen guardada correctamente")

#ventana = tk.Tk()
ventana = ttk.Window(themename="cosmo")
ventana.geometry("300x400")
ventana.title("JVShop")

opcion = tk.StringVar(value="Opción 1")

marco = tk.Frame(ventana)
marco.pack(padx=40,pady=40)

tk.Button(
    marco,
    text="Seleciona la imagen de entrada",
    command = abrirImagen,
    width=100
    ).pack(padx=10,pady=10)

tk.Radiobutton(
        marco,
        text="Negativo",
        variable=opcion,
        value=1
    ).pack(anchor=tk.W)

tk.Radiobutton(
        marco,
        text="Brillo",
        variable=opcion,
        value=2
    ).pack(anchor=tk.W)

tk.Scale(
    marco, 
    from_=-200, 
    to=200, 
    orient="horizontal",
    command=cambiaBrillo
    ).pack(anchor=tk.W)

tk.Radiobutton(
        marco,
        text="Contraste",
        variable=opcion,
        value=3,
        command=cambiaContraste
    ).pack(anchor=tk.W)

tk.Scale(
    marco, 
    from_=0, 
    to=4, 
    orient="horizontal"
    ).pack(anchor=tk.W)

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

retroalimentacion = tk.Label(
    marco,
    text=""
    )
retroalimentacion.pack()
ventana.mainloop()


