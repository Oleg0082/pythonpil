from PIL import Image

class JVImagen:
    def __init__(self,entrada,salida):
        self.entrada = entrada
        self.salida = salida
        self.imagen = Image.open(self.entrada)
        self.anchura,self.altura = self.imagen.size
        self.pixeles = self.imagen.load()

    def reescalar(self,nuevaanchura,nuevaaltura):
        tamano = (nuevaanchura,nuevaaltura)
        self.imagen = self.imagen.resize(tamano)
        self.anchura,self.altura = self.imagen.size
        self.pixeles = self.imagen.load()

    def recortar(self,x1,y1,x2,y2):
        coordenadas_recorte = (x1, y1, x2, y2)
        self.imagen = self.imagen.crop(coordenadas_recorte)
        self.anchura,self.altura = self.imagen.size
        self.pixeles = self.imagen.load()
    
    def recortarCentro(self,cx,cy,anchura,altura):
        coordenadas_recorte = (
            cx-round(anchura/2), 
            cy-round(altura/2), 
            cx+round(anchura/2), 
            cy+round(altura/2))
        self.imagen = self.imagen.crop(coordenadas_recorte)
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

    def negativo(self,factor):
        for x in range(0,self.anchura):
            for y in range(0,self.altura):
                rojo,verde,azul = self.pixeles[x,y]
                self.pixeles[x,y] = (
                    255-rojo,
                    255-verde,
                    255-azul
                    )
        
        
    def muestra(self):
        self.imagen.show(self)
    def guarda(self):
        self.imagen.save(self.salida)