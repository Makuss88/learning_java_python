import random
from turtle import Turtle


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color('green')
        self.shape('circle')
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.refresh()

    def refresh(self):
        x_pos = random.randint(-280, 280)
        y_pos = random.randint(-280, 280)
        self.goto(int(x_pos / 20) * 20, int(y_pos / 20) * 20)
