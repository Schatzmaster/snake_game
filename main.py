from turtle import Screen
import time
from Snake import Snake
from food import Food
from scoreboard import Scoreboard

# Setup screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
point = 0

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_runs = True
while game_runs:
    screen.update()
    # Updates the screen every 0.1 second
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 300 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset_snake()

    # Detect collision with tail
    for segment in snake.all_segments[4:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset_snake()

screen.exitonclick()
