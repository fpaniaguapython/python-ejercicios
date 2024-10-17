def funcion_auxiliar(*args):
    print(len(args))

def funcion_5(cantidad, *args):#***********************
    funcion_auxiliar(*args)#Pasa los elementos de args 'separados por coma'
    funcion_auxiliar(args)#Pasa una tupla con el contenido de args

    print(args)#(3, 8, 'Diez', True)
    print(type(args))#<class 'tuple'>
    print(*args)#3 8 Diez True

funcion_5(10, 3, 8, "Diez",True)#***********************

def funcion_6(pais, **kwargs):
    print(type(kwargs))
    print(kwargs)

funcion_6("España", Zaragoza=694_000, Huesca=54_000, Teruel=36_267)

#empresa,ubicacion,lista de productos,facturacion por meses
#*args, **kwargs
def function_7(empresa, ubicacion, *args, trimestre=1, **kwargs, ):
    pass
