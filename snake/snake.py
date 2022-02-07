"""This module contains the main function of 'snake' game"""

import pygame
import random
import time
import math
import items

FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

def main(display_width, display_height, snake_width, snake_speed):
    """
    The main function of 'snake' game.

    Parameters
    ----------
    display_width, display_height, snake_width, snake_speed : int

    See Also
    --------
    module items
    """

    dw = display_width
    dh = display_height
    sw = snake_width
    ss = snake_speed
    INF_HEIGHT = sw
    X_CENTRE = dw / 2
    Y_CENTRE = dh / 2
    crit_l = dw * ((dh-INF_HEIGHT)//sw*4)

    """Creating the main window."""
    pygame.init()
    screen = pygame.display.set_mode((dw, dh))
    pygame.display.set_caption("My snake")

    clock = pygame.time.Clock()

    """Setting snakes properties"""
    my_snake = items.Snake(sw)
    body = my_snake.get_body()
    head_pos = my_snake.get_head_pos()

    """Setting other values"""
    score = 0
    course = ""
    apple = items.Food(sw, dw, dh, INF_HEIGHT)


    """ Creating the game cycle."""
    state = "running"
    while state != "quit":
        """Keys binding"""
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                state = "quit"
            if event.type == pygame.KEYDOWN:
                if (event.key==pygame.K_LEFT) and (course!="RIGHT"):
                    course = "LEFT"
                elif (event.key==pygame.K_RIGHT) and (course!="LEFT"):
                    course = "RIGHT"
                elif (event.key==pygame.K_UP) and (course!="DOWN"):
                    course = "UP"
                elif (event.key==pygame.K_DOWN) and (course!="UP"):
                    course = "DOWN"
                elif event.key == pygame.K_ESCAPE:
                    state = "pause"
                elif event.key == pygame.K_r:
                    state = "running"

        if state == "running":

            """Snake movement"""
            my_snake.set_course(course, ss)
            my_snake.move()

            """Snake eats food"""
            h_pos = my_snake.get_head_pos()
            a_pos = apple.get_pos()
            a_radius = apple.get_size() / 2
            d = items.dist(a_pos, h_pos)
            if d < (sw / 2):
                color = apple.get_color()
                my_snake.eat(apple.get_size(), color)
                score += int(apple.get_size())
                if (len(my_snake.get_body()) < crit_l):
                    apple.set_size(sw, "r")
                else:
                    apple.set_size(sw, 0)
                apple.set_pos(body, sw)
                apple.set_color()

            """Collision a border."""
            if h_pos[0] <= 0:
                pos = [dw, h_pos[1]]
                my_snake.set_pos(pos)
            elif h_pos[0] >= dw:
                pos = [0, h_pos[1]]
                my_snake.set_pos(pos)
            if h_pos[1] <= INF_HEIGHT:
                pos = [h_pos[0], dh]
                my_snake.set_pos(pos)
            elif h_pos[1] >= dh:
                pos = [h_pos[0], INF_HEIGHT]
                my_snake.set_pos(pos)

            """Wasted by collision the snakes body."""
            for i in range(sw * 2, len(body)):
                segment = body[i]
                pos = segment.get_pos()
                d = items.dist(pos, h_pos)
                if d < sw:
                    font = pygame.font.Font(None, sw)
                    text = "Your score: " + str(score)
                    message = font.render(text, True, RED)
                    screen.blit(message, [X_CENTRE, Y_CENTRE])
                    pygame.display.update()
                    time.sleep(5)
                    state = "quit"
                    break

            """Frame out to the screen."""
            screen.fill(BLACK)

            """Showing current informatoin"""
            size = sw - sw // 4
            font = pygame.font.Font(None, size)
            text = "Your score: " + str(score)
            message = font.render(text, True, YELLOW)
            screen.blit(message, [0, 0])

            s_rad = sw / 2
            pygame.draw.line(screen, YELLOW, (0, INF_HEIGHT - s_rad),
                             (dw, INF_HEIGHT - s_rad))

            """Rendering snake"""
            for segment in body:
                pos = segment.get_pos()
                color = segment.get_color()
                pygame.draw.circle(screen, color, (pos[0], pos[1]),
                                   (sw/2), 0)

            """Rendering food"""
            apple_pos = apple.get_pos()
            a_color = apple.get_color()
            pygame.draw.circle(screen, a_color, (apple_pos[0], apple_pos[1]),
                            apple.get_size()/2 , 0)

            pygame.display.update()
            clock.tick(FPS)

    pygame.quit()
