from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

game_is_on = True
screen = Screen()
screen.tracer(0)
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.listen()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-360, 0))
ball = Ball()
score_board = ScoreBoard()

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    if ball.ycor() > 288 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.xcor() > 335 and ball.distance(r_paddle) < 45 or ball.xcor() < -345 and ball.distance(l_paddle) < 45:
        ball.bounce_x()
    if ball.xcor() > 400:
        ball.reset()
        score_board.l_score += 1
        score_board.show_score()
    if ball.xcor() < -410:
        ball.reset()
        score_board.r_score += 1
        score_board.show_score()
    screen.onkeypress(r_paddle.move_up, "Up")
    screen.onkeypress(r_paddle.move_down, "Down")
    screen.onkeypress(l_paddle.move_up, "w")
    screen.onkeypress(l_paddle.move_down, "s")


screen.exitonclick()
