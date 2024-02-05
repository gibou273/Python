from turtle import Screen
from turtles import Runners
import random

screen = Screen()
screen.title("Turtle Race Game")
screen.setup(width=800, height=600)
screen.bgcolor("#eeeee4")

players = Runners()
is_race_on = True
user_pick = screen.textinput(title="Which color turtle will win?", prompt="Enter: (red,orange,green,blue,indigo or violet)").lower()


while is_race_on:
    for player in players.all_turtles:
        move_distance = random.randint(1,  10)
        player.forward(move_distance)
        # Check winner
        if player.xcor() >= 380:
            is_race_on = False
            wining_color = player.pencolor()
            # check if the wining turtle have the same color as the user picked
            if user_pick == wining_color:
                print("Congrats! You won")
            else:
                print(f"Sorry you lost, the {wining_color} turtle won the race")
        

screen.exitonclick()