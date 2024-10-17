def depurador(funcion):
    def wrapper(*args, **kwargs):
        print("En el wrapper")
        return funcion(*args)
    return wrapper

@depurador
def sumar(a,b):
    print("Sumando")
    return a+b

print(sumar(3,8))