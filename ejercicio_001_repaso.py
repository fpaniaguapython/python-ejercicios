lista1 = [1,True,"Hola"]
lista2 = list()#Creamos una lista vacía
lista3 = []

tupla1 = (1,True,"Hola")
tupla2 = tuple(lista1)#Creamos una tupla a partir de la lista1
tuple3 = ()#Tupla
tupla4 = (5)#int OJO
tupla5 = (5,)#Tupla

for elemento in lista1:
    print(elemento)

diccionario1 = {"k1":"v1","k2":"v2","k3":"v3"}
diccioanrio2 = {}
diccionario3 = dict()

for clave in diccionario1.keys():
    print(clave)

for value in diccionario1.values():
    print(value)

for k,v in diccionario1.items():
    print(k,v)

conjunto1 = {3,4,38}
conjunto2 = set({4,3,8})
 