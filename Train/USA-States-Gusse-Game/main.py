'''
Hello there this is name of states of USA gussing game, play and learn about State names of USA. 
This game is developed with python turtle, pandas, csv and others.
'''

import turtle
import pandas
import csv

#Setting up background and other front end tools for the game
screen = turtle.Screen()
screen.title("U.S State Gusse Game")
image = "./blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

#Checking weather the user gusssed the correct state or not
states = pandas.read_csv("./50_states.csv")
state = states["state"].to_list()
learn = state
gussed_states = []
while len(gussed_states) < 50:
    answer = screen.textinput(title=f"😜{len(gussed_states)}/50 states Gussed😜", prompt="Enter the state...").title()
    if answer == "Exit":
        break
    if answer in state:
        learn.remove(answer)
        gussed_states.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = states[states.state == answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer)

#Change ungussed states into UnGussed-States.csv file
states_dict = {
    "States" : learn,
}
df = pandas.DataFrame(states_dict)
df.to_csv("UnGussed-States.csv")