import abc

class ICalculadora(abc.ABC):
    @abc.abstractmethod
    def sumar(self, operando1, operando2):
        pass

    @abc.abstractmethod
    def restar(self, operando1, operando2):
        pass

    @abc.abstractmethod
    def multiplicar(self, operando1, operando2):
        pass

    @abc.abstractmethod
    def dividir(self, operando1, operando2):
        pass
