# Shallow copy - Copia superficial
# Deep copy - Copia en profundidad

# Función id(objeto) --> Proporciona el identificador de un objeto

x = 10
print(id(x)) # 140709207205064

# Caso 1
a = 10
b = a # Asigna el valor
a = 11
print(b) # 10

# Caso 2
a = 'Hola'
b = a
a = 'Adios'
print(b) # Hola

# Caso 3
a = 5
b = 5
a = 3
print(b) # 5

# Caso 4
a = 'Hola'
b = 'Hola'
a = 'Adios'
print(b) # Hola

# Caso 5
a = [1, 2, 3]
b = a # Asignando la referencia
a[0]=4
print(b) # [4, 2, 3]

# Caso 6
a = [1, 2, 3]
b = a[:] # Asignando los valores
a[0]=4
print(b) # [1, 2, 3]

# Caso 7 (Shallow copy - Copia superficial)
# ATENCIÓN: El nivel superficial de a se copia por valor
# pero el segundo nivel se copia por referencia.
a = [1, 2, [3, 4, 5]]
b = a[:] 
a[0]=7
a[2][0]=6
print(a) # [7, 2, [6, 4, 5]]
print(b) # [1, 2, [6, 4, 5]]

# Caso 8 (Deep copy - Copia en profundidad)

import copy

a = [1, 2, [3, 4, 5]]
b = copy.deepcopy(a) 
a[0]=7
a[2][0]=6
print(a) # [7, 2, [6, 4, 5]] - Son objetos distintos
print(b) # [1, 2, [3, 4, 5]] - Son objetos distintos