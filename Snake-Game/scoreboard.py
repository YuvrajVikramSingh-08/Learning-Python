from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Verdana", 15, "bold")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=270)
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.highscore}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset_board(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.update_scoreboard()
