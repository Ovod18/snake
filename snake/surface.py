"""This module contains surfaces for snake game

:platform: Linux
:author: Ovod18

CLASSES

:py:class:`.PlayGround`

:py:class:`.InfoString`

|
"""

import pygame

class PlayGround:
    """This class describes the playing ground.

    METHODS

    :py:meth:`PlayGround.get_pos()`

    |

    ATTRIBUTES

    .. py:attribute:: self.__x0
        The initial X coordinate of playing ground.
        :type: int
    .. py:attribute:: self.__y0
        The initial Y coordinate of playing ground.
        :type: int
    .. py:attribute:: self.__x
        The final X coordinate of playing ground.
        :type: int
    .. py:attribute:: self.__y
        The final Y coordinate of playing ground.
        :type: int
    .. py:attribute:: pos
        The tuple, which contains initial and final coordinates of
        playing ground.
        :type: tuple((int, int), (int, int))

    |
    """

    def __init__(self, scene, info_string):
        info_size = info_string.get_size()
        scene_size = scene.get_size()
        self.__x0 = 0
        self.__y0 = info_size[1] + 1
        self.__x = scene_size[0]
        self.__y = scene_size[1]
        self.__pos = ((self.__x0, self.__y0),
        (self.__x, self.__y))

    def get_pos(self):
        """This method returns the coordinates of playing ground.

        :returns: the tuple, which contains initial and final coordinates.
        :rtype: tuple((int, int), (int, int))

        |
        """
        return self.__pos

class InfoString:
    """This class describes the information string.

    METHODS

    :py:meth:`InfoString.up_score()`

    :py:meth:`InfoString.draw()`

    :py:meth:`InfoString.get_size()`

    :py:meth:`InfoString.get_score()`
    |

    ATTRIBUTES

    .. py:attribute:: h
        The height of information string.
        :type: int
    .. py:attribute:: w
        The width of information string.
        :type: int
    .. py:attribute:: size
        The tuple like (w, h)
        :type: tuple
    .. py:attribute:: score
        The current score.
        :type: int
        :value: 0
    .. py:attribute:: color
        The color of drawing information.
        :type: tuple
        :value: 255, 255, 0

    |
    """

    def __init__(self, scene, sw):
        scene_size = scene.get_size()
        self.__h = sw
        self.__w = scene_size[0]
        self.__size = (self.__w, self.__h)
        self.__score = 0
        self.__color = (255, 255, 0)

    def get_score(self):
        """This method returns the score.

        :returns: score
        :rtype: int

        |
        """

        return self.__score

    def up_score(self, value):
        """This method increases score.

        :param int value: The value of increasing score.

        |
        """

        self.__score += value

    def draw(self, scene):
        """This method renders the information line.
        :param object scene: The scene for rendering food (pygame.display).

        |
        """

        size = self.__h - self.__h // 4
        font = pygame.font.Font(None, size)
        text = "Your score: " + str(self.__score)
        message = font.render(text, True, self.__color)
        scene.blit(message, [0, 0])
        pygame.draw.line(scene, self.__color, (0, self.__h - self.__h/2),
        (self.__w, self.__h - self.__h/2))

    def get_size(self):
        """This method returns the width and the height of the info string.

        :returns: size
        :rtype: tuple(int, int)

        |
        """

        return self.__size
