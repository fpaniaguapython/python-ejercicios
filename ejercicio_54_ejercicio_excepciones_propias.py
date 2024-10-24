'''
Crear una clase Alumno que reciba en el constructor
el nombre y la dirección de e-mail.
Si la dirección de email está vacía debe lanzar
una excepción EmailVacioError
'''
class EmailVacioError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class Alumno:
    @staticmethod
    def verificar_email(email):
        if (len(email)<=0):
            raise EmailVacioError("La longitud es insuficiente")

    def __init__(self, nombre, email) -> None:
        Alumno.verificar_email(email=email)
        self.nombre = nombre
        self.email = email

try:
    alumno = Alumno("Fernando","f@gmail.com")
except EmailVacioError as eve:
    print(eve)