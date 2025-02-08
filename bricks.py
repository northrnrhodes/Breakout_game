from turtle import Turtle
import random

COLOR = ["white", "blue", "green", "red", "orange", "purple", "yellow", "cyan", "indigo", "crimson", "grey"]

positions = [(-550, 50), (-450, 50), (-350, 50), (-250, 50), (-150, 50), (-50, 50), (50, 50), (150, 50),
             (250, 50), (350, 50), (450, 50), (550, 50),
             (-550, 100), (-450, 100), (-350, 100), (-250, 100), (-150, 100), (-50, 100),
             (50, 100), (150, 100), (250, 100), (350, 100), (450, 100), (550, 100),
             (-550, 150), (-450, 150), (-350, 150), (-250, 150),
             (-150, 150), (-50, 150), (50, 150), (150, 150), (250, 150), (350, 150), (450, 150), (550, 150),
             (-550, 200), (-450, 200), (-350, 200), (-250, 200), (-150, 200), (-50, 200), (50, 200), (150, 200),
             (250, 200), (350, 200), (450, 200), (550, 200)]

class Bricks:
    def __init__(self):
        super().__init__()
        self.all_bricks = []



    def spawn_bricks(self):
        for i in positions:
            new_brick = Turtle("square")
            new_brick.color(random.choice(COLOR))
            new_brick.penup()
            new_brick.goto(i)
            new_brick.shapesize(2, 5)
            self.all_bricks.append(new_brick)

