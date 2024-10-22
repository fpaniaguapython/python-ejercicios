from ICalculadora import ICalculadora

class CalculadoraDecimal(ICalculadora):
    def sumar(self, operando1, operando2):
        return operando1 + operando2

    def restar(self, operando1, operando2):
        return operando1 - operando2

    def multiplicar(self, operando1, operando2):
        return operando1 * operando2

    def dividir(self, operando1, operando2):
        return operando1 / operando2