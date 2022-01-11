import pygame
import random
import time

DISPLAY_WIDTH = 1024
DISPLAY_HEIGHT = 1280
X_CENTRE = DISPLAY_WIDTH / 2
Y_CENTRE = DISPLAY_HEIGHT / 2
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

"""Creating font and text"""
font = pygame.font.Font(None, 65)
text = "My text"
message = font.render(text, True, RED)

"""Setting the coordinates of snake."""

snake_x = X_CENTRE
snake_y = Y_CENTRE
snake_x_change = 0
snake_y_change = 0

"""Drowing the start screen and the snake."""
screen.fill(BLACK)
pygame.draw.rect(screen, GREEN, [snake_x, snake_y,
                 SNAKE_WIDTH, SNAKE_WIDTH])
pygame.display.update()

""" Creating the game cycle."""
running = True
while running:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            running = False

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            snake_x_change = -10
            snake_y_change = 0
        elif event.key == pygame.K_RIGHT:
            snake_x_change = 10
            snake_y_change = 0
        elif event.key == pygame.K_UP:
            snake_y_change = -10
            snake_x_change = 0
        elif event.key == pygame.K_DOWN:
            snake_y_change = 10
            snake_x_change = 0
        elif event.key == pygame.K_ESCAPE:
            running = False

    if ((snake_x >= DISPLAY_WIDTH) or (snake_x < 0) or
           (snake_y >= DISPLAY_HEIGHT) or
           (snake_y < 0)):
         text = "WASTED"
         message = font.render(text, True, RED)
         screen.blit(message, [X_CENTRE, Y_CENTRE])
         pygame.display.update()
         time.sleep(5)
         running = False

    snake_x += snake_x_change
    snake_y += snake_y_change

    screen.fill(BLACK)
    pygame.draw.rect(screen, GREEN, [snake_x, snake_y,
                     SNAKE_WIDTH, SNAKE_WIDTH])

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
quit()
