from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def clockwise():
    tim.setheading(tim.heading() - 5)

def ant_clockwise():
    tim.setheading(tim.heading() + 5)

def clear():
    tim.penup()
    tim.clear()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="a", fun=ant_clockwise)
screen.onkey(key="c", fun=clear)

screen.exitonclick()