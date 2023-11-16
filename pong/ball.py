from turtle import Turtle
import math
from paddle import Paddle
XSPEED = 10
YSPEED = -10
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed(0)
        self.goto(0, 0)
        self.dx = XSPEED
        self.dy = YSPEED

    def move(self):
        self.setx(self.xcor() + self.dx)
        self.sety(self.ycor() + self.dy)

    def bounce_off_paddle(self, paddle):
        for block in paddle.get_blocks():
            if (
                    block.ycor() - 10 <= self.ycor() <= block.ycor() + 10
                    and block.xcor() - 10 <= self.xcor() <= block.xcor() + 10
            ):
                angle = math.atan2(self.dy, self.dx)
                angle = math.pi - angle
                speed = math.sqrt(self.dx ** 2 + self.dy ** 2)
                self.dx = speed * math.cos(angle)
                self.dy = speed * math.sin(angle)