import turtle

NUM_CIRCLES = 360    # Количество рисуемых кругов
RADIUS = 150        # Радиус каждого круга
ANGLE = 1          # Угол поворота
ANIMATION_SPEED = 0 # Скорость анимации

turtle.speed(ANIMATION_SPEED)
turtle.bgcolor('gray')

# Нарисовать 360 кругов, наклоняя черепаху на
# 1 градусов после того, как каждый круг был нарисован

for x in range(NUM_CIRCLES):
    turtle.circle(RADIUS)
    turtle.left(ANGLE)

turtle.done()


