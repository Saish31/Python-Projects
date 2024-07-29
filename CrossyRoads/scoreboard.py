from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level=1
        self.hideturtle()
        self.penup()
        self.goto(-260,260)
        self.update()

    def update(self):
        self.clear()
        self.write(f"Level {self.level}", align="left", font=FONT)

    def increase_level(self):
        self.level+=1
        self.update()

    def gameover(self):
        self.clear()
        self.goto(-100,0)
        self.write(f"Game Over\nFinal Level {self.level}", align="left", font=FONT)
