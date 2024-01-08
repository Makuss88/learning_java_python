import turtle

import pandas
import pandas as pd

screen = turtle.Screen()
screen.title("U.S.A. Game")
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
states = data.state.to_list()

counter = 0
how_many = len(data)
guesses_answer = []

is_game = True
while is_game:
    answer_state = screen.textinput(title=f"{counter}/{how_many} the state",
                                    prompt="another state").title()
    if answer_state == "Exit":
        missing_state = []
        for state in states:
            if state not in guesses_answer:
                missing_state.append(state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("state_to_learn.csv")
        break

    if answer_state in states:
        guesses_answer.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        row = data[data.state == answer_state]
        t.goto(int(row.x), int(row.y))
        t.write(answer_state)
        counter += 1
    if counter == 50:
        print('Bay bay')
        is_game = False

