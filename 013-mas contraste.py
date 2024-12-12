from PIL import Image

ruta_imagen = "imagenes/josevicente.jpg"
imagen = Image.open(ruta_imagen)

anchura,altura = imagen.size
pixeles = imagen.load()
for x in range(0,anchura):
    for y in range(0,altura):
        rojo,verde,azul = pixeles[x,y]
        pixeles[x,y] = (
            rojo*2,
            verde*2,
            azul*2
            )
imagen.show()
imagen.save("resultado.jpg")
