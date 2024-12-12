from PIL import Image

ruta_imagen = "imagenes/josevicente.jpg"
imagen = Image.open(ruta_imagen)

anchura,altura = imagen.size
pixeles = imagen.load()
for x in range(0,anchura):
    for y in range(0,altura):
        pixeles[x,y] = (127,127,127)
imagen.save("resultado.jpg")
