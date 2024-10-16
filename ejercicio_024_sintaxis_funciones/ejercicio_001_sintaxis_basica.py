def funcion_1():
    pass

def funcion_2(cantidad : int):
    pass

def funcion_3(cantidad : int = 10 ):
    pass

def funcion_4(cantidad, peso = 10): #Siempre el valor por defecto al final
    pass

def funcion_5(cantidad, *args):
    print(args)#(3, 8, 'Diez', True)
    print(type(args))#<class 'tuple'>
    print(*args)#3 8 Diez True
    
    

funcion_5(10, 3, 8, "Diez",True)

