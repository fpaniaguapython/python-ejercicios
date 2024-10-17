import gc

class Pelicula:
    pass

class Serie:
    pass

p1 = Pelicula()
p2 = Pelicula()
p3 = Pelicula()

s1 = Serie()
s2 = Serie()

def contar_instancias(clase):
    instancias = [instancia for instancia in gc.get_objects() if isinstance(instancia, clase)]
    return instancias

instancias = contar_instancias(Pelicula)
print(f"Número de instancias: {len(instancias)}")
print("Instancias:", instancias)