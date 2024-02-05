from turtle import Turtle

POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():
    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.snake_head = self.snake_segments[0]
    def create_snake(self):
        for position in POSITIONS:
            new_snake = Turtle()
            new_snake.shape("square")
            new_snake.color("white")
            new_snake.penup()
            new_snake.goto(position)
            self.snake_segments.append(new_snake)
    def move_snake(self):
        for segment_num in range(len(self.snake_segments) - 1, 0, -1):
            new_posX = self.snake_segments[segment_num - 1].xcor()
            new_posY = self.snake_segments[segment_num - 1].ycor()
            self.snake_segments[segment_num].goto(x=new_posX, y=new_posY)
        self.snake_head.forward(20)
    def move_up(self):
        if self.snake_head.heading != DOWN:
            self.snake_head.setheading(UP)
    def move_down(self):
        if self.snake_head.heading != UP:
            self.snake_head.setheading(DOWN)
    def move_left(self):
        if self.snake_head.heading != RIGHT:
            self.snake_head.setheading(LEFT)
    def move_right(self):
        if self.snake_head.heading != LEFT:
            self.snake_head.setheading(RIGHT)