"""
Día 1 - Lección 4
- Herencia y polimorfismo -
"""

class Abuelo:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def familia():
        return print("Esta es la familia Castillo")
    
    def presentacion(self):
        return print(f"yo soy el tata {tataEduardo.nombre} {tataEduardo.apellido}")

class Padre(Abuelo):
    def __init__(self, nombreP, abuelo):
        super().__init__(abuelo.nombre, abuelo.apellido)
        self.nombreP = nombreP

    def presentacion(self):
        return print(f"yo soy el papa de {hijoJeff.nombreH} {hijoJeff.apellido} mi nombre es {papiFelipe.nombreP} {papiFelipe.apellido}")

class Hija(Padre):
    def __init__(self, nombreH, padre):
        super().__init__(nombreH, padre)
        self.nombreH = nombreH


    def presentacion(self):
        return print(f"yo soy {hijoJeff.nombreH} {hijoJeff.apellido} hijo de {papiFelipe.nombreP} {papiFelipe.apellido} nieto de {tataEduardo.nombre} {tataEduardo.apellido}")

#Objetos Herencia
tataEduardo = Abuelo("Eduardo", "Castillo")
papiFelipe = Padre("Felipe", tataEduardo)
hijoJeff = Hija("Jeff", papiFelipe)

#metodo Polimorfismo
tataEduardo.presentacion()
papiFelipe.presentacion()
hijoJeff.presentacion()