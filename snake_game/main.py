from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

#setting up the background
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

#initializing objects
snake = Snake()
food = Food()
score = Scoreboard()


#code for arrow keys
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

#start of the game
game_on = True
while game_on:
    screen.update()
    time.sleep(0.11)

    snake.move()

    #detect food collision
    if snake.head.distance(food) < 15:
        food.refresh()
        score.add_Score()
        snake.extend()
        time.sleep(0.05)
    
    #detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.reset()
        snake.reset()

    #detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()

screen.exitonclick()