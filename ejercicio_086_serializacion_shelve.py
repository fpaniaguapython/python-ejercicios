import shelve

class Pelicula:
    def __init__(self, titulo) -> None:
        self.titulo = titulo
        self.duracion = 100

    def __str__(self) -> str:
        return f'Título:{self.titulo}. Duración:{self.duracion}'

file_name = 'fichero.shlv' # Nombre del fichero
shelve_obj = shelve.open(filename=file_name, flag='c') # Creamos el objeto shelve
# Valores de flag son:
# c - Creación si no existe. Lectura y escritura. (Por defecto)
# w - Si no existe, error. Lectura y escritura.
# r - Sólo lecutra.
# n - Crea SIEMPRE. Lectura y escritura.


# Escritura
shelve_obj['clave'] = "Valor"
#shelve_obj['numero'] = 3
#shelve_obj['pelicula'] = Pelicula('Rambo')

# Lectura
print(shelve_obj['clave'])
print(shelve_obj['numero'])
print(shelve_obj['pelicula'])

# Uso de la función len
print(len(shelve_obj))#Nos proporciona el número de elementos que tenemos en el fichero

# Uso del operador in
print('clave' in shelve_obj) # True
print('formato' in shelve_obj) # False

# Iterar por los elementos:
for k,v in shelve_obj.items():
    print("ITEM:", k,v)

for k in shelve_obj.keys():
    print("KEY:", k)

for v in shelve_obj.values():
    print("VALUE:", v)    

# Actualización:
shelve_obj['clave']='Valor modificado'

# Eliminación
#del shelve_obj['clave']

shelve_obj.close() # Cerramos el fichero