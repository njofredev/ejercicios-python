try:
    with open ("archivo.txt", "r") as archivo:
        contenido = archivo.read()
        print(contenido)
except FileNotFoundError: # Función de error desde Python
    print("El archivo no se ha encontrado.")
except Exception as e:
    print("Error: ", e)