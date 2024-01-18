from turtle import Turtle

STARTING_POSNS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for posn in STARTING_POSNS:
            self.addsegment(posn)

    def addsegment(self,posn):
        seg = Turtle("square")
        seg.color("white")
        seg.penup()
        seg.goto(posn)
        self.segments.append(seg)

    def extend(self):
        self.addsegment(self.segments[-1].position())

    def move(self):
        for segno in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segno - 1].xcor()
            new_y = self.segments[segno - 1].ycor()
            self.segments[segno].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)


