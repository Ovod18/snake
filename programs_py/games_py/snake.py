import pygame
import random

DISPLAY_WIDTH = 360
DISPLAY_HEIGHT = 480
FPS = 20
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
SNAKE_WIDTH = 10

"""Creating the main window."""
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((DISPLAY_WIDTH,
                                  DISPLAY_HEIGHT))
pygame.display.set_caption("My snake")

clock = pygame.time.Clock()

"""Setting the coordinates of snake."""
x1 = DISPLAY_WIDTH  / 2
y1 = DISPLAY_HEIGHT / 2
x1_change = 0
y1_change = 0

"""Drowing the start screen and the snake."""
screen.fill(BLACK)
pygame.draw.rect(screen, GREEN, [x1, y1,
                 SNAKE_WIDTH, SNAKE_WIDTH])
pygame.display.update()

""" Creating the game cycle."""
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            x1_change = -10
            y1_change = 0
        elif event.key == pygame.K_RIGHT:
            x1_change = 10
            y1_change = 0
        elif event.key == pygame.K_UP:
            y1_change = -10
            x1_change = 0
        elif event.key == pygame.K_DOWN:
            y1_change = 10
            x1_change = 0

    if ((x1 >= DISPLAY_WIDTH) or (x1 < 0) or
           (y1 >= DISPLAY_HEIGHT) or
           (y1 < 0)):
        running = False

    x1 += x1_change
    y1 += y1_change

"""Rendering and updating the screen"""
    screen.fill(BLACK)
    pygame.draw.rect(screen, GREEN, [x1, y1,
                     SNAKE_WIDTH, SNAKE_WIDTH])

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
quit()
