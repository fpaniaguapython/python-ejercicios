#built-in types/classes

class CustomList(list):
    def __init__(self, list_type):
        self.list_type = list_type
    
    def check_object(self, object):
        if type(object) is not self.list_type:
            raise TypeError('El elemento no es del tipo '+ str(self.list_type))
        
    def append(self, object):
        self.check_object(object)
        super().append(object)

    def insert(self, index, object):
        self.check_object(object)
        super().insert(index, object)

    def extend(self, iterable):
        for item in iterable:
            self.check_object(item)
        super().extend(iterable)

    def __setitem__(self, key, value):
        self.check_object(value)
        super().__setitem__(key, value)

lista = CustomList(str)
# lista.append(True) # Provoca error
lista.append('Verdadero')
# lista.insert(0, 8) # Provoca error
lista.insert(0,'Inserta')
# lista.extend([2,3]) # Provoca error
lista.extend(('uno','dos'))
#lista[1]=3 # Provoca error
lista[1]='Cosa'
print(lista)