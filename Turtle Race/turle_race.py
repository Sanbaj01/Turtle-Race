from turtle import Turtle, Screen
from random import randint

race_is_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter ac color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_postions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_postions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    race_is_on = True
while race_is_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race_is_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won! The color of winning turtle is {winning_color}.")
            else:
                print(f"You lost! The {winning_color} turtle won.")

        turtle.forward(randint(0, 10))


screen.exitonclick()
