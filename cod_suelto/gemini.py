import pygame
import random

# Inicializar Pygame
pygame.init()

# Configurar pantalla
ancho = 800
alto = 600
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Juego de la Serpiente")

# Colores
blanco = (255, 255, 255)
negro = (0, 0, 0)
verde = (0, 255, 0)
rojo = (255, 0, 0)

# Variables
posicion_x = ancho // 2
posicion_y = alto // 2
direccion = "DERECHA"
longitud = 1
serpiente = [[posicion_x, posicion_y]]
comida_x = random.randint(0, ancho - 10)
comida_y = random.randint(0, alto - 10)
hecho = False
reloj = pygame.time.Clock()
fps = 15


# Funciones
def dibujar_serpiente():
    for segmento in serpiente:
        pygame.draw.rect(pantalla, verde, pygame.Rect(segmento[0], segmento[1], 10, 10))


def generar_comida():
    global comida_x, comida_y
    comida_x = random.randint(0, ancho - 10)
    comida_y = random.randint(0, alto - 10)


def verificar_colision():
    return serpiente[0][0] == comida_x and serpiente[0][1] == comida_y


def aumentar_longitud():
    global longitud
    serpiente.append([posicion_x, posicion_y])


# Bucle principal del juego
while not hecho:
    # Manejo de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            hecho = True

    # Teclas de control
    teclas_presionadas = pygame.key.get_pressed()
    if teclas_presionadas[pygame.K_RIGHT] and direccion != "IZQUIERDA":
        direccion = "DERECHA"
    if teclas_presionadas[pygame.K_UP] and direccion != "ABAJO":
        direccion = "ARRIBA"
    if teclas_presionadas[pygame.K_LEFT] and direccion != "DERECHA":
        direccion = "IZQUIERDA"
    if teclas_presionadas[pygame.K_DOWN] and direccion != "ARRIBA":
        direccion = "ABAJO"

    # Actualización de la posición de la serpiente
    if direccion == "DERECHA":
        posicion_x += 1
    if direccion == "ARRIBA":
        posicion_y -= 1
    if direccion == "IZQUIERDA":
        posicion_x -= 1
    if direccion == "ABAJO":
        posicion_y += 1

    # Limitar la serpiente dentro de la pantalla
    posicion_x %= ancho
    posicion_y %= alto

    # Verificar colisión con la comida
    if verificar_colision():
        generar_comida()
        aumentar_longitud()

    # Eliminar la cola de la serpiente si no hay colisión
    if len(serpiente) > longitud:
        del serpiente[0]

    # Verificar colisión con el cuerpo de la serpiente
    for segmento in serpiente[:-1]:
        if segmento[0] == posicion_x and segmento[1] == posicion_y:
            hecho = True

    # Rellenar la pantalla con negro
    pantalla.fill(negro)

    # Dibujar la serpiente
    dibujar_serpiente()

    # Dibujar la comida
    pygame.draw.rect(pantalla, rojo, pygame.Rect(comida_x, comida_y, 10, 10))

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar la velocidad del juego
    reloj.tick(fps)

# Finalizar Pygame
pygame.quit()
