from tkinter import *
import pandas
import random

### CONTAINS ###
LANGUAGES: list = ["French", "English"]
BACKGROUND: str = "#B1DDC6"
TITLE: str = "Flashy"
# IMAGES: list = [
#     "001_tutorial\python\\100_days\ex31_cardGame\images\card_front.png",
#     "001_tutorial\python\\100_days\ex31_cardGame\images\card_back.png",
#     "001_tutorial\python\\100_days\ex31_cardGame\images\\wrong.png",
#     "001_tutorial\python\\100_days\ex31_cardGame\images\\right.png",
# ]
IMAGES: list = [
    "images\\card_front.png",
    "images\\card_back.png",
    "images\\wrong.png",
    "images\\right.png",
]
# DATA_FILE: str = "001_tutorial\python\\100_days\ex31_cardGame\data\\french_words.csv"
DATA_FILE: str = "data\\french_words.csv"

current_card = {}

### DATA ###
data = pandas.read_csv(DATA_FILE)
to_learn = data.to_dict("records")


### Click Button ###

def greenButton():
    global to_learn
    to_learn.remove(current_card)
    df = pandas.DataFrame(to_learn)
    df.to_csv("data\\french_words.csv", index=False)
    clickButton()


def clickButton():
    global current_card
    global flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(language_text, text="French", fill='black')
    canvas.itemconfig(word, text=current_card["French"], fill='black')
    canvas.itemconfig(canvas_image, image=card_front)
    flip_timer = window.after(2000, func=flipCard)


### timer counter ###
def flipCard():
    canvas.itemconfig(language_text, text="English", fill='white')
    canvas.itemconfig(word, text=current_card["English"], fill='white')
    canvas.itemconfig(canvas_image, image=card_back)


### UI functions ###
window = Tk()
window.title(TITLE)
window.config(padx=50, pady=50, background=BACKGROUND)
flip_timer = window.after(2000, func=flipCard)

# Image
card_front = PhotoImage(file=IMAGES[0])
card_back = PhotoImage(file=IMAGES[1])
red_img = PhotoImage(file=IMAGES[2])
green_img = PhotoImage(file=IMAGES[3])

# Canvas
canvas = Canvas(width=800, height=540, highlightthickness=0, background=BACKGROUND)
canvas_image = canvas.create_image(400, 270, image=card_front)
language_text = canvas.create_text(400, 150, font="Ariel 40 italic", text="")
word = canvas.create_text(400, 250, text="", font="Helvetica 60 bold")
canvas.grid(column=0, row=0, columnspan=2, pady=(0, 40))

# Button
red_btn = Button(image=red_img, highlightthickness=0, command=clickButton)
red_btn.grid(column=0, row=3)
green_btn = Button(image=green_img, highlightthickness=0, command=greenButton)
green_btn.grid(column=1, row=3)

clickButton()

window.mainloop()
