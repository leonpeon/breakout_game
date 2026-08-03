from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-135, 240)
        self.score = 0
        self.lives = 3
        self.update_info()

    def update_info(self):
        self.clear()
        self.write(f"Score: {self.score}           Lives: {self.lives}", font=("Consolas", 14, "normal"))

    def add_score(self):
        self.score += 1
        self.update_info()

    def lose_life(self):
        self.lives -= 1
        self.update_info()
        if self.lives == 0:
            return True
        else:
            return False