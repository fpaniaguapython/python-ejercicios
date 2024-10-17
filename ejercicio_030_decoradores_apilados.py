def decorador1(numero):
    def wrapper_externo(funcion):
        def wrapper(*args, **kwargs):
            print(f'Decorador {numero}')
            return funcion(*args)
        return wrapper
    return wrapper_externo

def decorador2(letra):
    def wrapper_externo(funcion):
        def wrapper(*args, **kwargs):
            print(f'Decorador {letra}')
            return funcion(*args)
        return wrapper
    return wrapper_externo            

@decorador2('F')
@decorador1(7)
def sumar(s1,s2):
    return s1+s2

print(sumar(12,1))

