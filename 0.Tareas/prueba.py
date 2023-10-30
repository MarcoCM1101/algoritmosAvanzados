# Lista de cuadrados
cuadrados = [x ** 2 for x in range(10)]

# Set de cuadrados
cuadrados_set = {x ** 2 for x in range(10)}

# Diccionario de cuadrados
cuadrados_dict = {x: x ** 2 for x in range(10)}

# Generador de cuadrados
cuadrados_gen = (x ** 2 for x in range(10))

print(cuadrados)
print(cuadrados_set)
print(cuadrados_dict)
print(cuadrados_gen)
