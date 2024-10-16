#Crear una clase que transforme a voz un texto
#Crear una clase que escriba en un fichero un texto
#Crear una clase que contenga un texto y que pueda 
#transformar a voz y escribir el texto con las clases anteriores

from gtts import gTTS
import os

class Locutor:
    def enunciar(self, text, language = 'es'):
        myobj = gTTS(text=text, lang=language, slow=False)
        myobj.save("temporal.mp3")
        os.system("temporal.mp3")

class Escritor:
    def escribir(self, text, file_name = "temporal.txt"):
        with open(file_name, "w") as fichero:
            fichero.write(text)

#Con herencia múltiple
class Factura(Locutor, Escritor):
    def __init__(self, nombre) -> None:
        super().__init__()
        self.nombre = nombre
    def di_tu_nombre(self):
        self.enunciar(self.nombre)

#Factura("El nombre del cliente").di_tu_nombre()

#Con composición
class Animal:
    def __init__(self, nombre) -> None:
        self.nombre = nombre
        self.locutor = Locutor()
        self.escritor = Escritor()
        self.locutor.enunciar(self.nombre)
        self.escritor.escribir(f'Soy {self.nombre} y soy un animal','animal.txt')

Animal("Tigre de bengala")
