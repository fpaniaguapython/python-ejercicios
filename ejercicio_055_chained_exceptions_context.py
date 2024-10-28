a = ['a','b']

# Variable __context__, contiene información sobre la excepción 'superior'
# en un encadenado implícito de excepciones
try:
    print(a[2])
except IndexError as ie:
    try:
        print(1 / 0)
    except ZeroDivisionError as zde:
        print("Exterior:", ie) # Exterior: list index out of range
        print("Interior:", zde) # Interior: division by zero
        print("Context (implícito):", zde.__context__) # Context (implícito): list index out of range
        print(zde.__cause__) # None (sólo en encadenamiento explícito) 
        print(ie is zde.__context__) # True