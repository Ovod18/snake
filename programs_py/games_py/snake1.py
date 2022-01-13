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

"""Setting the coordinates of snake."""
snake_x_change = 0
snake_y_change = 0
snake_body_x = [X_CENTRE]
snake_body_y = [Y_CENTRE]
food_x = random.randrange(0, DISPLAY_WIDTH, SNAKE_WIDTH)
food_y = random.randrange(0, DISPLAY_HEIGHT, SNAKE_WIDTH)

my_snake = items.Snake(SNAKE_WIDTH)



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

    my_snake.set_course()
    my_snake.move()
   # my_snake.eat()


    screen.fill(BLACK)

    list_body_x = my_snake.get_body_x()
    list_body_y = my_snake.get_body_y()
    for i in range(len(list_body_x)):
        pygame.draw.rect(screen, GREEN, [list_body_x[i], list_body_y[i],
                         SNAKE_WIDTH, SNAKE_WIDTH])
        print(my_snake.get_course())
    pygame.draw.rect(screen, RED, [apple.get_x(), apple.get_y(),
                     SNAKE_WIDTH, SNAKE_WIDTH])

    pygame.display.update()
    clock.tick(fps)

pygame.quit()
quit()
