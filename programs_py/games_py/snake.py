import pygame
import random
import time

DISPLAY_WIDTH = 480
DISPLAY_HEIGHT = 800
X_CENTRE = DISPLAY_WIDTH / 2
Y_CENTRE = DISPLAY_HEIGHT / 2
FPS = 5
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
SNAKE_WIDTH = 10

"""Creating the main window."""
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("My snake")

clock = pygame.time.Clock()

"""Setting the coordinates of snake."""
snake_x = X_CENTRE
snake_y = Y_CENTRE
snake_x_change = 0
snake_y_change = 0
snake_body_x = [snake_x]
snake_body_y = [snake_y]
food_x = random.randrange(0, DISPLAY_WIDTH, SNAKE_WIDTH)
food_y = random.randrange(0, DISPLAY_HEIGHT, SNAKE_WIDTH)

"""Setting other values"""
score = 0
course = ""



""" Creating the game cycle."""
running = True
while running:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            running = False

    if event.type == pygame.KEYDOWN:
        if (event.key==pygame.K_LEFT) and (course!="RIGHT"):
            snake_x_change = -10
            snake_y_change = 0
            course = "LEFT"
        elif (event.key==pygame.K_RIGHT) and (course!="LEFT"):
            snake_x_change = 10
            snake_y_change = 0
            course = "RIGHT"
        elif (event.key==pygame.K_UP) and (course!="DOWN"):
            snake_y_change = -10
            snake_x_change = 0
            course = "UP"
        elif (event.key==pygame.K_DOWN) and (course!="UP"):
            snake_y_change = 10
            snake_x_change = 0
            course = "DOWN"
        elif event.key == pygame.K_ESCAPE:
            running = False

    if ((snake_x >= DISPLAY_WIDTH) or (snake_x < 0) or
           (snake_y >= DISPLAY_HEIGHT) or
           (snake_y < 0)):
         font = pygame.font.Font(None, 65)
         text = "WASTED"
         message = font.render(text, True, RED)
         screen.blit(message, [X_CENTRE, Y_CENTRE])
         pygame.display.update()
         time.sleep(5)
         running = False

    snake_x += snake_x_change
    snake_y += snake_y_change

    if (snake_x==food_x) and (snake_y==food_y):
        food_x = random.randrange(0, DISPLAY_WIDTH, SNAKE_WIDTH)
        food_y = random.randrange(0, DISPLAY_HEIGHT, SNAKE_WIDTH)
        score = score + 1
        snake_body_x.append(snake_x)
        snake_body_y.append(snake_y)

    screen.fill(BLACK)

    font = pygame.font.Font(None, 30)
    text = "Your score: " + str(score) + " Course: " + course
    message = font.render(text, True, YELLOW)
    screen.blit(message, [10, 10])

    pygame.draw.rect(screen, GREEN, [snake_x, snake_y,
                SNAKE_WIDTH, SNAKE_WIDTH])

    pygame.draw.rect(screen, RED, [food_x, food_y,
                     SNAKE_WIDTH, SNAKE_WIDTH])

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
quit()
