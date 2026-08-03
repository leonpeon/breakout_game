from turtle import Turtle

class Brick(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(1, 2)
        self.color("light blue")
        self.start_x = -362
        self.start_y = 220
        self.goto(self.start_x, self.start_y)

class Wall():
    def __init__(self):
        self.bricks = []
        self.create_wall()

    def create_wall(self):
        colours = ["#F6511D", "#FFB400", "#00A6ED", "#7FB800", "#0D2C54"]
        for n in range(0, 5):
            y_add = n * 25
            for i in range(17):
                brick = Brick()
                brick.color(colours[n])
                brick.goto(brick.start_x + i * 45, brick.start_y - y_add)
                self.bricks.append(brick)