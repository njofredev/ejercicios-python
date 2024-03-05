# Uso de clases anidadas
class Auto:
    
    def __init__(self, marca):
        self.marca = marca

    class Motor:
        
        def __init__(self, cilindrada):
            self.cilindrada = cilindrada

        class Lubricante:
            
            def __init__(self, marca, viscosidad):
                self.marca = marca
                self.viscosidad = viscosidad

toyota = Auto("Yaris") # Se accede a la primera clase

modelo = toyota.Motor("1.5 L") # Se accede a la segunda clase

aceite = modelo.Lubricante("Mobil", "5w40") # Se accede a la tercera clase anidada

# Se imprimen todos los datos del acceso en cadena de las clases anidadas.
print(f"El auto es {toyota.marca}, el modelo es {modelo.cilindrada} y el aceite de marca: {aceite.marca} es {aceite.viscosidad}")






        
        