from turtle import Screen
import time
from food import Food
from snake import Snake
from scoreboard import Scoreboard

screen=Screen()
screen.setup(width=600, height=600)

screen.tracer(0)

screen.bgcolor("black")
screen.title("Joc Snake")

snake=Snake()
food=Food()
scoreboard=Scoreboard()

#5 sus 90
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    #Detecteaza coliziunea
    if snake.head.distance(food)<15:
        food.refresh()
        scoreboard.inscrease_score()
        snake.extend()
    #Detecteaza_coliziunea cu peretii
    if snake.head.xcor() > 280 or snake.head.xcor() < - 280 or snake.head.ycor() > 280 or snake.head.ycor() < - 280:
        scoreboard.reset()
        snake.reset()

    #Detecteaza coliziunea cu coada
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()