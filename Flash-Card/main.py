from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
FONT = "Ariel"

window = Tk()
window.title("FlashCard")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# canvas

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_photo = PhotoImage(file="./images/card_front.png")
back_photo = PhotoImage(file="./images/card_back.png")
canvas.create_image( 400, 263, image=front_photo)

canvas.grid(row=1,column=1, columnspan=2)

# buttons
right_photo = PhotoImage(file="./images/right.png")
right_button = Button(image=right_photo)

right_button.grid(row=2, column=2)

wrong_photo = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_photo)

wrong_button.grid(row=2, column=1)


window.mainloop()