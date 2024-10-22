from CalculadoraFactory import CalculadoraFactory
from ICalculadora import ICalculadora

if __name__=='__main__':
    calculadora = CalculadoraFactory.get_calculadora()
    if (isinstance(calculadora, ICalculadora)):
        print(calculadora.sumar(2,3))
    else:
        print("No es una calculadora")