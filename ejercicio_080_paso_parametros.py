# Crear un función que recibe como argumentos:
# 1. Un número
# 2. Una cadena de caracteres
# 3. Una lista de números
# 4. Una lista de números que contiene otra lista de números
# 5. Un objeto de la clase película
# La función modifica los parámetros que recibe
# ¿Cómo quedan dichos párametros fuera de la función?
# ¿Qué parámetros se han pasado por valor / referencia?

class Pelicula:
    def __init__(self, titulo, duracion):
        self.titulo = titulo
        self.duracion = duracion
    
    def __str__(self) -> str:
        return f'Título:{self.titulo}. Duración:{self.duracion}'

def funcion(numero, cadena, lista_numeros, lista_anidada, pelicula):
    numero = 10
    cadena = "Cadena modificada"
    lista_numeros[0] = -1
    lista_anidada[0][1] = -1
    pelicula.titulo = "Título modificado"

numero = 1
cadena = "Cadena sin modificar"
lista_numeros = [1,2,3]    
lista_anidada = [[1,2,3],4,5]
pelicula = Pelicula("Título sin modificar", 100)

funcion(numero, cadena, lista_numeros, lista_anidada, pelicula)

print(numero) # 1 (Paso por valor)
print(cadena) # Cadena sin modificar (Paso por valor)
print(lista_numeros) # [-1, 2, 3] (Paso por referencia)
print(lista_anidada) # [[1, -1, 3], 4, 5] (Paso por referencia)
print(pelicula) # Título:Título modificado. Duración:100 (Paso por referencia)
