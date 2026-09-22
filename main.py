from turtle import Turtle, Screen
from random import randint

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="User bet", prompt="Which turtle color will win the race? Enter a color: ")

colors = ["red", "blue", "yellow", "green", "orange", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]

all_turtles = []
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()

            if winning_color == user_bet:
                print(f"You've won ! The winnig color is: {winning_color}")
            else:
                print(f"You've lost ! The winnig color is: {winning_color}")

        rand_distance = randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()