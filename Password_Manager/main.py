from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_pass():
    website = web_ent.get()
    email = email_ent.get()
    password = pass_ent.get()
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
gen_b = Button(text="Generate Password", width=13)
add_b = Button(text="Add", width=36, command = add_pass)

gen_b.grid(row=3, column=2)
add_b.grid(row=4, column=1, columnspan=2)

window.mainloop()