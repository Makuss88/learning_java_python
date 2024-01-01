# import random
import random
import turtle as t
from turtle import Turtle, Screen
# import colorgram

t.colormode(255)
tim = Turtle()
tim.speed(0)
tim.penup()
tim.goto(-225, -225)
tim.hideturtle()

# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# colors = ['red', 'blue', 'yellow', 'green', 'black', 'pink', 'aqua', 'orange', 'navy', 'brown']
#
# for shape in range(3, 11):
#     tim.color(random.choice(colors))
#     for _ in range(shape):
#         tim.forward(100)
#         tim.right(360/shape)
#     shape += 1


# def choice_turn():
#     how_many = random.choice([0, 1, 2, 3])
#     for _ in range(how_many):
#         tim.right(90)
#     tim.forward(50)


# def random_color():
#     r = random.randint(0, 225)
#     b = random.randint(0, 225)
#     g = random.randint(0, 225)
#     color = (r, b, g)
#     return color


# colors = ['red', 'blue', 'yellow', 'green', 'black', 'pink', 'aqua', 'orange', 'navy', 'brown']
# tim.pensize(15)
# tim.forward(30)


# for _ in range(100):
#     tup = random_color()
#     tim.pencolor(tup)
#     choice_turn()

# for _ in range(100):
#     tim.color(random_color())
#     tim.circle(100)
#     tim.left(360 / 100)


# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

def go_back():
    tim.left(90)
    tim.fd(50)
    tim.left(90)
    tim.fd(500)
    tim.left(180)


color_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20),
              (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70),
              (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74),
              (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153),
              (176, 192, 208), (168, 99, 102)]

for _ in range(10):
    for _ in range(10):
        color = random.choice(color_list)
        tim.dot(20, color)
        tim.forward(50)
    go_back()

screen = Screen()
screen.exitonclick()
