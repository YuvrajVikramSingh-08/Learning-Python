import tkinter

window = tkinter.Tk()

window.title("Mile to Km converter")
# window.title("My first GUI")
# window.minsize(width=500, height=300)

# my_label = tkinter.Label(text="I am Label", font=("Courier", 24, "bold"))
# my_label.pack()
#
# my_label["text"] = "New Text"
#
# def button_clicked():
#     content = input.get()
#     my_label.config(text=f"{content}")
#     print("I got clicked")
#
# button = tkinter.Button(text="click me", command=button_clicked)
# button.pack()
#
# input = tkinter.Entry(width=10)
# input.pack()

def convert():
    numb = float(inp.get())
    km = numb * 1.6
    ans.config(text=f"{km}")

window.config(padx=20, pady=20)

inp = tkinter.Entry(width=10)
inp.grid(row=0, column=1)

mile = tkinter.Label(text="Miles.")
mile.grid(row=0, column=2)

is_equal = tkinter.Label(text="is equal to")
is_equal.grid(row=1, column=0)

ans = tkinter.Label(text="0")
ans.grid(row=1,column=1)

km = tkinter.Label(text="Km.")
km.grid(row=1,column=2)

button = tkinter.Button(text="Calculate", command=convert)
button.grid(row=2,column=1)



window.mainloop()