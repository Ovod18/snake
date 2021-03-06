"""This module contains the describe of items for snake game.

:platform: Linux
:author: Ovod18

|

CLASSES

:py:class:`.Food`

:py:class:`.Segment`

:py:class:`.Snake`

|
"""
import random
import math
import copy
import pygame

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

    METHODS

    :py:meth:`Segment.draw()`

    :py:meth:`Segment.get_pos()`

    :py:meth:`Segment.get_width()`

    :py:meth:`Segment.get_color()`

    :py:meth:`Segment.set_pos()`

    :py:meth:`Segment.set_width()`

    :py:meth:`Segment.set_color()`

    |

    ATTRIBUTES

    .. py:attribute:: pos
        The list of segment coordinates.
        :type: list
        :value: [100, 100]
    .. py:attribute:: width
        The segment width.
        :type: int
    .. py:attribute:: color
        The segment color.
        :type: tuple
        :value: 0, 255, 0

    |
    """

    def __init__(self, snake_width):
        self.__pos = [100, 100]
        self.__width = snake_width
        self.__color = (0, 255, 0)

    def draw(self, scene):
        """This method renders a segment

        :param object scene: The scene for rendering a segment(pygame.display).

        |
        """
        pygame.draw.circle(scene, self.__color, (self.__pos[0], self.__pos[1]),
                                            (self.__width/2), 0)

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

    METHODS

    :py:meth:`Snake.draw()`

    :py:meth:`Snake.set_course()`

    :py:meth:`Snake.move()`

    :py:meth:`Snake.set_pos(pos)`

    :py:meth:`Snake.eat()`

    :py:meth:`Snake.get_course()`

    :py:meth:`Snake.get_head_pos()`

    :py:meth:`Snake.get_body()`

    :py:meth:`Snake.is_crit_len()`

    :py:meth:`Snake.is_collision_with_body()`

    :py:meth:`Snake.food_is_near()`

    :py:meth:`Snake.get_width()`

    :py:meth:`Snake.grow()`

    |

    ATTRIBUTES

    .. py:attribute:: width
        The snake width.
        :type: int
    .. py:attribute:: body
        The list of snake segments.

    :py:class:`.Segment()`

    .. py:attribute:: pos_change
        The course (pixels) of snake movement.
        :type: list[int, int]
        :value: 0, 0
    .. py:attribute:: course
        The course (word) of snake movement.
        :type: str
        :value: 'empty'
    .. py:attribute:: eaten_food
        The list of eaten food
        :type: list[object]

        |
    """

    def __init__(self, snake_width):
        self.__width = snake_width
        self.__body = [Segment(snake_width)]
        self.__pos_change = [0, 0]
        self.__course = "empty"
        self.__eaten_food = []

    def get_width(self):
        """This method returns the snake width.

        :returns: snake width
        :rtype: int
        """
        return self.__width

    def food_is_near(self, food):
        """This method checks the distance between the snake and food.

        :return: True or False
        :rtype: boolean

        |
        """
        head_pos = self.get_head_pos()
        food_pos = food.get_pos()
        if dist(head_pos, food_pos) < self.__width / 2:
            return True
        else:
            return False

    def is_collision_with_body(self):
        """This method checks the collision with snake body

        :return: True or False
        :rtype: boolean

        |
        """
        head_pos = self.get_head_pos()
        count = 0
        for i in range(self.__width * 2, len(self.__body)):
            segment = self.__body[i]
            if dist(segment.get_pos(), head_pos) < self.__width:
               count += 1
        if count != 0:
            return True
        else:
            return False

    def is_crit_len(self, scene):
        """This method chekcs wether the length of the snake is critical.

        :param object scene: The play ground.
        :returns: True or False
        :rtype: boolean

        |
        """
        scene_size = scene.get_size()
        scene_width = scene_size[0]
        scene_height = scene_size[1]
        crit_len = scene_width * scene_height // self.__width * 4
        if len(self.__body) >= crit_len:
            return True
        else:
            return False

    def draw(self, scene):
        """This method renders the snake body.

        :param object scene: The scene for rendering the body (pygame.display).

        """
        for segment in self.__body:
            segment.draw(scene)

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

    def move(self, play_ground):
        """This method defines snake movement.

        :param object play_ground: :py:class:`.PlayGround`

        |
        """

        i = len(self.__body) - 1
        last_segment = self.__body[i]
        last_segment_pos = last_segment.get_pos()
        if len(self.__eaten_food) > 0:
            eaten_food_pos = self.__eaten_food[0][0].get_pos()
            w = last_segment.get_width()
            if dist(last_segment_pos, eaten_food_pos) < w:
                self.grow()
        while(i > -1):
            segment = self.__body[i]
            pos = segment.get_pos()
            # move the head
            if (i == 0):
                x = pos[0] + self.__pos_change[0]
                y = pos[1] + self.__pos_change[1]
                pos = [x, y]
                segment.set_pos(pos)
                break
            # move the body
            p_segment = self.__body[i - 1]
            pos = p_segment.get_pos()
            segment.set_pos(pos)
            i -= 1
        # collision with borders
        p_g_pos = play_ground.get_pos()
        x = 0
        y = 1
        top = p_g_pos[0][y]
        bottom = p_g_pos[1][y]
        left = p_g_pos[0][x]
        right = p_g_pos[1][x]
        head = self.__body[0]
        head_pos = head.get_pos()
        if head_pos[x] <= left:
            new_pos = [right, head_pos[y]]
            head.set_pos(new_pos)
        elif head_pos[x] >= right:
            new_pos = [left, head_pos[y]]
            head.set_pos(new_pos)
        if head_pos[y] <= top:
            new_pos = [head_pos[x], bottom]
            head.set_pos(new_pos)
        elif head_pos[y] >= bottom:
            new_pos = [head_pos[x], top]
            head.set_pos(new_pos)

    def set_pos(self, pos):
        """This method sets position of the snake head.

        :param list pos: pos[int, int] is list of coordinates.

        |
        """

        head = self.__body[0]
        head.set_pos(pos)

    def eat(self, food):
        """This method defines eating food.

        :param object food: Eaten food.

        |
        """

        new_eaten_food = copy.deepcopy(food)
        size = food.get_size()
        self.__eaten_food.append([new_eaten_food, size])

    def grow(self):
        """This method defines the snake growing.

        |
        """
        size = self.__eaten_food[0][0].get_size()
        color = self.__eaten_food[0][0].get_color()
        new_pos = self.__body[-1].get_pos()
        new_segment = Segment(self.__width)
        new_segment.set_pos(new_pos)
        new_segment.set_color(color)
        self.__body.append(new_segment)
        self.__eaten_food[0][1] -= 1
        if self.__eaten_food[0][1] == 0:
            self.__eaten_food.pop(0)


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

        head = self.__body[0]
        pos = head.get_pos()
        return pos

    def get_body(self):
        """This method return the list of segments of snake.

        :returns: the list of snake segments.
        :rtype: list[object,]

        |
        """

        return self.__body

class Food:
    """This class describes a food.

    METHODS

    :py:meth:`Food.draw()`

    :py:meth:`Food.get_size()`

    :py:meth:`Food.get_pos()`

    :py:meth:`Food.get_color()`

    :py:meth:`Food.set_size()`

    :py:meth:`Food.set_pos()`

    |

    ATTRIBUTES

    .. py:attribute:: size
        The size of food.
        :type: int
    .. py:attribute:: primary_x
        The primary x coordinate of food.
        :type: int
    .. py:attribute:: primary_y
        The primary y coordinate of food.
        :type: int
    .. py:attribute:: pos
        The list of coordinates pos[x, y] of food.
        :type: list
    .. py:attribute:: color
        The color of food.
        :type: tuple
        :value: 0, 255, 0

    |
    """

    def __init__(self, play_ground, snake):
        self.__size = snake.get_width() // 3
        p_g_pos = play_ground.get_pos()
        self.__primary_x = random.randrange(p_g_pos[0][0] + self.__size,
                                            p_g_pos[1][0] - self.__size)
        self.__primary_y = random.randrange(p_g_pos[0][1] + self.__size,
                                            p_g_pos[1][1] - self.__size)
        self.__pos = [self.__primary_x, self.__primary_y]
        self.__color = (0, 255, 0)

    def draw(self, scene):
        """This method renders the food

        :param object scene: The scene for rendering food (pygame.display).

        |
        """
        pygame.draw.circle(scene, self.__color, (self.__pos[0], self.__pos[1]),
                                             self.__size/2 , 0)

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
            args contain the snake, the food size.
            snake : object
            food size : int or str
            The food size maybe int value in range(2) or 'r'.
            If the food size is 'r' then self.__size will be random value
            in (sw // 3, sw // 2, sw), where sw is the snake width.

        |
        """

        snake = args[0]
        sw = snake.get_width()
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

    def set_pos(self, play_ground, snake):
        """This method sets position of food.

        |
        """

        sw = snake.get_width()
        snake_body = snake.get_body()
        near = sw / 2 + self.__size
        p_g_pos = play_ground.get_pos()
        pos_valid = False
        while 1 < 2:
            count = 0
            x = random.randrange(p_g_pos[0][0] + self.__size,
                                 p_g_pos[1][0] - self.__size)
            y = random.randrange(p_g_pos[0][1] + self.__size,
                                 p_g_pos[1][1] - self.__size)
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
        """This method sets color of food.

        |
        """

        i = random.randint(2, len(colors) - 1)
        self.__color = colors[i]


