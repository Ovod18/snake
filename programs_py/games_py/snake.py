import pygame
import random

DISPLAY_WIDTH = 360
DISPLAY_HEIGHT = 480
FPS = 20                                           # setting the FPS
WHITE = (255, 255, 255)                             # setting the colors 
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
SNAKE_WIDTH = 10

pygame.init()                                       # creating the main window
pygame.mixer.init()
screen = pygame.display.set_mode((DISPLAY_WIDTH, 
                                  DISPLAY_HEIGHT))
pygame.display.set_caption("My snake")
clock = pygame.time.Clock()

x1 = DISPLAY_WIDTH  / 2                             # Setting the coordinates 
y1 = DISPLAY_HEIGHT / 2                             # of snake.  
x1_change = 0                                       # Setting the values of 
y1_change = 0                                       # the coordinates change.


screen.fill(BLACK)                                  # Paint the display  
                                                    # in BLACK. 
pygame.draw.rect(screen, GREEN, [x1, y1,
                 SNAKE_WIDTH, SNAKE_WIDTH])     
                                                    # Draw the snake
                                                    # in x1, y1 coordinates.
pygame.display.update()                             # Update the display.

running = True                                      # Creating the game cycle.
while running:
    for event in pygame.event.get():                # Check for closing window.
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

    screen.fill(BLACK)                              # Paint the display
                                                    # in BLACK.
    pygame.draw.rect(screen, GREEN, [x1, y1,
                     SNAKE_WIDTH, SNAKE_WIDTH])

    pygame.display.update()                         # Update the display.
    clock.tick(FPS) 

pygame.quit()
quit()
