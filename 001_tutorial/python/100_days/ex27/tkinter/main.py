from tkinter import *

window = Tk()

window.title("GUI")
window.minsize(width=600, height=400)

my_label = Label(text="my Label", font=("Arial", 24, "bold"))
my_label.pack()

my_label["text"] = "new text"

input_place = Entry(background="aqua")
input_place.pack()


def click():
    new_title = input_place.get()
    my_label.config(text=new_title)


button = Button(text="clil", command=lambda: click())
button.pack()


window.mainloop()
