from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()
screen.setup(width = 500, height= 400)
user_bet = screen.textinput(title = "Make your bet: ", prompt = "Which turtle will win the race? Enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
# tim = {}
# for i in range(len(colors)):
#     tim["col_{colors(i)}"] = Turtle(shape = "turtle")
#     tim["col_{colors(i)}"].color(colors[i])
#     tim["col_{colors(i)}"].penup()
#     tim["col_{colors(i)}"].shape()
#     tim["col_{colors(i)}"].goto(x=-230, y=-150 + 60*i)

all_turtle = []
for turtle_ind in range(len(colors)):
    tim = Turtle(shape = "turtle")
    tim.penup()
    tim.color(colors[turtle_ind])
    tim.goto(x = -230,y = -150 + 60*turtle_ind)
    all_turtle.append(tim)


if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtle:
         if turtle.xcor() > 230:
             is_race_on = False
             winning_color = turtle.pencolor()
             if winning_color == user_bet:
                 print(f"You've won! The {winning_color} turtle is the winner!")
             else:
                 print(f"You've lost! The {winning_color} turtle is the winner!")
         rand_distance = random.randint(0, 10)
         turtle.forward(rand_distance)

screen.exitonclick()