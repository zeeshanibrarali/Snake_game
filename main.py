import turtle
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
src = Screen()


src.bgcolor('black')
src.title("MY SNAKE GAME")
turtle.setup(width=600, height=600)
src.tracer(0)

snake = Snake()
food = Food()
src.listen()

src.onkey(snake.up, 'Up')
src.onkey(snake.down, 'Down')
src.onkey(snake.right, 'Right')
src.onkey(snake.left, 'Left')
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    src.update()
    time.sleep(0.1)
    snake.move()
    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.ycor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail
    for segment in snake.all_turtles[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

src.exitonclick()

