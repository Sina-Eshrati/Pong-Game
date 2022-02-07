from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.show_score()

    def show_score(self):
        self.clear()
        self.goto(-100, 230)
        self.write(self.l_score, align="center", font=("courier", 50, "normal"))
        self.goto(100, 230)
        self.write(self.r_score, align="center", font=("courier", 50, "normal"))

