import pygame
import random

pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

playerImg = pygame.image.load("spaceship_64x64.png")
enemyImg = pygame.image.load("2_resized_64x64.png")
icon = pygame.image.load("spaceship.png")
background = pygame.image.load("bing_resized_800x600.png")
pygame.display.set_caption("Space Invaders")
pygame.display.set_icon(icon)

px = 370
py = 480
ex = random.randint(0, SCREEN_WIDTH - 64)
ey = random.randint(50, 150)

# Score
score_value = 0
font = pygame.font.Font(None, 36)

def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y):
    screen.blit(enemyImg, (x, y))

last_move_time = pygame.time.get_ticks()

run = True
while run:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        px -= 3
    if keys[pygame.K_d]:
        px += 3

    if px < 0:
        px = 0
    if px > SCREEN_WIDTH - 64:
        px = SCREEN_WIDTH - 64

    current_time = pygame.time.get_ticks()
    if current_time - last_move_time > 2000:
        ex = random.randint(0, SCREEN_WIDTH - 64)
        ey = random.randint(50, 150)
        last_move_time = current_time
        score_value += 1  

    player(px, py)
    enemy(ex, ey)
    show_score(10, 10)

    pygame.display.update()
