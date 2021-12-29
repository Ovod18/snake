# Pygame шаблон - скелет для нового проекта Pygame
import pygame
import random

# Задаем ширину и высоту
WIDTH = 360    
HEIGHT = 480   
FPS = 30

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Создаем игру и окно
pygame.init()
pygame.mixer.init() # Для звука
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # Задаем размер 
#главного окна
pygame.display.set_caption("My Game") # Задаем название главного окна
clock = pygame.time.Clock() # Создаем объект типа часы

# Цикл игры
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False.quit()


    # рендеринг
    screen.fill(RED)
    # после отрисовки всего показываем каритнку на экране (переворачиваем экран)
    
    # рисуем прямоугольник белого цвета на главном окне
    pygame.draw.rect(screen, WHITE, (20, 20, 100, 75))
    # рисуем линию белого цвета на главном окне
    pygame.draw.line(screen, WHITE, [10, 30], [290, 15], 3)
    # обновление кадра# обновление кадра# обновление кадра                 
    pygame.display.flip()
