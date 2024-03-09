"""
Ejercicio grupal 2 - Trabajo grupal módulo 2
njofre

- Crear un programa que permita a una empresa de cine almacenar en su base de datos información sobre nuevas peliculas y estrenos. Cada pelicula se compone de: título, director, género y duración. Al final se debe mostrar la información detallada de cada película, lo que se debe crear la clase Pelicula y el Usuario encargado de agregar al menos 5 peliculas para después mostrarlas por pantalla.
"""

class Pelicula:
    
    def __init__(self, titulo, genero, duracion):
        self.titulo = titulo
        self.genero = genero
        self.duracion = duracion
        
    def get_datos_pelicula(self):
        print(f"La pelicula {self.titulo} del genero {self.genero} dura {self.duracion}")

catalogo_peliculas = [] # Contenedor de las peliculas
        
while True:
    print("***Bienvenido a gestor de peliculas*** \n")
    print("1. Ingrese una pelicula")
    print("2. Ver catalogo")
    print("3. Salir del programa \n")

    opcionMenu = int(input("Ingrese una opción del menú: \n"))
    
    if opcionMenu == 1:
        cantidad_peliculas = int(input("Ingrese la cantidad de peliculas a agregar: \n"))
        for i in range(cantidad_peliculas):
            titulo = input(f"Ingrese el título de la pelicula n°{i + 1}: ")
            genero = input(f"Ingrese el genero de la pelicula n°{i + 1}: ")
            duracion = input(f"Ingrese la duración de la pelicula n°{i + 1}: ")      
            # Instancias
            pelicula = Pelicula(titulo, genero, duracion)
            # Asignación a inventario
            catalogo_peliculas.append(pelicula)
            print("Pelicula ingresada correctamente! \n")
            
    elif opcionMenu == 2:
        
        for indice, pelicula in enumerate(catalogo_peliculas): # Recorre autos guardados y los muestra
            print(f"**Pelicula {indice + 1}**")
            pelicula.get_datos_pelicula()
            
    elif opcionMenu == 3:
        print("Gracias por participar del gestor de peliculas!")
        break
    else:
        print("Ingrese un valor correspondiente al menú")