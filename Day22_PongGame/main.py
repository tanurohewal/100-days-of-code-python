from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("#0f172a")
screen.setup(height=600, width=800)
screen.title("🔥 PONG PRO GAME 🔥")
screen.tracer(0)

#center line making
line = Turtle()
line.color("white")
line.penup()
line.goto(0, 300)
line.setheading(270)
line.hideturtle()

for _ in range(30):
    line.pendown()
    line.forward(10)
    line.penup()
    line.forward(10)

r_paddle = Paddle((370, 0))
l_paddle = Paddle((-370, 0))

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #detect the collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #detect R paddle misses
    if  ball.xcor() > 400:
        ball.reset_position()
        scoreboard.l_point()

    # detect L paddle misses
    if ball.xcor() < -400:
        ball.reset_position()
        scoreboard.r_point()






