# Las clases pueden estar anidadas
class Musica: 

    def __init__(self, nombre):
        self.nombre = nombre

    class Estilos:
        def __init__(self, estilo, fecha):
            self.estilo = estilo
            self.fecha = fecha

# Música
musica = Musica("Música")
# Estilos
rock = musica.Estilos("Rock", 1900)
jazz = musica.Estilos("Jazz", 1800)

print(f"El nombre de la música es: ")