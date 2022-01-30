"""This module contains the describe of items."""
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
import random
import math

colors = ((255, 255, 255),
         (0, 0, 0),
         (255, 0, 0),
         (0, 255, 0),
         (0, 0, 255),
         (255, 255, 0))

def dist(a, b):
    """
    Calculation the distance between two points.

    ARGUMENTSS:
        a[x,y]
        b[x,y]

    RETURN:
        d (int): distance.
    """

    d = math.sqrt((b[0] - a[0])**2 +(b[1] - a[1])**2)
    return d

class Snake:
    """
    This class describes a snake.

    ATTRIBUTES:
        self.__pos_change[x, y]: motion change module.
        self.__segment_pos[[x, y], ... , [n, m]]: list of snake segment
                                                            coordinates.
        self.__width (int): snake width.
        self.__course (str): course of snake movement,  maybe "LEFT", "RIGHT",
                                                            "UP", "DOWN".

    METHODS:
        set_course(course): sets self.__course = course
        move(): describes snake movement.
        set_pos(pos): sets the position of snake's head in pos[x, y].
        eat(food_size): increase the length of the snake by food_size.
        get_course(): return self.__course.
        get_head_pos(): return the list coordinates [x, y] of snake's head.
        get_body(): return the list of coordinates [x, y] of snake's segments.
    """
    def __init__(self, snake_width):
        self.__pos_change = [0, 0]
        self.__segment_pos = [[100, 100]]
        self.__width = snake_width
        self.__course = "empty"

    def set_course(self, course):
        """
        This method sets the course of snake movement.
        VARIABLES:
            step (int): the nubers of pixels of snake movement.
        """
        step = 1
        self.__course = course
        if self.__course == "LEFT":
            self.__pos_change = [-step, 0]
        elif self.__course == "RIGHT":
            self.__pos_change = [step, 0]
        elif self.__course == "UP":
            self.__pos_change = [0, -step]
        elif self.__course == "DOWN":
            self.__pos_change =[0, step]

    def move(self):
        """This method defines snake movement"""
        i = len(self.__segment_pos) - 1
        while(i > -1):
            pos = self.__segment_pos[i]
            if (i == 0):
                x = pos[0] + self.__pos_change[0]
                y = pos[1] + self.__pos_change[1]
                self.__segment_pos[i] = [x, y]
                break
            self.__segment_pos[i] = self.__segment_pos[i - 1]
            i -= 1

    def set_pos(self, pos):
        """This method sets position of snake head"""
        self.__segment_pos[0] = pos


    def eat(self, food_size):
        """
        This method defines eating snake food

        ARGUMENTS:
            food_size (int): size of food
        """
        for i in range(food_size):
            pos = self.__segment_pos[-1]
            x = pos[0] - self.__pos_change[0]
            y = pos[1] - self.__pos_change[1]
            buff = [x, y]
            self.__segment_pos.append(buff)

    def get_course(self):
        """This method return current course of snake movement"""
        return self.__course

    def get_head_pos(self):
        """This method return current position of snake head"""
        return self.__segment_pos[0]

    def get_body(self):
        """This method return the list of coordinates segments of snake"""
        return self.__segment_pos

class Food:
    """
    This class describes a food.

    ATTRIBUTES:
        self.__size (int): the size of food.
        self.__dw (int): the width of the display.
        self.__dh (int): the height of the display.
        self.__inf height (int): the height of the information line.
        self.__x (int): the x coordinate of food.
        self.__y (int): the y coordinate of food.
        self.__pos [self.__x, self.__y]: position of food.

    METHODS:
        get_x(): return x coordinate of food.
        get_y(): return y coordinate of food.
        get_size(): return the size of food.
        get_pos(): return the position of food.
        set_size(): sets self.__size.
        set_pos(): sets position of food.
    """
    def __init__(self, snake_width, display_width, display_height, inf_height):
        self.__size = snake_width // 3
        self.dw = display_width
        self.dh = display_height
        self.inf_height = inf_height
        self.__x = random.randrange(self.__size, self.dw)
        self.__y = random.randrange(self.__size + inf_height, self.dh)
        self.__pos = [self.__x, self.__y]
        self.__color = (0, 255, 0)

    def get_x(self):
        """This method return x coordinate of food."""
        return self.__x

    def get_y(self):
        """This method return y coordinate of food."""
        return self.__y

    def get_size(self):
        """This method return the size of food."""
        return self.__size

    def get_pos(self):
        """This method return the coordinates of food."""
        return self.__pos

    def set_size(self, snake_width):
        """
        This method sets the size of food.
        ARGUMENTS:
            snake_width (int): the width of snake.
        """
        sw = snake_width
        size = [sw // 3, sw // 2, sw]
        i = random.randrange(0, 3)
        self.__size = size[i]

    def get_color(self):
        return self.__color

    def set_pos(self, excl, snake_width):
        """
        This method sets position of food.
        ARGIMENTS:
            snake_width (int): the width of snake.
            excl [[x, y], ..., [n, m]]: the list of coordinates snake segments.
        VARIABLES:
            sw (int): snake width.
            near (int): distance between the food and snake segments.
            pos_valid (boolean): the flag of, which defines validity of assumed
                                food position.
            x (int): x coordinate of food position.
            y (int): y coordinate of food position.
            p [x, y]: coordinates of food.
        """
        sw = snake_width
        near = sw / 2 + self.__size
        pos_valid = False
        while 1 < 2:
            count = 0
            x = random.randrange(self.__size, (self.dw-self.__size))
            y = random.randrange(self.inf_height + self.__size,
                                 (self.dh-self.__size))
            p = [x, y]
            for pos in excl:
                if (dist(p, pos) >= near):
                    pos_valid = True
                else:
                    pos_valid = False
                    count += 1
            if count == 0:
                break
        self.__pos = p

    def set_color(self):
        i = random.randint(2, len(colors) - 1)
        self.__color = colors[i]
