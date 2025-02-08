from turtle import Turtle
from paddle import Paddle

from scoreboard import Scoreboard

class Lives(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.lives = 5
        self.update_lives()
        self.scoreboard = Scoreboard()



    def update_lives(self):
        self.clear()
        self.goto(-500, 375)
        self.write(f"Lives: {self.lives}", align="center", font=("Courier", 30, 'italic'))


    def lose_life(self):
        self.lives -= 1
        self.update_lives()

