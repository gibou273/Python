from turtle import Screen
from snake import Snake
from food import Food
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()


screen.listen()
screen.onkey(key="Up", fun=snake.move_up)
screen.onkey(key="Down", fun=snake.move_down)
screen.onkey(key="Left", fun=snake.move_left)
screen.onkey(key="Right", fun=snake.move_right)

is_snake_moving = True
while is_snake_moving:
    time.sleep(0.1)
    screen.update()
    snake.move_snake()
    # Detect collision with food
    if snake.snake_head.distance(food) < 15:
        food.move_food()


screen.exitonclick()