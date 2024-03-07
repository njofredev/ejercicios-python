class Regiones:
    def __init__(self, nombre, numero):
        self.nombre = nombre
        self.numero = numero

class Ciudades(Regiones):
    def __init__(self, nombre, numero, ciudad):
        super().__init__(nombre, numero)
        self.ciudad = ciudad

    def get_ciudad(self):
        return f"La ciudad {self.ciudad} es la mas importante de la region {self.nombre}"

regiones = []
ciudades = []

num_regiones = int(input("Cuantas regiones desea registrar: "))

for i in range(num_regiones):
    nombreR = input(f"Ingrese el nombre de la region {i + 1} de {num_regiones} :")
    numeroR = input(f"Ingrese el numero corresondiente a la region {nombreR}: ")
    region = Regiones(nombreR, numeroR)
    nombreC = input(f"Ingrese nombre de la ciudad mas importante de la region de {nombreR}: ")
    ciudadR = Ciudades(nombreR, numeroR, nombreC)
    regiones.append(region)
    ciudades.append(ciudadR.get_ciudad())

for r in regiones:
    print(f"La region {r.nombre} corresponde al numero {r.numero}")
    
for c in ciudades:
    print(c)