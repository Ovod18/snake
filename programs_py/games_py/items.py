import random
import math

def dist(a, b):
    d = math.sqrt((b[0] - a[0])**2 +(b[1] - a[1])**2)
    return d

class Snake:
    def __init__(self, snake_width):
        self.__pos_change = [0, 0]
        self.__segment_pos = [[100, 100]]
        self.__width = snake_width
        self.__course = "empty"

    def set_course(self, course):
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
        self.__segment_pos[0] = pos


    def eat(self, food_size):
        for i in range(food_size):
            pos = self.__segment_pos[-1]
            x = pos[0] - self.__pos_change[0]
            y = pos[1] - self.__pos_change[1]
            buff = [x, y]
            self.__segment_pos.append(buff)

    def get_course(self):
        return self.__course

    def get_head_pos(self):
        return self.__segment_pos[0]

    def get_body(self):
        return self.__segment_pos

class Food:
    def __init__(self, snake_width, display_width, display_height, inf_height):
        self.size_factor = 4
        self.__size = snake_width // self.size_factor
        self.d_w = display_width
        self.d_h = display_height
        self.inf_height = inf_height
        self.__x = random.randrange(self.__size, self.d_w)
        self.__y = random.randrange(self.__size + inf_height, self.d_h)
        self.__pos = [self.__x, self.__y]

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def set_size(self, snake_width):
        min_size = snake_width // self.size_factor
        max_size = snake_width
        self.__size = random.randrange(min_size, max_size + 1, 1)

    def set_pos(self, excl, snake_width):
        s_w = snake_width
        near = s_w / 2 + self.__size
        pos_valid = False
        while 1 < 2:
            count = 0
            x = random.randrange(self.__size, (self.d_w-self.__size))
            y = random.randrange(self.inf_height + self.__size,
                                 (self.d_h-self.__size))
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

    def get_size(self):
        return self.__size

    def get_pos(self):
        return self.__pos

    def get_space(self):
        x0 = self.__x - self.__radius
        y0 = self.__y - self.__radius
        self.__space = [[x0, y0]]
        for i in range(self.__size):
            for j in range(self.__size):
                self.__space.append([x0+i, y0+j])
        return self.__space
