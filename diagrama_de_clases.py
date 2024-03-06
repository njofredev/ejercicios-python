class Banco:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion

class Trabajador(Banco):
    def __init__(self, nombre, direccion, persona):
        super().__init__(nombre, direccion)
        self.persona = persona

    def obtener_datos(self):
        return f"El Trabajador {self.persona} es gerente del banco {self.nombre} ubicado en {self.direccion}"

class Sistemas(Banco):
    def __init__(self, nombre, direccion, sistemaOperativo):
        super().__init__(nombre, direccion)
        self.sistemaOperativo = sistemaOperativo

    def obtener_datosSistema(self):
        return f"El sistema usado en {self.nombre} es el sistema {self.sistemaOperativo}"

empleado1 = Trabajador("Santander", "Alameda 123", "Jannet")
print(empleado1.obtener_datos())

sistema1 = Sistemas("Banco Estado", "Alameda 321", "Linux")
print(sistema1.obtener_datosSistema())










