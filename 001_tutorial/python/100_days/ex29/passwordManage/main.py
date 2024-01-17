from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    pass


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    with open('my_password.txt', mode='a') as f:
        f.write(f"{website_place.get()} | {user_place.get()} | {password_place.get()}\n")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, bg="red", highlightthickness=0)
password_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_img)
canvas.grid(column=0, row=0, columnspan=3)


website_txt = Label(text="Website")
website_txt.grid(column=0, row=1)
website_place = Entry(width=36)
website_place.grid(column=1, row=1, columnspan=2)


user_txt = Label(text="User")
user_txt.grid(column=0, row=2)
user_place = Entry(width=36)
user_place.grid(column=1, row=2, columnspan=2)


password_txt = Label(text="Password")
password_txt.grid(column=0, row=3)
password_place = Entry(width=18)
password_place.grid(column=1, row=3)

generate_btn = Button(text="Generate", command=generate_password, width=14)
generate_btn.grid(column=2, row=3)

add_btn = Button(text="Add", command=add_password, width=30)
add_btn.grid(column=1, row=4, columnspan=2)

window.mainloop()
