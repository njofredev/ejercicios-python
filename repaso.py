"""
Repaso 27-02-24

Variables: Espacio de memoria que pueden almacenar información str, int, list, tupla, set, diccionario
a = 5 / Se le asigna a "a" el valor númerico de "5"

Ciclos: ciclo for, while, uso de break y continue

Tipos de datos:
    - Lista[] : es mutable y tiene index
    - Tupla() : es inmutable y tiene index
    - Diccionario{"k":"v"}: tiene key,value y puede ser recorrido por su index
    - Set(): Conjunto 
"""

# Uso de funciones:

def funcion (a,b):
    perrito = a + b
    gatito = b-a

    return (perrito, gatito)

gatito = funcion(5,6)

print(gatito)