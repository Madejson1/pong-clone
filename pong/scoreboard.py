from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 15, "bold")
FONT2 = ("Courier", 20, "bold")

class Scoreboard(Turtle):
    def __init__(self, s_xcord, s_ycord):
        self.score = 0
        super().__init__()
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.goto(s_xcord, s_ycord)
        self.hideturtle()
        self.update_scoreboard()
        self.substractor = 0

    def update_scoreboard(self):
        self.write(f"{self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def create_middle_blocks(self, mid_ycord,):
        mid = Turtle("square")
        mid.color("white")
        mid.penup()
        mid.shapesize(stretch_len=0.5, stretch_wid=0.5)
        mid.speed("fastest")
        mid.goto(0, mid_ycord + self.substractor)
        self.substractor -= 40
    def game_over(self):
        self.write("GAME OVER CHRISTOPHER", align=ALIGNMENT, font=FONT2)





