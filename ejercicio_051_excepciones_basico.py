def dividir(dividendo, divisor):
    return dividendo / divisor

#Apilamiento de excepciones --> Primera la más específica; Última las más genérica

try:
    resultado = dividir(dividendo=10, divisor=0)
except ZeroDivisionError as zde:
    print(zde) # division by zero
    print(zde.args) # ('division by zero',)
    #¿print(zde.path)?
except ArithmeticError as ae:
    pass
except Exception as e:
    pass
except BaseException as be:
    pass

# Cada tipo de excepción tiene sus propios atributos
try:
    import modulo_inexistente
except ImportError as ie:
    print(ie.args)
    print(ie.name)
    print(ie.path)


#Exception try-except-else-finally
try:
    print("1")
    x = 10 / 1 # 1
    print("1b") # 1b si no error
except ZeroDivisionError as zde:
    print("2:",zde) # 2 si error
else:
    print("3:","Else") # 3 si no error
finally:
    print("4","Finally") # 4 siempre
