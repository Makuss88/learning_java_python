from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color('white')
        self.penup()
        self.goto(x=x_pos, y=y_pos)

    def up(self):
        y_cor = self.ycor()
        self.setposition((self.xcor(), y_cor + 20))

    def down(self):
        y_cor = self.ycor()
        self.setposition((self.xcor(), y_cor - 20))
