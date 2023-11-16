from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import math
import time
SCREENHEIGHT = 800
SCREENWIDTH = 1000
screen = Screen()
screen.setup(width=SCREENWIDTH, height=SCREENHEIGHT)
screen.bgcolor("black")
screen.tracer(0)
paddle_right = Paddle(xcord=480)
screen.listen()
screen.onkey(paddle_right.up, "Up")
screen.onkey(paddle_right.down, "Down")
paddle_left = Paddle(xcord=-480)
screen.onkey(paddle_left.up, "w")
screen.onkey(paddle_left.down, "s")
ball = Ball()
score_left = Scoreboard(s_xcord=-250, s_ycord=350)
score_right = Scoreboard(s_xcord=250, s_ycord=350)
for i in range(1,27):
    score_right.create_middle_blocks(mid_ycord=400)
game_is_on = True

while game_is_on:
    paddle_right.move()
    paddle_left.move()
    ball.move()
    time.sleep(0.05)
    screen.update()
    ball.bounce_off_paddle(paddle_left)
    ball.bounce_off_paddle(paddle_right)
    if ball.ycor() > (SCREENHEIGHT / 2 - 20):
        ball.dy *= -1
    elif ball.ycor() < (-SCREENHEIGHT / 2 + 20):
        ball.dy *= -1

    if ball.xcor() > (SCREENWIDTH/2):
        score_left.increase_score()
        ball.home()
        ball.dx *= -1
    elif ball.xcor() < (-SCREENWIDTH/2):
        score_right.increase_score()
        ball.home()
        ball.dx *= -1
    if score_right.score > 5 or score_left.score > 5:
        score_right.game_over()
        game_is_on = False






























screen.exitonclick()