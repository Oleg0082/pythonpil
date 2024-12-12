from PIL import Image, ImageDraw
import cv2
import numpy as np

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

    def recortarEnCara(self,anchura,altura):
        cx,cy = self.detectaCara()
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

    def negativo(self):
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
    def detectaCara(self):
        cv_image = cv2.cvtColor(np.array(self.imagen), cv2.COLOR_RGB2BGR)
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        gray_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        for (x, y, w, h) in faces:
            cx = x+round(w/2)
            cy = y+round(h/2)
        return (int(cx),int(cy))