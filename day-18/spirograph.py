import turtle as t
import random

timmy = t.Turtle()
t.colormode(255)
timmy.speed("fastest")

def spirograph():
    for i in range(0, 360, 5):
        r_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        timmy.pencolor(r_color)
        timmy.setheading(i)
        timmy.circle(80)

spirograph()

screen = t.Screen()
screen.exitonclick()