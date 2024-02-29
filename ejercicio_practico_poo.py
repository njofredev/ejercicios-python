"""
Ejercicio práctico - Lección 2 n°1
njofre

- Crear una clase Persona
    - Atributos: nombre, edad, altura
    - Métodos: get_nombre(), set_nombre(nombre), get_edad(), 
               set_edad(edad), get_altura(), set_altura(altura)

- Crear una instancia con los siguientes datos: 
    persona = Persona ("Juan Pérez", 30, 1.75)
"""
class Persona:
    # Constructor con atributos
    def __init__ (self, nombre, edad, altura):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
    
    # Métodos
    def get_nombre(self):
        print(f"El nombre del usuario es: {self.nombre}")
    
    def set_nombre(self): # Definición de SET,
        nombre_usuario = str(input("Ingrese el nombre del usuario: "))
        self.nombre = nombre_usuario
        print(f"El nuevo nombre del usuario es: {nombre_usuario}")

    def get_edad(self):
        print(f"La edad del usuario es: {self.edad}")

    def set_edad(self):
        edad_usuario = int(input("Ingrese la edad del usuario"))
        self.edad = edad_usuario
        print(f"El usuario tiene: {edad_usuario}")

    def get_altura(self):
        print(f"La altura del usuario es: {self.altura}")

    def set_altura(self):
        altura_usuario = float(input("Ingrese una nueva altura para el usuario: "))
        self.altura = altura_usuario
        print(f"El usuario tiene {altura_usuario}")

# Instancia de la clase 'Persona'
persona = Persona("Juan pérez", 30, 1.75)

# Llamado de métodos con menú

while True:
    print("Bienvenido a gestor de nombres \n")
    print("1. Mostrar nombre de usuario")
    print("2. Modificar nombre de usuario")
    print("3. Mostrar edad de usuario")
    print("4. Modificar edad de usuario")
    print("5. Mostrar altura de usuario")
    print("6. Modificar altura de usuario")
    print("7. Salir del programa")

    opcionMenu = int(input("Ingrese una opción del menú: \n"))

    if opcionMenu == 1:
        persona.get_nombre()
    elif opcionMenu == 2:
        persona.set_nombre()
    elif opcionMenu == 3:
        persona.get_edad()
    elif opcionMenu == 4:
        persona.set_edad()
    elif opcionMenu == 5:
        persona.get_altura()
    elif opcionMenu == 6:
        persona.set_altura()
    elif opcionMenu == 7:
        print("Gracias por participar del gestor de Usuario!")
        break
    else:
        print("Ingrese un valor correspondiente al menú")
