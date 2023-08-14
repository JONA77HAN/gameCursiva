
import pygame
import random

# Inicialización de Pygame
pygame.init()

# Dimensiones de la pantalla
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Creación de la pantalla
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Las Cursivas")

# Colores
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)

# Clase para representar al jugador
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./img/LEON_player.jpg")
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = SCREEN_HEIGHT - self.rect.height
        self.speed_x = 5
        self.speed_y = 5
        self.lives = 3

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed_x
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed_x
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed_y
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed_y

    def draw(self):
        screen.blit(self.image, self.rect)

    def lose_life(self):
        self.lives -= 1

# Clase para representar la pelotita
class Ball(pygame.sprite.Sprite):
    def __init__(self, color):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        pygame.draw.circle(self.image, color, (10, 10), 10)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(0, SCREEN_HEIGHT - self.rect.height)
        self.speed_x = random.choice([-2, 2])
        self.speed_y = random.choice([-2, 2])

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.left < 0 or self.rect.right > SCREEN_WIDTH:
            self.speed_x *= -1
        if self.rect.top < 0 or self.rect.bottom > SCREEN_HEIGHT:
            self.speed_y *= -1

    def draw(self):
        screen.blit(self.image, self.rect)

# Grupo de sprites
all_sprites = pygame.sprite.Group()
player = Player()
balls = [Ball(RED), Ball(GREEN), Ball(BLUE), Ball(YELLOW), Ball(PURPLE), Ball(ORANGE)]
all_sprites.add(player, *balls)

# Fuentes de texto
font = pygame.font.Font(None, 36)

# Bucle principal del juego
running = True
clock = pygame.time.Clock()
start_ticks = pygame.time.get_ticks()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

    # Comprobar colisiones
    for ball in balls:
        if pygame.sprite.collide_rect(player, ball):
            player.lose_life()
            if player.lives == 0:
                game_over_text = font.render("Game Over", True, WHITE)
                game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
                screen.blit(game_over_text, game_over_rect)
                running = False
            else:
                ball.rect.x = random.randint(0, SCREEN_WIDTH - ball.rect.width)
                ball.rect.y = random.randint(0, SCREEN_HEIGHT - ball.rect.height)

    # Fondo de pantalla
    screen.fill((0, 0, 0))

    all_sprites.draw(screen)

    # Temporizador
    seconds = (pygame.time.get_ticks() - start_ticks) // 1000
    timer_text = font.render(f"Tiempo: {seconds}", True, WHITE)
    screen.blit(timer_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

# Finalización de Pygame
pygame.quit()
"""

import pygame
import random

# Inicialización de Pygame
pygame.init()

# Dimensiones de la pantalla
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Creación de la pantalla
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Las Cursivas")

# Colores
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)

# Clase para representar al jugador
class Player(pygame.sprite.Sprite):
    # ... (código anterior)

# Clase para representar la pelotita
class Ball(pygame.sprite.Sprite):
    # ... (código anterior)

# Clase para representar una vida (corazón)
class Heart(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("./img/heart.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        screen.blit(self.image, self.rect)

# ... (código anterior)

# Grupo de sprites
all_sprites = pygame.sprite.Group()
player = Player()
balls = [Ball(RED), Ball(GREEN), Ball(BLUE), Ball(YELLOW), Ball(PURPLE), Ball(ORANGE)]
all_sprites.add(player, *balls)

# Grupo de corazones
hearts_group = pygame.sprite.Group()

# Crear corazones
heart_positions = [(10 + i * 30, 10) for i in range(player.lives)]
hearts = [Heart(x, y) for x, y in heart_positions]
hearts_group.add(hearts)

# Fuentes de texto
font = pygame.font.Font(None, 36)

# Bucle principal del juego
running = True
clock = pygame.time.Clock()
start_ticks = pygame.time.get_ticks()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

    # ... (código anterior)

    # Fondo de pantalla
    screen.fill((0, 0, 0))

    all_sprites.draw(screen)
    hearts_group.draw(screen)  # Dibujar corazones en la pantalla

    # Temporizador
    seconds = (pygame.time.get_ticks() - start_ticks) // 1000
    timer_text = font.render(f"Tiempo: {seconds}", True, WHITE)
    screen.blit(timer_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

# Finalización de Pygame
pygame.quit()

"""