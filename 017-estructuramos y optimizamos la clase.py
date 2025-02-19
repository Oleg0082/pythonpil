from PIL import Image

class JVImagen:
    def __init__(self,entrada,salida):
        self.entrada = entrada
        self.salida = salida
        self.imagen = Image.open(self.entrada)
        self.anchura,self.altura = self.imagen.size
        self.pixeles = self.imagen.load()
    
    def brillo(self,factor):
        for x in range(0,self.anchura):
            for y in range(0,self.altura):
                rojo,verde,azul = self.pixeles[x,y]
                self.pixeles[x,y] = (
                    round(rojo+factor),
                    round(verde+factor),
                    round(azul+factor)
                    )

    def contraste(self,factor):
        for x in range(0,self.anchura):
            for y in range(0,self.altura):
                rojo,verde,azul = self.pixeles[x,y]
                self.pixeles[x,y] = (
                    round(rojo*factor),
                    round(verde*factor),
                    round(azul*factor)
                    )
        
        
    def muestra(self):
        self.imagen.show(self)
    def guarda():
        self.imagen.save(self.salida)

imagen = JVImagen("imagenes/josevicente.jpg","resultado.jpg")
imagen.brillo(200)
imagen.muestra()
