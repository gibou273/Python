from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
POSITIONS = [-150, -100, -50, 0, 50, 100, 150]

class Runners:
    def __init__(self):
        self.all_turtles = []
        self.create_turtles()
    def create_turtles(self):
        for i in range(0, 7):
            new_turtle = Turtle()
            new_turtle.shape("turtle")
            new_turtle.color(COLORS[i])
            new_turtle.penup()
            new_turtle.goto(x=-380, y=POSITIONS[i])
            self.all_turtles.append(new_turtle)
