"""
Clases en python
Usar variables Snake Case (_)
Leer sobre programación orientada a objeto (POO) asociarlo con py **

Objeto es una instancia de una clase.
Entidad que tiene características (atributos) y acciones (métodos)
por ejemplo: auto, persona, estudiante,  

"""

# definición de clase en python, pass para mantenerla activa

class Persona:
    # definición de atributos de la clase | __init__ constructor inicializador
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # definición de métodos (funciones definidas)
    def saludar(self):
        print(f"Hola mundo, me llamo {self.nombre} y tengo {self.edad} años.")

# crea la instancia de la clase
persona = Persona("Nicolas", 27)

# print(persona.nombre)
# print(persona.edad)
# llamado de método
# persona.saludar() 

"""
El paradigma de la programación orientada a objeto POO:

Enfoque de programación se basa en objetos
Los programas se diseñan pensando en que se representan entidades
del mundo real o conceptos abstractos tienen propiedades (atributos),
comportamientos y acciones (métodos) y pueden interactuar entre si
mediante mensajes.

La POO tiene 4 principios fundamentales:
- 1.Abstracción:
    - Proceso de identificar características de un objeto del mundo real,
    solo información relevante y ocultar detalles innecesarios.
    
- 2.Encapsulamiento:
    - Proceso de ocultar detalles de un objeto y exponer solo una interfaz pública
    que permita interactuar con el objeto.
    
- 3.Herencia:
    - Proceso que permite a las clases derivadas heredar atributos y métodos de una
    clase base (o super clase). Permite la creación de jerarquías de clases.
    
- 4.Polimorfismo:
    - Principio que permite a un objeto comportarse de diferentes formas según su
    contexto

La POO permite la modularidad, la reutilización de código, facilidad de mantenimiento
capacidad de modelar problemas de forma natural y estructurada.    
"""
# ejemplos de los 4 principios fundamentales de la POO

# Abstracción
class Vehiculo:
    def __init__(self, marca, modelo, estado):
        self.marca = marca
        self.modelo = modelo
        self.estado = estado
        
    def obtener_info(self):
        return f"Vehiculo: {self.marca} {self.modelo} está {self.estado}"
    
    def arrancar_auto(self):
        self.estado = True
        return f"El vehiculo: {self.marca} modelo: {self.modelo} se ha encendido "
    
    def detener_auto(self):
        self.estado = False
        return f"El vehiculo: {self.marca} modelo: {self.modelo} se ha apagado "
    
    def estado_auto(self):
        if self.estado == True:
            print("El auto está encendido en este momento :)")
        else:
            print("El auto se encuentra apagado en éste momento :(")
    
# Menu para el uso de la clase y sus métodos
"""while True:
    print("**Uso de auto**")
    print("1. Agregar vehiculos")
    print("2. Obtener información de vehiculos")
    print("3. Arrancar auto")
    print("4. Salir del auto")
    
    opcionMenu = int(input("Ingrese un valor del menú: "))
        """
    
# uso de clase Vehículo
autodeFernando = Vehiculo("Toyota", "Hillux", True)
coche2 = Vehiculo("Bmw", "mw-303", False)

print(autodeFernando.arrancar_auto())

print(autodeFernando.estado_auto())

print(coche2.detener_auto())

print(coche2.estado_auto())