import pygame
import random
import time

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

"""Setting other values"""
score = 0
course = ""
fps = 5



class snake:
    def __init__(self, snake_width):
        self.__x_change = 0
        self.__y_change = 0
        self.__body_x = []
        self.__body_y = []
        self.__width = snake_width
        self.__course = ""

    def set_course(self):
        if event.type == pygame.KEYDOWN:
            if (event.key==pygame.K_LEFT) and (self.__course!="RIGHT"):
                self.__x_change = -10
                self.__y_change = 0
                self.__course = "LEFT"
            elif (event.key==pygame.K_RIGHT) and (self.__course!="LEFT"):
                self.__x_change = 10
                self.__y_change = 0
                self.__course = "RIGHT"
            elif (event.key==pygame.K_UP) and (self.__course!="DOWN"):
                self.__snake_y_change = -10
                self.__snake_x_change = 0
                self.__course = "UP"
            elif (event.key==pygame.K_DOWN) and (self.__course!="UP"):
                self.__snake_y_change = 10
                self.__snake_x_change = 0
                self.__course = "DOWN"

    def moving(self):
        i = len(self._body_x) - 1
        while(i > -1):
            if (i == 0):
                self._body_x[i] += self._x_change
                self._body_y[i] += self._y_change
                break
            self._body_x[i] = self._body_x[i - 1]
            self._body_y[i] = self._body_y[i - 1]
            i -= 1

    def eat(self):
        self_body_x.append(self_body_x[-1] - self_x_change)
        self_body_y.append(self_body_y[-1] - self_y_change)

    def get_snake_body_x(self)
        return self.body_x[]
    def get_snake_body_y(self)
        return self.body_y[]


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

    """Wasted by collision a border."""
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
    """Wasted by collision the snakes body."""
    for i in range(len(snake_body_x)):
        if i != 0:
            if ((snake_body_x[0] == snake_body_x[i]) and
               (snake_body_y[0] == snake_body_y[i])):
                 font = pygame.font.Font(None, 65)
                 text = "WASTED"
                 message = font.render(text, True, RED)
                 screen.blit(message, [X_CENTRE, Y_CENTRE])
                 pygame.display.update()
                 time.sleep(5)
                 running = False

    """The snake is moving."""
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
        fps = fps + 1

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
    clock.tick(fps)

pygame.quit()
quit()
