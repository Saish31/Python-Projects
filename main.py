import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

Rpaddle = Paddle((350, 0))
Lpaddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(Rpaddle.go_up, "Up")
screen.onkey(Rpaddle.go_down, "Down")
screen.onkey(Lpaddle.go_up, "w")
screen.onkey(Lpaddle.go_down, "s")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # wall collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # paddle collision
    if ball.distance(Rpaddle) < 50 and ball.xcor() > 320 or ball.distance(Lpaddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # paddle miss
    if ball.xcor() > 380:
        scoreboard.clear()
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        scoreboard.clear()
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
