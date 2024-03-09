class Pichanga:

    def __init__(self, jugador, equipo, numeroCamiseta):

        self.jugador = jugador
        self.equipo = equipo
        self.numeroCamiseta = numeroCamiseta

    def crearEquipo(self):
        print("el nombre del jugador es", self.jugador, "pertenece al equipo", self.equipo, "su numero es:", self.numeroCamiseta )

    class Partido:
        def __init__(self, nombre):
            self.nombre = nombre

        def jugando(self, jugadorRival):
            return print(f"el {self.nombre} tapa el tiro de {jugadorRival.jugador}, que es del equipo {jugadorRival.equipo}")
    

jugador1 = Pichanga("Fernando", "mañana", "1")
jugador2 = Pichanga("Felipe", "mañana", "2")

jugador3 = Pichanga("Luigi", "tarde", "3")


jugador1.crearEquipo()
jugador2.crearEquipo()
jugador3.crearEquipo()

jugador1.Partido("Primera ronda").jugando(jugador3)
