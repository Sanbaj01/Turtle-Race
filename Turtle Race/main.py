from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()
def move_forwards():
    tim.setheading(0)
    tim.forward(10)
def move_backwards():
    tim.setheading(180)
    tim.forward(10)
def move_left():
    tim.left(10)
    tim.forward(10)
def move_right():
    tim.right(10)
    tim.forward(10)
def clear():
    tim.home()
    tim.clear()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=clear)

screen.exitonclick()