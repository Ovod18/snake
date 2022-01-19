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
        step = 1
        self.__course = course
        if self.__course == "LEFT":
            self.__x_change = -step
            self.__y_change = 0
        elif self.__course == "RIGHT":
            self.__x_change = step
            self.__y_change = 0
        elif self.__course == "UP":
            self.__y_change = -step
            self.__x_change = 0
        elif self.__course == "DOWN":
            self.__y_change = step
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
        for i in range(self.__width):
            self.__body_x.append(self.__body_x[-1] - self.__x_change)
            self.__body_y.append(self.__body_y[-1] - self.__y_change)

    def get_head_space(self):
        x0 = self.__body_x[0]
        y0 = self.__body_y[0]
        self.__space = [[x0, y0]]
        for i in range(self.__width):
            for j in range(self.__width):
                self.__space.append([x0+i, y0+j])
        return self.__space

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

class CircularSnake:
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

    def eat(self):
        for i in range(self.__width):
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
    def __init__(self, food_size, display_width, display_height):
        self.__radius = food_size / 2
        self.__size = food_size
        self.__d_w = display_width
        self.__d_h = display_height
        self.__x = random.randrange(0, self.__d_w, food_size)
        self.__y = random.randrange(0, self.__d_h, food_size)
        self.__pos = [self.__x, self.__y]

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def set_pos(self):
        x = random.randrange(self.__radius, (self.__d_w-self.__radius),
                                            (self.__radius*2))
        y = random.randrange(self.__radius, (self.__d_h-self.__radius),
                                            (self.__radius*2))
        self.__pos = [x, y]

    def get_radius(self):
        return self.__radius

    def get_size(self):
        return self.__radius * 2

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
