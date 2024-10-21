# Decorador que escriba en un fichero fecha y hora a la que  se ha ejecutado una 
# función. La escritura de la fecha y la hora se realizará en función de un 
# parámetro indicado en el propio decorador
import datetime

class Logwriter:
    def __init__(self, enabled, file_name):
        self.enabled = enabled
        self.file_name = file_name

    def __call__(self, funcion):
        def wrapper(*args, **kwargs):
            if (self.enabled==True):
                self.write_log(self.file_name,"El texto del log")
            retorno = funcion(*args, **kwargs)
            return retorno
        return wrapper
    
    def write_log(self, file_name, log):
        with open(file_name, 'a') as f_log:
            f_log.write(str(datetime.datetime.now()) + log + '\n')


@Logwriter(True, "logoo.txt")
def saludar(nombre):
    return "Hola"+nombre

print(saludar("Adrian"))