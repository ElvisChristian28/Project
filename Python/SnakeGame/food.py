from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.speed("fastest")
        self.add_food()
    def add_food(self):
        x = random.randint(-480,480)
        y = random.randint(-280,250)
        self.goto(x,y)
        self.color("white")
