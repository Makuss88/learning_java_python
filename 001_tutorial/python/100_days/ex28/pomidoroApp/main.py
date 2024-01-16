import math
from tkinter import *
import time

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 5
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 4
rest = 0
# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global rest
    rest += 1
    work_sec = WORK_MIN * 60
    long_sec = LONG_BREAK_MIN * 60
    short_sec = SHORT_BREAK_MIN * 60

    if rest % 8 == 0:
        counting(LONG_BREAK_MIN)
        timer_txt.config(text="break", fg=PINK)
    elif rest % 2 == 0:
        counting(SHORT_BREAK_MIN)
        timer_txt.config(text="many break", fg="aqua")
    elif rest % 2 == 1:
        counting(WORK_MIN)
        timer_txt.config(text="WORK!", fg="brown")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def counting(count: int):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    canvas.itemconfig(
        timer_text, text=f'{"{:02d}".format(count_min)}:{"{:02d}".format(count_sec)}'
    )
    if count > 0:
        window.after(1000, counting, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100, bg=GREEN)

timer_txt = Label(text="Timer", fg=RED, font=(FONT_NAME, 35), bg=GREEN)
timer_txt.grid(column=1, row=0)

canvas = Canvas(width=200, height=223, bg=GREEN, highlightthickness=0)
tomate_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 111, image=tomate_img)
timer_text = canvas.create_text(
    102, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
)
canvas.grid(column=1, row=1)

start_btn = Button(text="Start", command=start_timer)
start_btn.grid(column=0, row=2)

ok_txt = Label(text="✔", fg=PINK, font=(FONT_NAME, 20, "bold"), bg=GREEN)
ok_txt.grid(column=1, row=2)

reset_btn = Button(text="Reset")
reset_btn.grid(column=2, row=2)

window.mainloop()
