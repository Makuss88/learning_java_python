from turtle import Turtle

START_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in START_POSITION:
            self.add_body(position)

    def moving(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            x_pos = self.segments[seg_num - 1].xcor()
            y_pos = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x_pos, y_pos)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def add_body(self, position):
        tim = Turtle('square')
        tim.penup()
        tim.color('white')
        tim.speed(1)
        tim.goto(position)
        self.segments.append(tim)

    def expend(self):
        self.add_body(self.segments[-1].position())

    def reset(self):
        for seg in self.segments:
            seg.goto((1000, 1000))
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
