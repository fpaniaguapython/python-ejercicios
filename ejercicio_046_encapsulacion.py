class Cosa:
    def __init__(self) -> None:
        self.nombre = "Nombre" #Público
        self._edad = 35 #'Protected'
        self.__altura = 1.70 #Privado (oculto)

    #Método de acceso 'get' artesanal
    def get_altura(self):
        return(self.__altura)
    
    #Este decorador 'convierte' el método 'altura' en un atributo de lectura
    @property
    def altura(self):
        return(self.__altura)
    
    #Método de acceso 'set' artesanal
    def set_altura(self, nueva_altura):
        self.__altura = nueva_altura
    
    #Este decorador 'convierte' el método 'altura' en un atributo de escritura
    @altura.setter #Requiere la existencia del @property con el mismo nombre
    def altura(self, nueva_altura):
        self.__altura = nueva_altura

    # Relacionado con la función delattr, 'interceptamos' la ejecución de 
    # la eliminación del atributo
    @altura.deleter
    def altura(self):
        print('Eliminado el atributo altura')
        delattr(self, '_Cosa__altura')

c = Cosa()
print(c.get_altura())
print(c.altura)
c.altura = 1.80
print(c.altura)
c.set_altura(1.90)
print(c.get_altura())
delattr(c, 'altura')
print(c.altura)

