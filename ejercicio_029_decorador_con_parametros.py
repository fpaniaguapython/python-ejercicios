def coloreador(color):
    def wrapper_externo(funcion):
        def wrapper(*args, **kwargs):
            #Ocurren cosas
            print(f'Soy de color {color}. Antes')
            resultado =  funcion(*args, **kwargs)
            print(f'Soy de color {color}. Después')
            #Ocurren más cosas
            return resultado
        return wrapper
    return wrapper_externo

@coloreador('azul')
def saludar():
    print("Hola")

saludar()
