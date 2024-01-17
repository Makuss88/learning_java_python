from tkinter import *
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_place.delete(0, END)
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []
    for char in range(1, 7):
        password_list += random.choice(letters)
    for char in range(1, 3):
        password_list += random.choice(symbols)
    for char in range(1, 3):
        password_list += random.choice(numbers)
    random.shuffle(password_list)
    password = "".join(password_list)

    password_place.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():

    web = website_place.get()
    user = user_place.get()
    password = password_place.get()

    if len(web) == 0 and len(password) == 0:
        messagebox.showinfo(message="OMG! empty??")
    else:
        is_ok = messagebox.askokcancel(title="check!", message=f"web = {web} \npassword = {password}")
        if is_ok:
            with open("my_password.txt", mode="a") as f:
                f.write(f"{web} | {user} | {password}\n")
                website_place.delete(0, END)
                password_place.delete(0, END)


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
user_place.insert(0, "makuss@gmail.com")

password_txt = Label(text="Password")
password_txt.grid(column=0, row=3)
password_place = Entry(width=18)
password_place.grid(column=1, row=3)

generate_btn = Button(text="Generate", command=generate_password, width=14)
generate_btn.grid(column=2, row=3)

add_btn = Button(text="Add", command=add_password, width=30)
add_btn.grid(column=1, row=4, columnspan=2)

window.mainloop()
