from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, cord):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(x=cord[0], y=cord[1])

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(y=new_y, x=self.xcor())

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(y=new_y, x=self.xcor())
