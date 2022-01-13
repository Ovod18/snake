import pygame
import random
import time

DISPLAY_WIDTH = 360
DISPLAY_HEIGHT = 360
X_CENTRE = DISPLAY_WIDTH / 2
Y_CENTRE = DISPLAY_HEIGHT / 2
FPS = 10
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
snake_x_change = 0
snake_y_change = 0
snake_body_x = [X_CENTRE]
snake_body_y = [Y_CENTRE]
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

    """Setting the course of movement."""
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

    """Wasted"""
    if ((snake_body_x[0] >= DISPLAY_WIDTH) or (snake_body_x[0] < 0) or
           (snake_body_y[0] >= DISPLAY_HEIGHT) or
           (snake_body_y[0] < 0)):
         font = pygame.font.Font(None, 65)
         text = "WASTED"
         message = font.render(text, True, RED)
         screen.blit(message, [X_CENTRE, Y_CENTRE])
         pygame.display.update()
         time.sleep(5)
         running = False

    """The snake is growing."""
    iterator = len(snake_body_x) - 1
    while(iterator > -1):
        if (iterator == 0):
            snake_body_x[iterator] += snake_x_change
            snake_body_y[iterator] += snake_y_change
            break
        snake_body_x[iterator] = snake_body_x[iterator - 1]
        snake_body_y[iterator] = snake_body_y[iterator - 1]
        iterator -= 1

    """The snake eat food."""
    if (snake_body_x[0]==food_x) and (snake_body_y[0]==food_y):
        food_x = random.randrange(0, DISPLAY_WIDTH, SNAKE_WIDTH)
        food_y = random.randrange(0, DISPLAY_HEIGHT, SNAKE_WIDTH)
        score = score + 1
        snake_body_x.append(snake_body_x[-1] - snake_x_change)
        snake_body_y.append(snake_body_y[-1] - snake_y_change)

    """Frame out to the screen."""
    screen.fill(BLACK)

    font = pygame.font.Font(None, 30)
    text = "Your score: " + str(score)
    message = font.render(text, True, YELLOW)
    screen.blit(message, [10, 10])

    for i in range(len(snake_body_x)):
        pygame.draw.rect(screen, GREEN, [snake_body_x[i],
                         snake_body_y[i], SNAKE_WIDTH, SNAKE_WIDTH])

    pygame.draw.rect(screen, RED, [food_x, food_y,
                     SNAKE_WIDTH, SNAKE_WIDTH])

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
quit()
