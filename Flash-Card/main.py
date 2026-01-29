from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT = "Ariel"

french_word =  pd.read_csv("./data/french_words.csv")
to_learn = french_word.to_dict(orient="records")
word = {}

def flip():
    canvas.itemconfig(card, image=back_photo)
    canvas.itemconfig(word_text, text=word["English"], fill="white")
    canvas.itemconfig(title_text, text="English", fill="white")

def next_card():
    global flip_timer, word
    window.after_cancel(flip_timer)
    word = random.choice(to_learn)
    canvas.itemconfig(card, image=front_photo)
    french = word['French']
    english = word['English']
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=french, fill="black")
    flip_timer = window.after(3000, flip)

window = Tk()
window.title("FlashCard")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip)

# canvas

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_photo = PhotoImage(file="./images/card_front.png")
back_photo = PhotoImage(file="./images/card_back.png")
card = canvas.create_image( 400, 263, image=front_photo)

title_text = canvas.create_text(400, 150, text="", font=(FONT, 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=(FONT, 60, "bold"))


canvas.grid(row=1,column=1, columnspan=2)

# buttons
right_photo = PhotoImage(file="./images/right.png")
right_button = Button(image=right_photo, highlightthickness=0, command=is_known)

right_button.grid(row=2, column=2)

wrong_photo = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_photo, highlightthickness=0, command=next_card)

wrong_button.grid(row=2, column=1)

next_card()

window.mainloop()