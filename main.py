# TO DO:
# Classes: paddle, ball, bricks, score
# Paddle: move left and right, detect collision with ball
# Ball: move diagonally when it hits something
# Bricks: disappear once the ball touches it
# Score: +1 for every brick

from turtle import Turtle
from paddle import Paddle
from bricks import Wall
from ball import Ball
from score import Score

t = Turtle()
t.hideturtle()
t.penup()

screen = t.screen
screen.title("Breakout")
screen.setup(width=800, height=540)
screen.tracer(0)
paddle = Paddle()
bricks = Wall()
ball = Ball()
score = Score()

# Tracks if the user is pressing the left or right buttons
left_pressed = False
right_pressed = False

def press_left():
    global left_pressed
    left_pressed = True
def release_left():
    global left_pressed
    left_pressed = False
def press_right():
    global right_pressed
    right_pressed = True
def release_right():
    global right_pressed
    right_pressed = False

screen.listen()
screen.onkeypress(press_left, "Left")
screen.onkeyrelease(release_left, "Left")
screen.onkeypress(press_right, "Right")
screen.onkeyrelease(release_right, "Right")

# Updates the screen every 16 ms
def game_loop():
    if left_pressed:
        paddle.move_left()
    if right_pressed:
        paddle.move_right()

    if ball.game_win or ball.game_lose:
        if ball.game_win:
            winner = True
        else:
            winner = False
        game_over(winner)
        return

    screen.update()
    screen.ontimer(game_loop, 16)

    ball.move(paddle=paddle, wall=bricks, score=score)

def game_over(winner):
    t.goto(0, -30)
    if winner:
        t.color("green")
        t.write("YOU WON!", font=("Impact", 50, "bold"), align="center")
    else:
        t.color("red")
        t.write("YOU LOST", font=("Impact", 50, "bold"), align="center")

game_loop()

screen.exitonclick()