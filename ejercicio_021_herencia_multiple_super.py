class Automovil:
    def arrancar(self):
        print ("Soy Automovil y estoy arrando...")

class Barco:
    def arrancar(self):
        print ("Soy Barco y estoy arrando...")

class Anfibio(Automovil, Barco):
    def arrancar(self):
        super().arrancar()

Anfibio().arrancar()#Soy Automovil y estoy arrando...
