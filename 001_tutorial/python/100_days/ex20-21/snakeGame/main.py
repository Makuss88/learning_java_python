import time
from turtle import Screen
from Snake import Snake

snake = Snake()

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake game")
screen.tracer(0)
screen.listen()
screen.onkey(fun=snake.up, key='Up')
screen.onkey(fun=snake.down, key='Down')
screen.onkey(fun=snake.left, key='Left')
screen.onkey(fun=snake.right, key='Right')


is_game = True

while is_game:
    screen.update()
    time.sleep(0.1)
    snake.moving()

screen.exitonclick()
