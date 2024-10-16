class Entidad:
    pass

e1 = Entidad()
e2 = Entidad()
i1 = 5
i2 = 8
s1 = "cadena1"
s2 = "cadena2"

objetos = [e1, e2, i1, i2, s1, s2]

for objeto in objetos:
    if isinstance(objeto, Entidad):
        print("Entidad encontrada")
