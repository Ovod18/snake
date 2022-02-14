"""This module contains the describe of items for snake game.

:platform: Linux
:author: Ovod18

|
"""
import random
import math

colors = ((255, 255, 255),
         (0, 0, 0),
         (255, 0, 0),
         (0, 255, 0),
         (0, 0, 255),
         (255, 255, 0))
"""RGB colors values.

:type: tuple

|
"""

def dist(a, b):
    """
    Calculation the distance between two points.

    :param a: point coordinates a[x, y]
    :type a: list
    :param b: point coordinates b [x, y]
    :type b: list

    :rtype: int
    :return: distance between a and b

    |
    """

    return math.sqrt((b[0] - a[0])**2 +(b[1] - a[1])**2)

class Segment:
    """This class defines snake segments.

    .. py:method:: get_pos()
    .. py:method:: get_width()
    .. py:method:: get_color()
    .. py:method:: set_pos()
    .. py:method:: set_width()
    .. py:method:: set_color()

    |

    .. py:attribute:: pos
        :type: list
        :value: [100, 100]
    .. py:attribute:: width
        :type: int
    .. py:attribute:: color
        :type: tuple
        :value: 0, 255, 0

    |
    """

    def __init__(self, snake_width):
        self.__pos = [100, 100]
        self.__width = snake_width
        self.__color = (0, 255, 0)

    def get_pos(self):
        """This method returns the position of segment.

        :return: The list of segment coordinates.
        :rtype: list

        |
        """

        return self.__pos

    def get_width(self):
        """This method returns the width of segment.

        :returns: A segment width.
        :rtype: int

        |
        """

        return self.__width

    def get_color(self):
        """This method returns the color of segment.

        :returns: A segment color.
        :rtype: tuple

        |
        """

        return self.__color

    def set_pos(self, pos):
        """This method sets the position of segment with pos.

        :param list pos: The list of segment coordinates.

        |
        """

        self.__pos = pos

    def set_width(self, width):
        """This method sets the width of segment.

        :param int width: A segment width.

        |
        """

        self.__width = width

    def set_color(self, color):
        """This method sets the color of the segment.

        :param tuple color: A segment color.

        |
        """

        self.__color = color

class Snake:
    """This class defines the snake.

    .. py:method:: set_course()
    .. py:method:: move()
    .. py:method:: set_pos(pos)
    .. py:method:: eat()
    .. py:method:: get_course()
    .. py:method:: get_head_pos()
    .. py:method:: get_body()

    |

    .. py:attribute:: width
        :type: int
    .. py:attribute:: segment
        :type: object
    .. py:attribute:: pos_change
        :type: list[int, int]
        :value: 0, 0
    .. py:attribute:: course
        :type: str
        :value: 'empty'

        |
    """

    def __init__(self, snake_width):
        self.__width = snake_width
        self.__segment = [Segment(snake_width)]
        self.__pos_change = [0, 0]
        self.__course = "empty"

    def set_course(self, course, speed):
        """This method sets the course of snake movement.

        :param str course: The course of snake movement.
        :param int speed: The nubers of pixels of snake movement.

        |
        """

        step = speed
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
        """This method defines snake movement.

        |
        """
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
        """This method sets position of snake head.

        :param list pos: pos[int, int] is list of coordinates.

        |
        """

        head = self.__segment[0]
        head.set_pos(pos)

    def eat(self, food_size, food_color):
        """This method defines eating snake food.

        :param int food_size: The size of food.

        |
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
        """This method return current course of snake movement.

        :returns: The course of snake movement.
        :rtype: str

        |
        """

        return self.__course

    def get_head_pos(self):
        """This method return current position of snake head.

        :returns: The list of coordinates of the snake head.
        :rtype: list[int, int]

        |
        """

        head = self.__segment[0]
        pos = head.get_pos()
        return pos

    def get_body(self):
        """This method return the list of segments of snake.

        :returns: the list of snake segments.
        :rtype: list[object,]

        |
        """

        return self.__segment

class Food:
    """This class describes a food.

    .. py:method:: get_x()
    .. py:method:: get_y()
    .. py:method:: get_size()
    .. py:method:: get_pos()
    .. py:method:: set_size()
    .. py:method:: set_pos()

    |

    .. py:attribute:: size
        :type: int
    .. py:attribute:: dw
        :type: int
    .. py:attribute:: dh
        :type: int
    .. py:attribute:: inf height
        :type: int
    .. py:attribute:: x
        :type: int
    .. py:attribute:: y
        :type: int
    .. py:attribute:: pos
        :type: list
    .. py:attribute:: color
        :type: tuple
        :value: 0, 255, 0

    |
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
        """This method return x coordinate of food.

        :returns: x
        :rtype: int

        |
        """

        return self.__x

    def get_y(self):
        """This method return y coordinate of food.

        :returns: y
        :rtype: int

        |
        """

        return self.__y

    def get_size(self):
        """This method return the size of food.

        :returns: size
        :rtype: int

        |
        """

        return self.__size

    def get_pos(self):
        """This method return the coordinates of food.

        :returns: pos
        :rtype: list

        |
        """

        return self.__pos

    def set_size(self, *args):
        """This method sets the size of food.

        args : int
            args contain the snake width, the food size.
            snake width: int
            food size : int, str
            The food size maybe int value in range(2) or 'r'.
            If the food size is 'r' then self.__size will be random value
            in (sw // 3, sw // 2, sw), where sw is the snake width.

        |
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
        """This method return current color of food.

        :returns: color
        :rtype: tuple

        |
        """

        return self.__color

    def set_pos(self, snake_body, snake_width):
        """This method sets position of food.

        :param int snake_width: The width of snake.
        :param list snake_body: The list of segment objects.

        |
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
        """This method sets color of food.i

        |
        """
        i = random.randint(2, len(colors) - 1)
        self.__color = colors[i]
