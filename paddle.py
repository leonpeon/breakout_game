from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("purple")
        self.shapesize(1, 5)
        self.goto(0, -200)
        self.move_units = 10

    def move_left(self):
        if -320 <= self.xcor() <= 320:
            self.forward(-self.move_units)
        elif 320 <= self.xcor() <= 380:
            self.forward(-self.move_units)

    def move_right(self):
        if -320 <= self.xcor() <= 320:
            self.forward(self.move_units)
        elif -380 <= self.xcor() <= -320:
            self.forward(self.move_units)