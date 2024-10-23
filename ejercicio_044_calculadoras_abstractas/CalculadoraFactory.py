import json

from CalculadoraBinaria import CalculadoraBinaria
from CalculadoraDecimal import CalculadoraDecimal
from CalculadoraHexadecimal import CalculadoraHexadecimal
from tipos_calculadora import TipoCalculadora

class CalculadoraFactory:
    @staticmethod
    def __get_tipo_calculadora():
        with open("config.json","rt") as fichero:
            configuracion =  json.load(fichero)
        return configuracion['tipo_calculadora']

    @staticmethod
    def get_calculadora():
        tipo = CalculadoraFactory.__get_tipo_calculadora()
        '''
        if (tipo==TipoCalculadora.DECIMAL):
            return CalculadoraDecimal()
        elif (tipo==TipoCalculadora.BINARIA):
            return CalculadoraBinaria()
        elif (tipo==TipoCalculadora.HEXADECIMAL):
            return CalculadoraHexadecimal()
        '''
        match tipo:
            case TipoCalculadora.DECIMAL.value:
                return CalculadoraDecimal()
            case TipoCalculadora.BINARIA.value:
                return CalculadoraBinaria()
            case TipoCalculadora.HEXADECIMAL.value:
                return CalculadoraHexadecimal()
            case _: #Por defecto
                return CalculadoraDecimal()


