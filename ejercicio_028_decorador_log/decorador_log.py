#Decorador que escriba en un fichero fecha y hora a la que  se ha ejecutado una función.
#La escritura de la fecha y la hora se realizará en función de un parámetro 
#almacenado en un fichero

import json
import datetime

def is_log_active():
    with open('config.json','r') as f_config:
        config = json.load(f_config)
        return config['log']
    
def write_log(file_name, log):
    with open(file_name, 'a') as f_log:
        f_log.write(str(datetime.datetime.now()) + log + '\n')
    
def logeador(funcion):
    def wrapper(*args, **kwargs):
        if (is_log_active()):
            write_log('log.txt',funcion.__name__)
        return funcion(*args, **kwargs)
    return wrapper

@logeador
def sumar(s1, s2):
    return s1+s2 

@logeador
def saludar():
    print("Hola")

print(sumar(3,8))
saludar()
    

    
