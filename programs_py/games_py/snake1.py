import pygame
import random
import time
import items

DISPLAY_WIDTH = 360
DISPLAY_HEIGHT = 360
X_CENTRE = DISPLAY_WIDTH / 2
Y_CENTRE = DISPLAY_HEIGHT / 2
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

"""Setting snakes properties"""
my_snake = items.Snake(SNAKE_WIDTH)
body_x = my_snake.get_body_x()
body_y = my_snake.get_body_y()

"""Setting other values"""
score = 0
course = ""
fps = 5

apple = items.Food(SNAKE_WIDTH, DISPLAY_WIDTH, DISPLAY_HEIGHT)

""" Creating the game cycle."""
running = True
while running:
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
    my_snake.set_course(course)
    my_snake.move()
    if ((body_x[0]==apple.get_x()) and
       (body_y[0]==apple.get_y())):
        my_snake.eat()
        apple.set_pos()
        fps = fps + 1
        score = score +1

    """Wasted by collision a border."""
    if ((body_x[0] >= DISPLAY_WIDTH) or (body_x[0] < 0) or
           (body_y[0] >= DISPLAY_HEIGHT) or
           (body_y[0] < 0)):
         font = pygame.font.Font(None, 65)
         text = "WASTED"
         message = font.render(text, True, RED)
         screen.blit(message, [X_CENTRE, Y_CENTRE])
         pygame.display.update()
         time.sleep(5)
         running = False

    """Wasted by collision the snakes body."""
    for i in range(len(body_x)):
        if i != 0:
            if ((body_x[0] == body_x[i]) and
               (body_y[0] == body_y[i])):
                font = pygame.font.Font(None, 65)
                text = "WASTED"
                message = font.render(text, True, RED)
                screen.blit(message, [X_CENTRE, Y_CENTRE])
                pygame.display.update()
                time.sleep(5)
                running = False

    """Frame out to the screen."""
    screen.fill(BLACK)

    font = pygame.font.Font(None, 30)
    text = "Your score: " + str(score)
    message = font.render(text, True, YELLOW)
    screen.blit(message, [10, 10])

    for i in range(len(body_x)):
        pygame.draw.rect(screen, GREEN, [body_x[i], body_y[i],
                         SNAKE_WIDTH, SNAKE_WIDTH])
    pygame.draw.rect(screen, RED, [apple.get_x(), apple.get_y(),
                     SNAKE_WIDTH, SNAKE_WIDTH])

    pygame.display.update()
    clock.tick(fps)

pygame.quit()
quit()
