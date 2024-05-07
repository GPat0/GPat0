import pygame
import random
import os

# Inicializar pygame
pygame.init()

# Definir colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Definir tamaño de la pantalla
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Definir la clase Carta
class Carta:
    def __init__(self, valor, imagen):
        self.valor = valor
        self.imagen = imagen
        self.rect = self.imagen.get_rect()
        self.volteada = False

    def voltear(self):
        self.volteada = not self.volteada

# Función para cargar las imágenes de las cartas
def cargar_imagenes():
    imagenes = []
    for filename in os.listdir("."):
        if filename.endswith(".PNG"):
            img_path = os.path.join(".", filename)
            print("Cargando imagen:", img_path)  # Mensaje de depuración
            imagen = pygame.image.load(img_path).convert()
            imagenes.append(imagen)
    return imagenes

# Función para crear el conjunto de cartas
def crear_cartas():
    imagenes = cargar_imagenes()
    print("Número de imágenes cargadas:", len(imagenes))  # Mensaje de depuración
    valores = list(range(len(imagenes))) * 2
    random.shuffle(valores)
    cartas = [Carta(valor, imagen) for valor, imagen in zip(valores, imagenes)]
    return cartas

# Función para dibujar las cartas en la pantalla
def dibujar_cartas(cartas, pantalla):
    for i, carta in enumerate(cartas):
        fila = i // 4
        columna = i % 4
        x = 50 + columna * 150
        y = 50 + fila * 150
        carta.rect.topleft = (x, y)
        if not carta.volteada:
            pygame.draw.rect(pantalla, GRAY, carta.rect)
        else:
            pantalla.blit(carta.imagen, carta.rect)

# Función para manejar los eventos del juego
def manejar_eventos(cartas):
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            # Voltear la carta si se hace clic en ella
            x, y = pygame.mouse.get_pos()
            for carta in cartas:
                if carta.rect.collidepoint(x, y):
                    carta.voltear()

# Función para verificar si todas las cartas están volteadas
def todas_volteadas(cartas):
    for carta in cartas:
        if not carta.volteada:
            return False
    return True

# Función principal del juego
def main():
    pantalla = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Memorama")

    cartas = crear_cartas()
    print("Número de cartas:", len(cartas))  # Mensaje de depuración

    reloj = pygame.time.Clock()

    while True:
        pantalla.fill(WHITE)

        # Dibujar las cartas en la pantalla
        dibujar_cartas(cartas, pantalla)

        # Manejar eventos del juego
        manejar_eventos(cartas)

        # Verificar si todas las cartas están volteadas
        if todas_volteadas(cartas):
            font = pygame.font.SysFont(None, 50)
            texto = font.render("¡Felicidades! Has ganado.", True, BLACK)
            pantalla.blit(texto, (SCREEN_WIDTH // 2 - texto.get_width() // 2, SCREEN_HEIGHT // 2 - texto.get_height() // 2))

        pygame.display.update()
        reloj.tick(60)

if __name__ == "__main__":
    main()

