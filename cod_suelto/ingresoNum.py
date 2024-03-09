"""
Crear un programa en Python que solicite al usuario por pantalla ingresar un número
y se debe almacenar la tabla de multiplicar hasta el 10 en una lista e imprimirla.
Usar "For"

Ej: El usuario ingresa el num 5 y se debe imprimir la lista con la tabla
"5"(5,10,15,20,25,30,35,40,45,50)
"""

# Se transforma el "input" str en int y se asigna a variable "numero"
numero = int(input("Ingrese un número: "))

# Se inicializa una lista vacía para almacenar datos
lista = []

for i in range(1,11):
    # Append agrega cada resultado a la lista vacía
    lista.append (i * numero)

print("La tabla del número ", numero, "es: ",lista)