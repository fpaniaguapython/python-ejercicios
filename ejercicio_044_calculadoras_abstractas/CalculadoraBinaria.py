from ICalculadora import ICalculadora

class CalculadoraBinaria(ICalculadora):
    def sumar(self, operando1, operando2):
        return bin(operando1 + operando2)

    def restar(self, operando1, operando2):
        return bin(operando1 - operando2)

    def multiplicar(self, operando1, operando2):
        return bin(operando1 * operando2)

    def dividir(self, operando1, operando2):
        return bin(operando1 / operando2)