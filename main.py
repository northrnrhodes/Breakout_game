from turtle import Turtle, Screen
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball
from lives import Lives
from bricks import Bricks
import time
import random


screen = Screen()
screen.bgcolor("black")
screen.setup(width=1200, height=1000)
screen.title("Breakout Game!")
screen.tracer(0)


paddle = Paddle((0, -380))
paddle.speed("fastest")
scoreboard = Scoreboard()
ball = Ball()
lives = Lives()


screen.listen()
screen.onkey(paddle.go_left, "Left")
screen.onkey(paddle.go_right, "Right")

bricks = Bricks()
bricks.spawn_bricks()
game_on = True
screen.update()
time.sleep(1)
dropping = True

skip = False
while game_on:
    scoreboard.update_score()
    if skip == True and dropping == True:
        ball.bounce()

    for brick in bricks.all_bricks:
        if brick.distance(ball) < 50:
            brick.hideturtle()
            scoreboard.score += 1
            scoreboard.update_score()
            bricks.all_bricks.remove(brick)
            ball.bounce()
            screen.update()

    if len(bricks.all_bricks) == 0:
        game_on = False

    while dropping:
        screen.update()
        time.sleep(ball.pace)
        ball.drop()

        if ball.ycor() < -360 and ball.distance(paddle) < 120:
            dropping = False



        if ball.ycor() < -390 and lives.lives > 0:
            lives.lose_life()
            paddle.reset_paddle()

            if lives.lives == 0:
                ball.hideturtle()
                paddle.hideturtle()
                dropping = False
                game_on = False
                skip = True

            ball.reset_position()
            screen.update()
            if skip == False:
                time.sleep(1)

        if lives.lives == 0:
            ball.hideturtle()
            paddle.hideturtle()
            dropping = False
            game_on = False


    if dropping == False:
        ball.move()
        screen.update()
        time.sleep(ball.pace)

    if ball.ycor() < -385:
        lives.lose_life()
        ball.reset_position()
        paddle.reset_paddle()
        time.sleep(1)
        dropping = True
        skip = True

    #detects hitting top of screen
    if ball.ycor() > 395:
        ball.bounce()
    #detects hitting sides of screen
    if ball.xcor() > 580 or ball.xcor() < -580:
        ball.reverse()
    #detects collision with paddle
    if ball.ycor() < -360 and ball.distance(paddle) < 120:
        ball.bounce()


    if lives.lives == 0:
        game_on = False


screen.clearscreen()
screen.bgcolor("black")
scoreboard.game_over()
screen.exitonclick()