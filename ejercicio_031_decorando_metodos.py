def decorador(funcion):
    def wrapper(*args, **kwargs):
        print("Soy el decorador")
        return funcion(*args, **kwargs)
    return wrapper

class MiClase:
    @decorador
    def __init__(self) -> None:
        pass

    @decorador
    def metodo(self):
        pass

MiClase().metodo()