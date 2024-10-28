class MiExcepton(Exception):
    pass

def comprobar(listado):
    try:
        print("2º Elemento:", listado[1])
    except IndexError as ie:
        raise MiExcepton() from ie

lista = ['Primer elemento']

try:
    comprobar(lista)
except MiExcepton as me:
    print(me.__context__) # list index out of range (supuestamente para encadenado implícito)
    print(me.__cause__) # list index out of range (consecuencia del raise de una excepción encadenada)
