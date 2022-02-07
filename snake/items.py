"""
This module contains the describe of items for snake game.

Classes
-------
Segment
Snake
Food

Functions
---------
dist
"""
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

    Parameters
    ----------
        a, b : list
            Coordinate list a[x, y]
            x, y : int

    Returns
    -------
        d : int
            Distance between a and b.
    """

    d = math.sqrt((b[0] - a[0])**2 +(b[1] - a[1])**2)
    return d

class Segment:
    """
    This class defines a segments of snake.

    Attributes
    ----------
    self.__pos : list
        Coordinate list self.__pos[x, y]
        x, y : int
    self.__width : int
        The width of segment.
    self.__color : tuple
        The color of segment. (x, y, z)
        x, y, z : int some value in range 256.

    Methods
    -------
    get_pos()
    get_width()
    get_color()
    set_pos()
    set_width()
    set_color()
    """

    def __init__(self, snake_width):
        self.__pos = [100, 100]
        self.__width = snake_width
        self.__color = (0, 255, 0)

    def get_pos(self):
        """
        This method returns the position of segment.

        Returns
        -------
        self.__pos : list
            self.__pos[x, y] the coordinate list.
            x, y : int
        """

        return self.__pos

    def get_width(self):
        """
        This method returns the width of segment.

        Returns
        -------
        self.__width : int
        """

        return self.__width

    def get_color(self):
        """
        This method returns the color of segment.

        Returns
        -------
        self.__color : tuple
        """

        return self.__color

    def set_pos(self, pos):
        """
        This method sets the position of segment with pos.

        Parameters
        ----------
        pos : list
            pos[x, y] the coordinate list
            x, y : int
        """

        self.__pos = pos

    def set_width(self, width):
        """
        This method sets the width of segment.

        Parameters
        ----------
        width :int
            The value, what will be the width of the segment.
        """

        self.__width = width

    def set_color(self, color):
        """
        This method sets the color of the segment.

        Parameters
        ----------
        color : tuple
            color(x, y, z)
            x, y, z : int some value in range 256.
        """

        self.__color = color

class Snake:
    """
    This class defines the snake.

    Attributes
    ----------
    self.__width : int
        The width of the snake.
    self.__segment : list
        self.__segment[Segment(snake_width)]
        Segment(snake_width) is an object of class Segment with snake_width.
    self.__pos_change : list
        self.__pos_change[x, y] the numbers of pixels of snake movement.
        x, y : int
    self.__course : str
        self.__course maybe 'LEFT', 'RIGHT', 'UP', 'DOWN'.

    Methods
    -------
    set_course(course)
        This method sets the course of snake movement.
    move()
        This method defines snake movement
    set_pos(pos)
        This method sets position of snake head
    eat()
        This method defines eating snake food
    get_course()
        This method return current course of snake movement
    get_head_pos()
        This method return current position of snake head
    get_body()
        This method return the list of segments of snake

    See Also
    --------
    class Segment
    """

    def __init__(self, snake_width):
        self.__width = snake_width
        self.__segment = [Segment(snake_width)]
        self.__pos_change = [0, 0]
        self.__course = "empty"

    def set_course(self, course, speed):
        """
        This method sets the course of snake movement.

        Parameters
        ----------
        course : str
            The course of snake movement.
        speed : int
            The nubers of pixels of snake movement.
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
        """
        This method sets position of snake head

        Parameters
        ----------
        pos : list
            pos[x, y] is list of coordinates.
            x, y : int
        """

        head = self.__segment[0]
        head.set_pos(pos)

    def eat(self, food_size, food_color):
        """
        This method defines eating snake food

        Parameters
        ----------

        food_size : int
            The size of food.
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
        """
        This method return current course of snake movement

        Returns
        -------
        self.__course : str
            self.__course is the course of snake movement.
        """

        return self.__course

    def get_head_pos(self):
        """
        This method return current position of snake head
        Returns
        -------
        pos : list
            The pos is the list of snake head coordinates.
        """

        head = self.__segment[0]
        pos = head.get_pos()
        return pos

    def get_body(self):
        """
        This method return the list of segments of snake
        Returns
        -------
        self.__segment : list
            self.segment is the list of snake segments.
        """

        return self.__segment

class Food:
    """
    This class describes a food.

    Attributes
        self.__size : int
            The size of food.
        self.__dw : int
            The width of the display.
        self.__dh : int
            The height of the display.
        self.__inf height : int
            The height of the information line.
        self.__x : int
            The x coordinate of food.
        self.__y : int
            The y coordinate of food.
        self.__pos [self.__x, self.__y] : list
            The list of food coordinates.
            self.__x, self.__y : int

    Methods
        get_x()
            Return x coordinate of food.
        get_y()
            Return y coordinate of food.
        get_size()
            Return the size of food.
        get_pos()
            Return the position of food.
        set_size()
            Sets self.__size.
        set_pos()
            Sets position of food.
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
        """
        This method return x coordinate of food.

        Returns
        -------
        self.__x : int
            self.__x is value of X coordinate of food.
        """

        return self.__x

    def get_y(self):
        """
        This method return y coordinate of food.

        Returns
        -------
        self.__y : int
            self.__y is value of Y coordinate of food.

        """

        return self.__y

    def get_size(self):
        """
        This method return the size of food.

        Returns
        -------
        self.__size : int
            self.__size is the size of food.

        """

        return self.__size

    def get_pos(self):
        """
        This method return the coordinates of food.

        Returns
        -------
        self.__pos : list
            self.__pos is the list of food coordinates.
        """

        return self.__pos

    def set_size(self, *args):
        """
        This method sets the size of food.

        Parameters
        ----------
        args : int
            args contain the snake width, the food size.
            snake width: int
            food size : int, str
            The food size maybe int value in range(2) or 'r'.
            If the food size is 'r' then self.__size will be random value
            in (sw // 3, sw // 2, sw), where sw is the snake width.
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
        """
        This method return current color of food.

        Returns
        -------
        self.__color : tuple
            self.__color(x, y, z)
            x, y, z : int value in range(256)
        """

        return self.__color

    def set_pos(self, snake_body, snake_width):
        """
        This method sets position of food.

        Parameters
        ----------
            snake_width : int
                The width of snake.
            snake_body [Segment()] : list
                The list of segment objects.
        Note
        ----
            sw : int
                Snake width.
            near : int
                Distance between the food and snake segments.
            pos_valid : boolean
                The flag of, which defines validity of assumed food position.
            x : int
                The X coordinate of food position.
            y : int
                The Y coordinate of food position.
            p : list
                p[x, y] is list of food coordinates.
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
