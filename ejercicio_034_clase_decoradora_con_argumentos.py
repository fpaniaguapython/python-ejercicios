class Decorador:
    def __init__(self, idioma):
        self.idioma = idioma

    def __call__(self, funcion):
        def wrapper(*args, **kwargs):
            print("Antes:" + self.idioma)
            retorno = funcion(*args, **kwargs)
            print("Después:" + self.idioma)
            return retorno
        return wrapper

@Decorador('Inglés')
def saludar(nombre):
    return "Hola"+nombre

print(saludar("Adrian"))