from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-35, 240)
        self.score = 0
        self.write(f"Score: {self.score}", font=("Consolas", 14, "normal"))

    def add_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", font=("Consolas", 14, "normal"))