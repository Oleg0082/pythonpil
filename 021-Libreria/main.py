from JVImagen import *

imagen = JVImagen("imagenes/josevicente.jpg","resultado.jpg")
imagen.reescalar(200,200)
imagen.negativo(200)
imagen.contraste(3)
imagen.muestra()
