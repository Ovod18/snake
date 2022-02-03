"""This module contains the describe of items."""
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

class Segment:
    def __init__(self, snake_width):
        self.__pos = [100, 100]
        self.__width = snake_width
        self.__color = (0, 255, 0)

    def get_pos(self):
        return self.__pos

    def get_width(self):
        return self.__width

    def get_color(self):
        return self.__color

    def set_pos(self, pos):
        self.__pos = pos

    def set_width(self, width):
        self.__width = width

    def set_color(self, color):
        self.__color = color

class Snake:

    def __init__(self, snake_width):
        self.__width = snake_width
        self.__segment = [Segment(snake_width)]
        self.__pos_change = [0, 0]
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
        i = len(self.__segment) - 1
        while(i > -1):
            segment = self.__segment[i]
            pos = segment.get_pos()
            if (i == 0):
                x = pos[0] + self.__pos_change[0]
                y = pos[1] + self.__pos_change[1]
                pos = [x, y]
                segment.set_pos(pos)
                break
            p_segment = self.__segment[i - 1]
            pos = p_segment.get_pos()
            segment.set_pos(pos)
            i -= 1

    def set_pos(self, pos):
        """This method sets position of snake head"""
        head = self.__segment[0]
        head.set_pos(pos)

    def eat(self, food_size, food_color):
        """
        This method defines eating snake food

        ARGUMENTS:
            food_size (int): size of food
        """
        for i in range(food_size):
            segment = self.__segment[-1]
            pos = segment.get_pos()
            x = pos[0] - self.__pos_change[0]
            y = pos[1] - self.__pos_change[1]
            new_pos = [x, y]
            new_segment = Segment(self.__width)
            new_segment.set_pos(new_pos)
            new_segment.set_color(food_color)
            self.__segment.append(new_segment)

    def get_course(self):
        """This method return current course of snake movement"""
        return self.__course

    def get_head_pos(self):
        """This method return current position of snake head"""
        head = self.__segment[0]
        pos = head.get_pos()
        return pos

    def get_body(self):
        """This method return the list of segments of snake"""
        return self.__segment

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

    def set_size(self, *args):
        """
        This method sets the size of food.
        """
        sw = args[0]
        if args[1] == "r":
            r = True
        else :
            r = False
        if r:
            size = [sw // 3, sw // 2, sw]
            i = random.randrange(0, 3)
            self.__size = size[i]
        else:
            i = args[1]
            size = [sw // 3, sw // 2, sw]
            self.__size = size[i]

    def get_color(self):
        """This method return current color of food."""
        return self.__color

    def set_pos(self, snake_body, snake_width):
        """
        This method sets position of food.
        ARGIMENTS:
            snake_width (int): the width of snake.
            snake_body [Segment()]: list of segment objects.
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
            y = random.randrange(self.inf_height+self.__size,
                                 (self.dh-self.__size))
            p = [x, y]
            for i in range(len(snake_body)):
                segment = snake_body[i]
                pos = segment.get_pos()
                if (dist(p, pos) >= near):
                    pos_valid = True
                else:
                    pos_valid = False
                    count += 1
            if count == 0:
                break
        self.__pos = p

    def set_color(self):
        """This method sets color of food."""
        i = random.randint(2, len(colors) - 1)
        self.__color = colors[i]
