# Este ejercicio no está completo

def entidad(nombre_db):
    def external_wrapper(funcion):
        def internal_wrapper(*args, **kwargs):
            print(nombre_db)
            print(*args)
            funcion(*args, **kwargs)
        return internal_wrapper
    return external_wrapper

class Cliente:
    @entidad('t_clientes')
    def __init__(self, nombre, saldo):
        pass

    @atributo('nombre')
    def set_nombre(self, nombre):
        pass

c = Cliente('Juan',1000)