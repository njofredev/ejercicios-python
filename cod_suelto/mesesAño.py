"""
Cree una "Tupla" que contenga los nombres de los meses del año, se pueden ingresar
números al azar entre 1 y 12, si se ingresan fuera del rango, el programa
indica que se pueden ingresar solo entre 1 y 12 y continua su ejecución.
Según el número ingresado el programa imprimirá en pantalla el mes correspondiente:
Ej: "1" el mes es Enero, "12" el mes es Diciembre.

"""

# Tupla de meses
meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", 
         "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

salir = False
cont = 1

print ("\n")
print ("** Para salir del programa ingrese el número cero**")
while(not salir):

    numero = int(input("Ingrese un número entre 1 y 12 \n"))

    if(numero == 0):
        salir = True
    else:
        if (numero > 1 and numero <= len(meses)):
            print ("El mes es: ", meses[numero - 1])
            print("\n")
        else:
            print ("\n")
            print ("Ingrese solo números entre el 1 y el ", len(meses))
            print("\n")