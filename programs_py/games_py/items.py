import pygame
import random

class Snake:
    def __init__(self, snake_width):
        self.__x_change = 0
        self.__y_change = 0
        self.__body_x = [50]
        self.__body_y = [50]
        self.__width = snake_width
        self.__course = "empty"
        self.__length = len(self.__body_x)

    def set_course(self, course):
        self.__course = course
        if self.__course == "LEFT":
            self.__x_change = -self.__width
            self.__y_change = 0
        elif self.__course == "RIGHT":
            self.__x_change = self.__width
            self.__y_change = 0
        elif self.__course == "UP":
            self.__y_change = -self.__width
            self.__x_change = 0
        elif self.__course == "DOWN":
            self.__y_change = self.__width
            self.__x_change = 0

    def move(self):
        i = len(self.__body_x) - 1
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

    def get_body_x(self):
        return self.__body_x

    def get_body_y(self):
        return self.__body_y

    def get_course(self):
        return self.__course

    def get_length(self):
        return self.__length

    def get_x_change(self):
        return self.__x_change

    def get_y_change(self):
        return self.__y_change

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

class CircleFood:
    def __init__(self, food_size, display_width, display_height):
        self.__radius = food_size / 2
        self.__d_w = display_width
        self.__d_h = display_height
        self.__x = random.randrange(0, self.__d_w, food_size)
        self.__y = random.randrange(0, self.__d_h, food_size)

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def set_pos(self):
        self.__x = random.randrange(self.__radius, (self.__d_w-self.__radius),
                                   (self.__radius*2))
        self.__y = random.randrange(self.__radius, (self.__d_h-self.__radius),
                                   (self.__radius*2))

    def get_radius(self):
        return self.__radius
