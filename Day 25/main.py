import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.tracer(0)

tim = turtle.Turtle()
tim.hideturtle()
tim.penup()

data = pd.read_csv("50_states.csv")
states = data.state.to_list()

total_correct_guess = 0
guessed_states = []

game_on = True

while game_on:
    answer_state = screen.textinput(title=f"{total_correct_guess}/50 State Correct: ", prompt="What's another state's name: ")
    if answer_state.title() in states and answer_state not in guessed_states:
        guessed_states.append(answer_state.title())
        total_correct_guess += 1
        x = int(data[data["state"] == answer_state.title()]["x"].item())
        y = int(data[data["state"] == answer_state.title()]["y"].item())
        tim.goto(x, y)
        tim.write(arg=f"{answer_state.title()}")
    if total_correct_guess == 50:
        game_on = False
    if answer_state == "off":
        states_not_guessed = []
        for state in states:
            if state not in guessed_states:
                states_not_guessed.append(state)

        st = {"states": states_not_guessed}

        learn_State = pd.DataFrame(st)
        learn_State.to_csv("learn.csv")
        game_on = False
    screen.update()

turtle.mainloop()