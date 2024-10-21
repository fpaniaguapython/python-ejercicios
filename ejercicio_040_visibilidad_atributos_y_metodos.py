class Enemigo:
    def __init__(self, nombre, fuerza, salud):
        self.nombre = nombre #Public
        self._fuerza = fuerza #Protected?
        self.__salud = salud # Private... private?

    def get_salud(self):
        return self.__salud
    
    def get_salud_compinche(self, compinche):
        return compinche.__salud
    
    def __calcular_raiz_cuadrada(self):
        print("Soy un método private...")

sauron = Enemigo('Sauron', 10_000, 100)
print(sauron.nombre)#Ok
print(sauron._fuerza)#Ok
#print(sauron.__salud)#AttributeError: 'Enemigo' object has no attribute '__salud'
print(sauron.get_salud())#Ok
print(sauron._Enemigo__salud)#Ok
saruman = Enemigo('Saruman', 2_000, 50)
print(sauron.get_salud_compinche(saruman))#Ok

