from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letter = [random.choice(letters) for char in range(nr_letters)]
    password_symbols = [random.choice(symbols) for char in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for char in range(nr_numbers)]

    password_list = password_letter + password_symbols + password_numbers

    random.shuffle(password_list)

    password_ = "".join(password_list)
    pyperclip.copy(password_)
    pass_ent.insert(0, password_)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_pass():
    website = web_ent.get()
    email = email_ent.get()
    password = pass_ent.get()


    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="OOPS", message="Please don't leave any field empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}"
                                                  f"\nPassword: {password} \nIs it ok to Save? ")
        if is_ok:
            form = f"{website} | {email} | {password}\n"
            with open("data.txt", "a") as data:
                data.write(form)
                web_ent.delete(0, END)
                pass_ent.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image( 100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Label
web_label = Label(text="Website: ")
web_label.grid(row=1, column=0)

email_label = Label(text="Username/Email: ")
email_label.grid(row=2, column=0)

pass_label = Label(text="Password: ")
pass_label.grid(row=3, column=0)

#Entries
web_ent = Entry(width=36)
web_ent.grid(row=1, column=1, columnspan=2)
web_ent.focus()

email_ent = Entry(width=36)
email_ent.grid(row=2, column=1, columnspan=2)
email_ent.insert(0, "dummy_mail@gmail.com")

pass_ent = Entry(width=20)
pass_ent.grid(row=3, column=1)

#buttons
gen_b = Button(text="Generate Password", width=13, command=generate_pass)
add_b = Button(text="Add", width=36, command = add_pass)

gen_b.grid(row=3, column=2)
add_b.grid(row=4, column=1, columnspan=2)

window.mainloop()