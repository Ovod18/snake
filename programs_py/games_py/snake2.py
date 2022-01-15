import pygame
import random
import time
import math
import items

DISPLAY_WIDTH = 200
DISPLAY_HEIGHT = 200
X_CENTRE = DISPLAY_WIDTH / 2
Y_CENTRE = DISPLAY_HEIGHT / 2
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
SNAKE_WIDTH = 20

"""Creating the main window."""
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("My snake")

clock = pygame.time.Clock()

"""Setting snakes properties"""
my_snake = items.CircularSnake(SNAKE_WIDTH)
body = my_snake.get_body()
head_pos = my_snake.get_head_pos()

"""Setting other values"""
score = 0
course = ""
apple = items.Food(SNAKE_WIDTH, DISPLAY_WIDTH, DISPLAY_HEIGHT)
scr_border = [[]]
for i in range(DISPLAY_WIDTH):
    scr_border.append([i, 0])
    scr_border.append([i, DISPLAY_WIDTH])
for i in range(DISPLAY_HEIGHT):
    scr_border.append([0, i])
    scr_border.append([0, DISPLAY_HEIGHT])

def dist(a, b):
    d = math.sqrt((b[0] - a[0])**2 +(b[1] - a[1])**2)
    return d

""" Creating the game cycle."""
running = True
while running:
    """Keys binding"""
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            running = False
        if event.type == pygame.KEYDOWN:
            if (event.key==pygame.K_LEFT) and (course!="RIGHT"):
                course = "LEFT"
            elif (event.key==pygame.K_RIGHT) and (course!="LEFT"):
                course = "RIGHT"
            elif (event.key==pygame.K_UP) and (course!="DOWN"):
                course = "UP"
            elif (event.key==pygame.K_DOWN) and (course!="UP"):
                course = "DOWN"
            elif event.key == pygame.K_ESCAPE:
                running = False

    """Snake movement"""
    my_snake.set_course(course)
    my_snake.move()

    """Snake eats food"""
    h_pos = my_snake.get_head_pos()
    a_pos = apple.get_pos()
    a_radius = apple.get_radius()
    d = dist(a_pos, h_pos)
    if d < a_radius:
        my_snake.eat()
        apple.set_pos(body, SNAKE_WIDTH)
        score = score + 1


    """Collision a border."""
    if h_pos[0] == 0:
        pos = [DISPLAY_WIDTH, h_pos[1]]
        my_snake.set_pos(pos)
    elif h_pos[0] == DISPLAY_WIDTH:
        pos = [0, h_pos[1]]
        my_snake.set_pos(pos)
    if h_pos[1] == 0:
        pos = [h_pos[0], DISPLAY_HEIGHT]
        my_snake.set_pos(pos)
    elif h_pos[1] == DISPLAY_HEIGHT:
        pos = [h_pos[0], 0]
        my_snake.set_pos(pos)

    """Wasted by collision the snakes body."""
    for i in range(SNAKE_WIDTH * 2, len(body)):
        d = dist(body[i], h_pos)
        if d < SNAKE_WIDTH:
            font = pygame.font.Font(None, 65)
            text = "WASTED"
            message = font.render(text, True, RED)
            screen.blit(message, [X_CENTRE, Y_CENTRE])
            pygame.display.update()
            time.sleep(3)
            running = False
            break

    """Frame out to the screen."""
    screen.fill(BLACK)

    font = pygame.font.Font(None, 30)
    text = "Your score: " + str(score) + "      FPS: " + str(FPS)
    message = font.render(text, True, YELLOW)
    screen.blit(message, [10, 10])

    for segment in body:
        pygame.draw.circle(screen, GREEN, (segment[0], segment[1]),
                           (SNAKE_WIDTH/2), SNAKE_WIDTH)

    apple_pos = apple.get_pos()
    pygame.draw.circle(screen, RED, (apple_pos[0], apple_pos[1]),
                    apple.get_radius() , SNAKE_WIDTH)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
quit()
