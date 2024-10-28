# 1. Crear una clase Pelicula con dos atributos
# 2. Instanciar un objeto de la clase Pelicula
# 3. Asignar el objeto a una nueva variable
# 4. ¿Son el mismo objeto?
# 5. Modificar el valor de uno de los atributos del primer objeto
# 6. ¿Se han cambiado los dos objetos?
# 7. ¿Son el mismo objeto?

# 1
class Pelicula:
    def __init__(self, titulo, duracion):
        self.titulo = titulo
        self.duracion = duracion

    def __eq__(self, value: object) -> bool:
        return self.titulo == value.titulo

# 2
peli1 = Pelicula("Título 1", 100)
peli2 = Pelicula("Título 1", 100)
# 3
peli3 = peli1

print(peli1 == peli2) # True
print(peli1 is peli2) # False
# 4
print(peli1 is peli3) # True: peli1 y peli3 son el mismo objeto

# 5
peli1.titulo = "Título modificado"

#6, 7 --> Se ha modificado en los 'dos objetos' (son el mismo) 
print(peli1.titulo) # Título modificado
print(peli3.titulo) # Título modificado