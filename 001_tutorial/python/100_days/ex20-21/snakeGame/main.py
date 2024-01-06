import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
snake = Snake()
food = Food()
score = Scoreboard()

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

    # detect the collision.
    if snake.head.distance(food) < 19:
        food.refresh()
        snake.expend()
        score.add_score()

    # detect the wall.
    if abs(snake.head.xcor()) > 280 or abs(snake.head.ycor()) > 280:
        score.reset_score()
        snake.reset()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset_score()
            snake.reset()
screen.exitonclick()
