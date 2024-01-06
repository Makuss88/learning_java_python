from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt') as f:
            self.high_score = int(f.read())
        self.penup()
        self.goto(0, 250)
        self.color('aqua')
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}  High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode='w') as f:
                f.write(str(self.high_score))
        self.score = 0
        self.update_score()

    def add_score(self):
        self.score += 1
        self.update_score()
