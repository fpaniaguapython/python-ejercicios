def decorador_simple(funcion):
    print("Soy un decorador simple")
    return funcion

@decorador_simple
def saludador(nombre):
    print("Hola",nombre)

saludador('Fernando')

