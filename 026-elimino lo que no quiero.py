from PIL import Image, ImageDraw
import cv2
import numpy as np

image_path = "imagenes/josevicente.jpg"
pil_image = Image.open(image_path)

cv_image = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
gray_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
draw = ImageDraw.Draw(pil_image)
for (x, y, w, h) in faces:
    cx = x+round(w/2)
    cy = y+round(h/2)
print(cx,cy)

