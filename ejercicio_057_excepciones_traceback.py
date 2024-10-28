import traceback

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
    print(traceback.format_tb(me.__traceback__))
