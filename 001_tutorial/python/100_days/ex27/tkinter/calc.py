from tkinter import *

window = Tk()

window.title("GUI")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)


def click():
    new = 1.6 * float(input_place.get())
    is_text.config(text=new)


input_place = Entry(width=7)
input_place.grid(column=1, row=0)

miles_text = Label(text="miles")
miles_text.grid(column=2, row=0)

sec_text = Label(text="is equal to ")
sec_text.grid(column=0, row=1)

is_text = Label(text="0")
is_text.grid(column=1, row=1)

km_text = Label(text="km")
km_text.grid(column=2, row=1)

button = Button(text="calculate", command=click)
button.grid(column=1, row=2)

window.mainloop()
