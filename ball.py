from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.goto(0, 0)
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.pace = 0.02



    def move(self):
        xcor = self.xcor()
        ycor = self.ycor()
        self.goto((xcor + self.x_move), (ycor + self.y_move))




    def drop(self):
        xcor = self.xcor()
        ycor = self.ycor()
        self.goto((xcor), (ycor - self.y_move))



    def bounce(self):
        self.y_move *= -1
        # self.pace *= 0.9


    def reverse(self):
        self.x_move *= -1
        # self.pace *= 0.9


    def reset_position(self):
        self.home()
        # self.drop()
