from PIL import Image

def brillo(entrada,salida,factor):
    imagen = Image.open(entrada)
    anchura,altura = imagen.size
    pixeles = imagen.load()
    for x in range(0,anchura):
        for y in range(0,altura):
            rojo,verde,azul = pixeles[x,y]
            pixeles[x,y] = (
                round(rojo+factor),
                round(verde+factor),
                round(azul+factor)
                )
    imagen.show()
    imagen.save(salida)

def contraste(entrada,salida,factor):
    imagen = Image.open(entrada)
    anchura,altura = imagen.size
    pixeles = imagen.load()
    for x in range(0,anchura):
        for y in range(0,altura):
            rojo,verde,azul = pixeles[x,y]
            pixeles[x,y] = (
                round(rojo*factor),
                round(verde*factor),
                round(azul*factor)
                )
    imagen.show()
    imagen.save(salida)

contraste("imagenes/josevicente.jpg","resultado.jpg",0.5)
brillo("imagenes/josevicente.jpg","resultado.jpg",100)
