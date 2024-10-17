def decorador_simple(funcion):
    print("Soy un decorador simple")
    return funcion

def saludador():
    print("Hola")

funcion_decorada = decorador_simple(saludador)
funcion_decorada()    