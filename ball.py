from turtle import Turtle
import time

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("black", "#D3D3D3")
        self.speed("fastest")
        self.goto(0, -178)
        self.setheading(45)
        self.move_speed = 10
        self.game_lose = False
        self.game_win = False

    def move(self, paddle, wall, score):
        self.forward(self.move_speed)

        # When it hits the wall
        if self.xcor() >= 372:
            self.setx(372)
            self.setheading(180 - self.heading())

        elif self.xcor() <= -372:
            self.setx(-372)
            self.setheading(180 - self.heading())

        # When it hits the bricks
        for brick in wall.bricks:
            if self.distance(brick) <= 25:
                self.setheading(360 - self.heading())
                wall.bricks.remove(brick)
                score.add_score()
                self.move_speed += 0.2
                brick.hideturtle()
                break

        # Calculate direction and angle of ball when it the paddle
        if self.ycor() <= paddle.ycor() + 20 and abs(self.xcor() - paddle.xcor()) < 60 and self.heading() > 180:
            self.sety(paddle.ycor() + 25)
            self.setheading(360 - self.heading())

        # When player misses the ball
        if self.ycor() < -230:
            self.ball_reset(paddle, score)

        # If player wins
        if not wall.bricks:
            self.game_win = True

    def ball_reset(self, paddle, score):
        if score.lose_life():
            self.game_lose = True
        self.goto(0, -178)
        paddle.goto(0, -200)
        self.setheading(45)
        self.move_speed = 10
        time.sleep(1)
        
