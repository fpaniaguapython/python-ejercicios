from CalculadoraBinaria import CalculadoraBinaria
from CalculadoraDecimal import CalculadoraDecimal
from CalculadoraHexadecimal import CalculadoraHexadecimal

class CalculadoraFactory:
    @staticmethod
    def __get_tipo_calculadora():
        return 2

    @staticmethod
    def get_calculadora():
        tipo = CalculadoraFactory.__get_tipo_calculadora()
        if (tipo==1):
            return CalculadoraDecimal()
        elif (tipo==2):
            return CalculadoraBinaria()
        elif (tipo==3):
            return CalculadoraHexadecimal()

