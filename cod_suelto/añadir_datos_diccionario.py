alumnos = {}

while True:
    pregunta = input("Desea ingresar un datos? SI/NO")
    if pregunta.lower() == "si":
        nombre = input("Ingrese un nombre: ")
        edad = int(input("Ingrese la edad: "))
        alumnos[nombre] = edad
    elif pregunta == "no":
        print(f"Estos son los alumnos del curso Python mañana: {alumnos}")
        break
    else:
        print("Ingrese una opción válida")