from tkinter import *
import pandas
import random

### CONTANS ###
LANAGUAGES: list = ["French", "English"]
BACKGROUND: str = "#B1DDC6"
TITLE: str = "Flashly"
IMAGES: list = [
    "001_tutorial\python\\100_days\ex31_cardGame\images\card_front.png",
    "001_tutorial\python\\100_days\ex31_cardGame\images\card_back.png",
    "001_tutorial\python\\100_days\ex31_cardGame\images\\wrong.png",
    "001_tutorial\python\\100_days\ex31_cardGame\images\\right.png",
]
DATA_FILE: str = "001_tutorial\python\\100_days\ex31_cardGame\data\\french_words.csv"

### DATA ###
data = pandas.read_csv(DATA_FILE)
df = pandas.DataFrame(data)
df_dict = df.to_dict("records")


### Click Button ###


def clickButton():
    randomNumber = random.randint(0, len(df_dict) - 1)
    randomDict = df_dict[randomNumber]
    frenchWord = randomDict["French"]
    canvas.itemconfig(word, text=frenchWord)


### UI functions ###
window = Tk()
window.title(TITLE)
window.config(padx=50, pady=50, background=BACKGROUND)


# Image
card_front = PhotoImage(file=IMAGES[0])
card_back = PhotoImage(file=IMAGES[1])
red_img = PhotoImage(file=IMAGES[2])
green_img = PhotoImage(file=IMAGES[3])

# Canvas
canvas = Canvas(width=800, height=540, highlightthickness=0, background=BACKGROUND)
canvas.create_image(400, 270, image=card_front)
languageText = canvas.create_text(
    400, 150, text=LANAGUAGES[0], fill="black", font=("Ariel 40 italic")
)
word = canvas.create_text(
    400, 250, text="partie", fill="black", font=("Helvetica 60 bold")
)
canvas.grid(column=0, row=0, columnspan=2, pady=(0, 40))

# Button
red_btn = Button(image=red_img, highlightthickness=0, command=clickButton)
red_btn.grid(column=0, row=3)
green_btn = Button(image=green_img, highlightthickness=0, command=clickButton)
green_btn.grid(column=1, row=3)


window.mainloop()
