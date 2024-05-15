from turtle import Screen
from snakeclass import Snake
from food import Food
from scoreboard import ScoreBoard
import time
p1 = ScoreBoard()
s1 = Snake()
screen = Screen()
screen.setup(width=1000, height=600)
screen.bgcolor("black")
screen.title("Welcome to Snake Game")
screen.tracer(0)
is_game_on = True
toeat = Food()
# screen.onkey(fun=turn_left, key="a")
screen.listen()
screen.onkey(s1.up, "Up")
screen.onkey(s1.down, "Down")
screen.onkey(s1.right, "Right")
screen.onkey(s1.left, "Left")
while is_game_on:
    screen.update()
    time.sleep(0.1)
    s1.move()
    if s1.turtles[0].distance(toeat) < 25:
        toeat.add_food()
        s1.add_tail()
        p1.update_score()
    if s1.turtles[0].xcor() > 480 or s1.turtles[0].xcor() < -500 or s1.turtles[0].ycor() > 250 or s1.turtles[0].ycor() <-280:
        # s1.turtles[0].left(90)
        p1.gameover()
        break
    is_yes = s1.check()
    if is_yes:
        p1.gameover()
        break
screen.exitonclick()
