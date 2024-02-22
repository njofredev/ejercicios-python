from random import randint


def deathNote(listaInicial, listaEliminados, listaActual):
    largoLista = len(listaActual)
    print(largoLista)
    print(len(listaActual))
    quienEsEliminado = listaActual[randint(0, largoLista -1)]
    indice = listaActual.index(quienEsEliminado)
    alumnoEliminado = listaActual.pop(indice)
    listaEliminados.append(alumnoEliminado)
    print("Lista Inicial", listaInicial)
    print(alumnoEliminado)
    print("Lista Eliminados", listaEliminados)
    print("Lista Actual", listaActual)
    return 

def bornNote(listaActual):
    nuevoAlumno = input("Ingrese el nombre del nuevo alumno: ")
    listaActual.append(nuevoAlumno)
    print(listaActual)
    return

def crearLista():
    listaInicial = []
    crearListaInicial = int(input("Ingrese el numero de la cantidad de Personas que quiere ingresar a su lista Inicial: "))

    for n in range(0, crearListaInicial):
        n = input(f"Ingrese el nombre {n + 1} de {crearListaInicial} : ")
        listaInicial.append(n)
    return listaInicial

def main():
        
    listaInicial = crearLista()
    listaEliminados = []
    listaActual = listaInicial.copy()

    while True:
        try:
            print("Opciones = Eliminar 1 / Agregar 2 / Salir 3")
            pregunta = int(input("Escoja una opcion: "))
            if pregunta == 1:
                deathNote(listaInicial, listaEliminados, listaActual)
            elif pregunta == 2:
                bornNote(listaActual)
            elif pregunta == 3:
                print("Hasta Luego")
                break
            else:
                print("Ingrese una opcion correcta")
        except ValueError:
            print("Ingrese un valor numerico")
