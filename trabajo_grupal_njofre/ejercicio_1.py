"""
Ejercicio grupal 1 - Trabajo grupal módulo 2
njofre

- Crear clase automóvil, se puede agregar color a automovil, marca, modelo, número de puertas y la patente. Crear constructor y así los métodos que encuentre necesarios. Se deben crear 5 instancias donde el usuario ingrese -manualmente- la información de estos vehículos para que sean agregados al inventario e imprimirlos en pantalla.
"""

class Automovil:
    
    def __init__(self, marca, modelo, color, num_puertas, patente):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.num_puertas = num_puertas
        self.patente = patente
        
    def get_datos_auto(self):
        print(f"El auto marca {self.marca}, modelo {self.modelo}, color {self.color}, tiene {self.num_puertas} puertas y su patente es: {self.patente}")

inventario = [] # Contenedor de los autos
        
while True:
    print("***Bienvenido a gestor de vehículo*** \n")
    print("1. Ingresar 5 vehículos")
    print("2. Ver inventario")
    print("3. Salir del programa \n")

    opcionMenu = int(input("Ingrese una opción del menú: \n"))
    
    if opcionMenu == 1:
        
        for i in range(5):
            marca = input(f"Ingrese la marca del automóvil {i + 1}: ")
            modelo = input(f"Ingrese el modelo del automóvil {i + 1}: ")
            color = input(f"Ingrese el color del automóvil {i + 1}: ")
            num_puertas = int(input(f"Ingrese el número de puertas del automóvil {i + 1}: "))
            patente = input(f"Ingrese la patente del automóvil {i + 1}: ")      
            # Instancias
            auto = Automovil(marca, modelo, color, num_puertas, patente)
            # Asignación a inventario
            inventario.append(auto)
            print("Auto ingresado correctamente! \n")
            
    elif opcionMenu == 2:
        
        for indice, auto in enumerate(inventario): # Recorre autos guardados y los muestra
            print(f"--Vehiculo {indice + 1}--")
            auto.get_datos_auto()
            
    elif opcionMenu == 3:
        print("Gracias por participar del gestor vehículos!")
        break
    else:
        print("Ingrese un valor correspondiente al menú")
