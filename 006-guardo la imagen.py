from PIL import Image

ruta_imagen = "imagenes/josevicente.jpg"
imagen = Image.open(ruta_imagen)


anchura,altura = imagen.size
pixeles = imagen.load()
pixeles[0,0] = (0,0,0)
imagen.save("resultado.png")
