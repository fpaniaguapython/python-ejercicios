#built-in types/classes

class StringList(list):
    @staticmethod
    def check_object(object):
        if type(object) is not str:
            raise TypeError('No es un str')

    def append(self, object):
        StringList.check_object(object)
        super().append(object)

    def insert(self, index, object):
        StringList.check_object(object)
        super().insert(index, object)

    def extend(self, iterable):
        for item in iterable:
            StringList.check_object(item)
        super().extend(iterable)

    def __setitem__(self, key, value):
        StringList.check_object(value)
        super().__setitem__(key, value)

lista = StringList()
# lista.append(True) # Provoca error
lista.append('Verdadero')
# lista.insert(0, 8) # Provoca error
lista.insert(0,'Inserta')
# lista.extend([2,3]) # Provoca error
lista.extend(('uno','dos'))
# lista[1]=3 # Provoca error
lista[1]='Cosa'
print(lista)


