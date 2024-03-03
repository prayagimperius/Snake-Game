from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("Black")
screen.title("My snake Game")
screen.tracer(0)
game_on = True

snake = Snake()
food = Food()
score = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_on:
    screen.update()
    time.sleep(0.12)
    snake.move()

    if snake.head.distance(food) < 13:
        food.refresh()
        snake.extend()
        score.update()

    if snake.head.xcor() > 280 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.resset()
        game_on = False

## HAVE TO ADD DAY 24 THINGS TO THIS CLASS

    for segment in snake.segments[1:]:


        if snake.head.distance(segment) < 10:

            score.resset()

            game_on = False

screen.exitonclick()
