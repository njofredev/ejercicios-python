# Clase
class Persona:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def saludar(self):
        return f"Hola!, me llamo {self.nombre} {self.apellido}"


# Instancia
persona1 = Persona("Nicolás", "         Jofré")

print(persona1.saludar())
print(1 + 1)
