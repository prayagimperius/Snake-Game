from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Verdana", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.color("white")
        self.write(arg=f'Score:{self.score} High Score: {self.high_score}', align=ALIGNMENT, font=FONT)

    def update(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Score:{self.score} High Score: {self.high_score}", align="center", font=("Verdana", 24, "normal"))

    def resset(self):
        if self.score > self.high_score:
            self.high_score = self.score

        self.score = 0
