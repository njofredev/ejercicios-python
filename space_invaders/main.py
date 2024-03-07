import pygame
import random

# Inicializar Pygame
pygame.init()

# Definir colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)

# Definir dimensiones de la pantalla
ANCHO = 800
ALTO = 600

# Definir la velocidad de movimiento del jugador y de los obstáculos
VELOCIDAD_JUGADOR = 5
VELOCIDAD_OBSTACULOS = 5
VELOCIDAD_CARRETERA = 5

# Clase para el jugador (auto)
class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(VERDE)
        self.rect = self.image.get_rect()
        self.rect.centerx = ANCHO // 2
        self.rect.bottom = ALTO - 50
        self.velocidad_x = 0

    def update(self):
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]:
            self.velocidad_x = -VELOCIDAD_JUGADOR
        elif teclas[pygame.K_RIGHT]:
            self.velocidad_x = VELOCIDAD_JUGADOR
        else:
            self.velocidad_x = 0
        self.rect.x += self.velocidad_x
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > ANCHO:
            self.rect.right = ANCHO

# Clase para los obstáculos
class Obstaculo(pygame.sprite.Sprite):
    def __init__(self, size):
        super().__init__()
        if size == "small":
            self.image = pygame.Surface((20, 20))
        else:
            self.image = pygame.Surface((40, 40))
        self.image.fill(ROJO)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, ANCHO - self.rect.width)
        self.rect.y = random.randrange(-100, -40)

    def update(self):
        self.rect.y += VELOCIDAD_OBSTACULOS
        if self.rect.top > ALTO:
            self.rect.x = random.randrange(0, ANCHO - self.rect.width)
            self.rect.y = random.randrange(-100, -40)

# Clase para el mapa de carretera
class Carretera(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((ANCHO, ALTO * 2))
        self.image.fill(NEGRO)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = -ALTO

    def update(self):
        self.rect.y += VELOCIDAD_CARRETERA
        if self.rect.top >= 0:
            self.rect.y = -ALTO

# Inicializar pantalla
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Hot Rod")

# Reloj
reloj = pygame.time.Clock()

# Crear sprites
jugador = Jugador()
todos_los_sprites = pygame.sprite.Group()
todos_los_sprites.add(jugador)
obstaculos = pygame.sprite.Group()
carretera = Carretera()
todos_los_sprites.add(carretera)
for _ in range(10):
    obstaculo = Obstaculo(random.choice(["small", "large"]))
    todos_los_sprites.add(obstaculo)
    obstaculos.add(obstaculo)

# Bucle principal
corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    # Actualizar sprites
    todos_los_sprites.update()

    # Colisiones entre el jugador y los obstáculos
    colisiones = pygame.sprite.spritecollide(jugador, obstaculos, False)
    if colisiones:
        print("¡Has chocado!")
        corriendo = False

    # Limpiar pantalla
    pantalla.fill(NEGRO)

    # Dibujar sprites
    todos_los_sprites.draw(pantalla)

    # Dibujar mapa de carretera
    pantalla.blit(carretera.image, carretera.rect)

    # Actualizar pantalla
    pygame.display.flip()

    # Controlar velocidad de cuadros por segundo
    reloj.tick(60)

pygame.quit()
