class GeneradorPDF:
    def generar_pdf(self, item):
        pass

class Factura:
    def __init__(self, nombre_cliente, generador : GeneradorPDF) -> None:
        self.nombre_cliente = nombre_cliente
        self.generador = generador

factura = Factura("Cliente", GeneradorPDF())
factura.generador.generar_pdf()#Dispongo de funcionalidad de generación de pdfs


