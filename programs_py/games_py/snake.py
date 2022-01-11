import pygame
import random

WIDTH = 360
HEIGHT = 480
FPS = 30                                              # setting the FPS
WHITE = (255, 255, 255)                               # setting the colors 
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.init()                                         # creating the main window
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My snake")
clock = pygame.time.Clock()


x1 = 300                                              # setting the coordinates 
y1 = 300                                              # of snake
x1_change = 0                                         # setting the values of 
y1_change = 0                                         # the coordinates change


screen.fill(WHITE)                                    # paint the display 
                                                      # in WHITE
pygame.draw.rect(screen, BLUE, [x1, y1, 10, 10])      # draw the snake
                                                      # in x1, y1 coordinates
pygame.display.update()                               # update the display


running = True                                        # creating a game cycle
while running:
    for event in pygame.event.get():                  # check for closing window
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

    x1 += x1_change
    y1 += y1_change

    screen.fill(WHITE)                                # paint the display 
                                                      # in WHITE
    pygame.draw.rect(screen, BLUE, [x1, y1, 10, 10])

    pygame.display.update()                           # update the display
    clock.tick(FPS) 


pygame.quit()
quit()
