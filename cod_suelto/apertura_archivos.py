import os

def renombrar():
    libro = input("Ingrese el nombre del libro a renombrar: ")
    nuevonombre = input("Ingrese el nuevo nombre del libro: ")
    ruta_original = f'{libro}.txt'
    nuevo_nombre = f'{nuevonombre}.txt'
    try:
        os.rename(ruta_original, nuevo_nombre)
        print(f"El archivo '{ruta_original}' ha sido renombrado como '{nuevo_nombre}'.")
    except FileNotFoundError:
        print(f"No se encontró el archivo '{ruta_original}'.")
    except FileExistsError:
        print(f"Ya existe un archivo con el nombre '{nuevo_nombre}'.")
    except Exception as e:
        print("Error al intentar renombrar el archivo:", e)

def leer():
    try:
        eleccion = input("Que libro quiere leer hoy: ")
        with open(f'{eleccion}.txt', 'r') as archivo:
            contenido = archivo.read()
            print(contenido)
    except FileNotFoundError:
        print("El archivo no se ha encontrado.")
    except Exception as e:
        print("Error:", e)

def crearyEscribir():
    try:
        nombre = input("Ingrese nombre de su libro: ")
        frase = input("Ingrese una frase motivacional: ")
        with open(f'{nombre}.txt', 'w') as archivo:
            archivo.write(f"{frase}")
            print("Se ha escrito en el archivo correctamente.")
    except Exception as e:
        print("Error:", e)

print(f"MENU \n \t 1-Crear y Escribir \n \t 2-Lectura \n \t 3-Renombrar \n \t 4-Salir")
while True:
    opcion = int(input("Ingrese opcion: "))
    if opcion == 1:
        crearyEscribir()
    elif opcion == 2:
        leer()
    elif opcion == 3:
        renombrar()
    elif opcion == 4:
        break
    else:
        print("Opcion Incorrecta")