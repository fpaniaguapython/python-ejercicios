class DecoradorSimple:
    def __init__(self, funcion_a_decorar):
        self.funcion_a_decorar = funcion_a_decorar

    def __call__(self, *args, **kwds):
        print("Antes")
        self.funcion_a_decorar(*args, **kwds)
        print("Después")


@DecoradorSimple()
def saludar():
    print("Hola")

saludar()