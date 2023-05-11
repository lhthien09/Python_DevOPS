import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)
guessed_states = []

df = pandas.read_csv("50_states.csv")


while len(guessed_states) < 50:
        answer_state = screen.textinput(title = f"{len(guessed_states)}/50 states",
                                        prompt = "What's another state's name?").title()
        all_state = df.state.to_list()
        if answer_state == "Exit":
            missing_states = []
            for state in all_state:
                if state not in guessed_states:
                    missing_states.append(state)
            new_data = pandas.DataFrame(missing_states)
            new_data.to_csv("State_to_learn.csv")
            break
        if answer_state in all_state:
            guessed_states.append(answer_state)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = df[df.state == answer_state]
            t.goto(int(state_data.x), int(state_data.y))
            t.write(answer_state)


turtle.mainloop()

