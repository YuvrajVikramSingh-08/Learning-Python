import turtle as t
import random

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

tim = t.Turtle()
tim.penup()
tim.speed("fastest")
t.colormode(255)

screen = t.Screen()
screen.setup(width=400, height=400)
tim.sety(-180)

def x_pattern():
    tim.setx(-180)
    for i in range(0,200, 10):
        tim.dot(10, random_color())
        tim.forward(20)


def draw_pattern():
    for i in range(0, 200, 10):
        x_pattern()
        tim.sety(tim.ycor() + 20)

draw_pattern()

screen.exitonclick()