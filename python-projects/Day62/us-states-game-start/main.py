import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

df = pd.read_csv("50_states.csv")
all_states = df.state.to_list()
guessed_states = []


while len(guessed_states) < 50:
    answer_state = (screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name")).title()
    print(answer_state)

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        print(f"You missed these states: {missing_states}")
        break

    if answer_state not in all_states:
        print("Not a US State")

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = df[df.state == answer_state]
        t.goto(int(state_data.x.item()), int(state_data.y.item()))
        t.write(answer_state)
    """
    If answer_state is one of the states in all the states of the 50_states.csv
        if they got it right:
            Create a turtle to write the name of the state at the state's coordinate (location) on the map image
    """


def get_mouse_click_coor(x, y):
    print(x, y)


turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()
# screen.exitonclick()
