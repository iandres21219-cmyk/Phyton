import pygame
import random

# Inicialitzar pygame
pygame.init()

# Definir les mides de la pantalla
ample = 800
alt = 600
pantalla = pygame.display.set_mode((ample, alt))
pygame.display.set_caption("Arkanoid")

# Colors
blanc = (255, 255, 255)
negro = (0, 0, 0)
vermell = (255, 0, 0)

# Carregar imatges
raqueta_img = pygame.image.load('/home/iker/AO/Python/raqueta.png')
pelota_img = pygame.image.load('/home/iker/AO/Python/pelota.png')
ladrillos_img = pygame.image.load('/home/iker/AO/Python/ladrillos.png')

# Mida de la paleta
paleta_amplada = 100
paleta_alçada = 20
paleta_x = ample // 2 - paleta_amplada // 2
paleta_y = alt - paleta_alçada - 10

# Posició de la pilota
pilota_x = ample // 2
pilota_y = alt // 2
pilota_velocitat_x = 3
pilota_velocitat_y = -3
pilota_diameter = 20

# Crear blocs
bloc_amplada = 60
bloc_alçada = 30
blocs = []

def crear_blocs():
    for i in range(5):  # 5 files de blocs
        for j in range(10):  # 10 blocs per cada fila
            bloc = pygame.Rect(j * (bloc_amplada + 5) + 50, i * (bloc_alçada + 5) + 50, bloc_amplada, bloc_alçada)
            blocs.append(bloc)

# Funció per dibuixar la paleta
def dibuixar_paleta():
    pantalla.blit(paleta_img, (paleta_x, paleta_y))

# Funció per dibuixar la pilota
def dibuixar_pilota():
    pantalla.blit(pilota_img, (pilota_x - pilota_diameter // 2, pilota_y - pilota_diameter // 2))

# Funció per dibuixar els blocs
def dibuixar_blocs():
    for bloc in blocs:
        pantalla.blit(bloc_img, bloc)

# Funció per controlar els esdeveniments
def controlar_esdeveniments():
    global paleta_x, pilota_velocitat_x, pilota_velocitat_y, pilota_x, pilota_y
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paleta_x > 0:
        paleta_x -= 10
    if keys[pygame.K_RIGHT] and paleta_x < ample - paleta_amplada:
        paleta_x += 10
    return True

# Funció per actualitzar la posició de la pilota
def moure_pilota():
    global pilota_x, pilota_y, pilota_velocitat_x, pilota_velocitat_y, blocs
    pilota_x += pilota_velocitat_x
    pilota_y += pilota_velocitat_y

    # Col·lisions amb les parets
    if pilota_x <= 0 or pilota_x >= ample:
        pilota_velocitat_x *= -1
    if pilota_y <= 0:
        pilota_velocitat_y *= -1

    # Col·lisions amb la paleta
    if pilota_y + pilota_diameter >= paleta_y and paleta_x <= pilota_x <= paleta_x + paleta_amplada:
        pilota_velocitat_y *= -1

    # Col·lisions amb els blocs
    for bloc in blocs[:]:
        if bloc.collidepoint(pilota_x, pilota_y):
            pilota_velocitat_y *= -1
            blocs.remove(bloc)
    
# Funció per inicialitzar el joc
def joc():
    global paleta_x, paleta_y, pilota_x, pilota_y, pilota_velocitat_x, pilota_velocitat_y, blocs

    crear_blocs()
    joc_actiu = True
    while joc_actiu:
        pantalla.fill(negro)
        joc_actiu = controlar_esdeveniments()

        # Actualitzar posició de la pilota
        moure_pilota()

        # Dibuixar elements
        dibuixar_paleta()
        dibuixar_pilota()
        dibuixar_blocs()

        # Actualitzar la pantalla
        pygame.display.update()

        # Condició per acabar el joc
        if pilota_y > alt:
            print("Has perdut!")
            joc_actiu = False

        # Limitant la velocitat de la pantalla
        pygame.time.delay(10)

    pygame.quit()

# Iniciar el joc amb la barra espaiadora
while True:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        joc()
        break
