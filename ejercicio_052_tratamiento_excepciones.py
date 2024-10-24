def dividir(dividendo, divisor):
    try:
        resultado = dividendo / divisor
    except ZeroDivisionError as zde:
        print("Tratando el error", zde, "en dividir")
        raise zde
    return resultado

def calcular_saldo(operando1, operando2, operando3):
    operando_agrupado = operando1 + operando2
    try:
        resultado_division = dividir(dividendo=operando_agrupado, 
                                     divisor=operando3)
    except ZeroDivisionError as zde:
        print("Tratando el error", zde, "en calcular_saldo")
        raise zde
    return resultado_division

try:
    calcular_saldo(operando1=3, operando2=10, operando3=0)
except ZeroDivisionError as zde:
    print("Tratando el error", zde, "en la capa más superficial de la aplicación")
