import random


class Snake:
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
                self.__body_x[i] += self.__x_change
                self.__body_y[i] += self.__y_change
                break
            self.__body_x[i] = self.__body_x[i - 1]
            self.__body_y[i] = self.__body_y[i - 1]
            i -= 1

    def eat(self):
        self.__body_x.append(self.__body_x[-1] - self.__x_change)
        self.__body_y.append(self.__body_y[-1] - self.__y_change)

    def get_snake_body_x(self):
        return self.__body_x
    def get_snake_body_y(self):
        return self.__body_y

class Food:

    def __init__(self, food_size, display_width, display_height):
        self.__size = food_size
        self.__d_w = display_width
        self.__d_h = display_height
        self.__x = random.randrange(0, self.__d_w, self.__size)
        self.__y = random.randrange(0, self.__d_h, self.__size)

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def set_pos(self):
        self.__x = random.randrange(0, self.__d_w, self.__size)
        self.__y = random.randrange(0, self.__d_h, self.__size)
