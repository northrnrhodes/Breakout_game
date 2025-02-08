from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(1, 12)
        self.goto(position)




    def go_right(self):
        x_cor = self.xcor() + 40
        if x_cor < 500:
            self.goto(x_cor, self.ycor())


    def go_left(self):
        x_cor = self.xcor() - 40
        if x_cor > -500:
            self.goto(x_cor, self.ycor())


    def reset_paddle(self):
        self.goto((0, -380))