from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.penup()
        self.restart()
        self.setheading(90)

    def go_up(self):
        newy = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), newy)

    def restart(self):
        self.goto(STARTING_POSITION)

    def success(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
