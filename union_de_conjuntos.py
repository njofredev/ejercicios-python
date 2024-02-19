"""
Clase 19-02-24
Listas, tuplas, diccionarios, set.

Listas tiene orden en un indice y puede ser modificada.
Tuplas no pueden ser modificadas
"""
# Se definen dos conjuntos de números
conjunto1 = {1,2,3,4,5}
conjunto2 = {4,5,6,7,8}

# Realizar operaciones de conjuntos
union = conjunto1.union(conjunto2)
intersection = conjunto1.intersection(conjunto2)
diferencia = conjunto1.difference(conjunto2)
diferencia2 = conjunto2.difference(conjunto1)

# Imprimir los resultados 
print(f"El conjunto 1 es {conjunto1}")
print(f"El conjunto 2 es {conjunto2}")
print(f"La unión de conjuntos es: {union}")
print(f"La intersección de los conjuntos es: {intersection}")
print(f"La diferencia entre el conjunto 1 y el conjunto 2 es: {diferencia}")
print(f"La diferencia entre el conjunto 2 y el conjunto 1 es: {diferencia2}")


