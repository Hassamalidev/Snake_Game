from turtle import Screen, Turtle
import time
from snake import  Snake
from food import Food
from scoreBoard import ScoreBoard
screen=Screen()
screen.bgcolor("black")
screen.setup(600,600)
screen.title("My Snake game")
screen.tracer(0)

snake=Snake()
scoreBoard=ScoreBoard()
food=Food()
screen.listen()
screen.onkey(snake.move_left,"Left")
screen.onkey(snake.move_right,"Right")
screen.onkey(snake.move_up,"Up")
screen.onkey(snake.move_down,"Down")

game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        scoreBoard.score_count()

    if snake.head.xcor() > 280  or snake.head.xcor()< -280 or snake.head.ycor() > 280 or snake.head.ycor()< -280:
        snake.reset()
        scoreBoard.reset()

    for segment in snake.all_segment:
        if segment==snake.head:
            pass
        elif snake.head.distance(segment)<10:
            scoreBoard.reset()

screen.exitonclick()


