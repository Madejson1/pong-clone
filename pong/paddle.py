from turtle import Turtle
SCREENHEIGHT = 800
SCREENWIDTH = 1000
UP = 90
DOWN = 270
SPEED = 20

PLAYERXCOR = 480

MOVE_DISTANCE = 20

# for player on the right xcord = 480, left =-480
class Paddle:
    def __init__(self, xcord):
        self.xcord = xcord
        self.x = 0
        self.blocks = []
        self.create_paddle()
        self.upper = self.blocks[0]
        self.going_up = False
        self.going_down = False


    def create_paddle(self):
        while self.x > -61:
            paddle = Turtle("square")
            paddle.color("white")
            paddle.penup()
            paddle.speed("fastest")
            paddle.goto(self.xcord, 40 + self.x)
            self. x -= 20
            paddle.speed("normal")
            self.blocks.append(paddle)

    def move(self):
        if self.going_up:
            for i in range(len(self.blocks)):
                new_x = self.blocks[i].xcor()
                new_y = self.blocks[i].ycor() + SPEED
                self.blocks[i].goto(new_x, new_y)
                if self.blocks[i].ycor() > SCREENHEIGHT/2 :
                    self.going_up = False
                    self.going_down = True

        elif self.going_down:
            for i in range(len(self.blocks)):
                new_x = self.blocks[i].xcor()
                new_y = self.blocks[i].ycor() - SPEED
                self.blocks[i].goto(new_x, new_y)
                if self.blocks[i].ycor() < - SCREENHEIGHT/2 :
                    self.going_up = True
                    self.going_down = False


    def up(self):
        self.going_up = True
        self.going_down = False

    def down(self):
        self.going_down = True
        self.going_up = False

    def get_blocks(self):
        return self.blocks

    def check_bounce(self):
        for block in self.get_blocks():
            if block.ycor() > SCREENHEIGHT:
                self.going_down = True
                self.going_up = False


