import time
from turtle import Screen
from paddle import Paddle


user_paddle = Paddle(-350, 0)
comp_paddle = Paddle(350, 0)

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("pong")
screen.tracer(0)
screen.listen()
screen.onkey(user_paddle.up, 'Up')
screen.onkey(user_paddle.down, 'Down')


is_game = True
while is_game:
    screen.update()
    time.sleep(0.1)

screen.exitonclick()
