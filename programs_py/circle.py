import turtle

NUM_CIRCLES = 20
STARTING_RADIUS =20
OFFSET = 10
ANIMATION_SPEED = 10

turtle.speed(ANIMATION_SPEED)

radius = STARTING_RADIUS

turtle.bgcolor('gray')

for count in range(NUM_CIRCLES):
    turtle.circle(radius)

    x = turtle.xcor()
    y = turtle.ycor() - OFFSET

    radius = radius + OFFSET

    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

turtle.done()

