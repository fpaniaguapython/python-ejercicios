'''
Crear un clase Empleado con los atributos privados:
- Nombre
- Email
- Salario

El constructor debe verificar que los datos de entrada son correctos:
- Nombre es cadena de caracteres no vacia y sin espacios en los extremos.
- Email es un email
- Salario es > Salario mínimo interprofesional

Crear los métodos de acceso siguientes mediante el uso de notaciones:
- Nombre: get y set (acceso y modificación como propiedades).
- Email: get y set (acceso y modificación como propiedades).
- Salario: get (acceso como propiedad).
'''
import re
class Empleado:
    salario_minimo_interprofesional = 15_800

    def __init__(self, nombre, email, salario) -> None:
        self.__nombre = Empleado.verificar_nombre(nombre) #Validamos en el __init__
        self.email = email #Validamos en el setter
        self.__salario = Empleado.verificar_salario(salario) #Validamos en el __init__
    
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def email(self):
        return self.__email
    
    @property
    def salario(self):
        return self.__salario
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    @email.setter
    def email(self, nuevo_email):
        self.__email = Empleado.verificar_email(nuevo_email)

    @staticmethod
    def verificar_nombre(nombre):
        if (not isinstance(nombre, str)):
            raise TypeError("El nombre no es un string")
        if (len(nombre.strip())==0 or nombre.strip()!=nombre):
            raise ValueError("El nombre no puede estar vacio ni contener espacios en los extremos")
        return nombre
    
    @staticmethod
    def verificar_email(email):
        if not re.match(r'^\S+@\S+\.\S+$',email):
            raise ValueError("Email incorrecto")
        return email
    
    @staticmethod
    def verificar_salario(salario):
        if (salario < Empleado.salario_minimo_interprofesional):
            raise ValueError("El salario es insuficiente")
        
try:
    e1 = Empleado("Fernando","fernando.paniagua@gmail.com",25_000)
    #e2 = Empleado("Fernando","fernando.paniagua@gmail.com",12_000)
    #e3 = Empleado("Fernando","fernandogmail.com",25_000)
    #e4 = Empleado(10_000,"fernandogmail.com",25_000)
    #e5 = Empleado("         ","fernandogmail.com",25_000)
    #e6 = Empleado("","fernandogmail.com",25_000)
except BaseException as be:
    print(be)