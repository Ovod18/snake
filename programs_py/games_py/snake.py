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

def main(display_width, display_height, snake_width):

    d_w = display_width
    d_h = display_height
    s_w = snake_width
    INF_HEIGHT = 40
    X_CENTRE = d_w / 2
    Y_CENTRE = d_h / 2

    """Creating the main window."""
    pygame.init()
    screen = pygame.display.set_mode((d_w, d_h))
    pygame.display.set_caption("My snake")

    clock = pygame.time.Clock()

    """Setting snakes properties"""
    my_snake = items.Snake(s_w)
    body = my_snake.get_body()
    head_pos = my_snake.get_head_pos()

    """Setting other values"""
    score = 0
    course = ""
    apple = items.Food(s_w, d_w, d_h, INF_HEIGHT)


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
            my_snake.set_course(course)
            my_snake.move()

            """Snake eats food"""
            h_pos = my_snake.get_head_pos()
            a_pos = apple.get_pos()
            a_radius = apple.get_size() / 2
            d = items.dist(a_pos, h_pos)
            if d < (s_w / 2):
                color = apple.get_color()
                my_snake.eat(apple.get_size(), color)
                score += int(apple.get_size())
                apple.set_size(s_w)
                apple.set_pos(body, s_w)
                apple.set_color()



            """Collision a border."""
            if h_pos[0] == 0:
                pos = [d_w, h_pos[1]]
                my_snake.set_pos(pos)
            elif h_pos[0] == d_w:
                pos = [0, h_pos[1]]
                my_snake.set_pos(pos)
            if h_pos[1] == INF_HEIGHT:
                pos = [h_pos[0], d_h]
                my_snake.set_pos(pos)
            elif h_pos[1] == d_h:
                pos = [h_pos[0], INF_HEIGHT]
                my_snake.set_pos(pos)

            """Wasted by collision the snakes body."""
            for i in range(s_w * 2, len(body)):
                segment = body[i]
                pos = segment.get_pos()
                d = items.dist(pos, h_pos)
                if d < s_w:
                    font = pygame.font.Font(None, 20)
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
            font = pygame.font.Font(None, 30)
            text = "Your score: " + str(score)
            message = font.render(text, True, YELLOW)
            screen.blit(message, [6, 6])

            s_rad = s_w / 2
            pygame.draw.line(screen, YELLOW, (0, INF_HEIGHT - s_rad),
                             (d_w, INF_HEIGHT - s_rad))

            for segment in body:
                pos = segment.get_pos()
                pygame.draw.circle(screen, GREEN, (pos[0], pos[1]),
                                   (s_w/2), 0)

            apple_pos = apple.get_pos()
            a_color = apple.get_color()
            pygame.draw.circle(screen, a_color, (apple_pos[0], apple_pos[1]),
                            apple.get_size()/2 , 0)

            pygame.display.update()
            clock.tick(FPS)

    pygame.quit()
