from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0



    def update_score(self):
        self.clear()
        self.goto(0, 375)
        self.write(f"Score: {self.score}", align="center", font=("Courier", 30, 'normal'))


    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER. Final score: {self.score}", align="center", font=("Courier", 50, 'normal'))
