from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.turtles = []
        x = 0
        for _ in range(3):
            tur = Turtle(shape="square")
            tur.color("white")
            tur.penup()
            # tur.speed("slowest")
            tur.goto(x, 00)
            x += -20
            self.turtles.append(tur)

    def move(self):
        for num in range(len(self.turtles) - 1, 0, -1):
            new_x = self.turtles[num - 1].xcor()
            new_y = self.turtles[num - 1].ycor()
            self.turtles[num].goto(new_x, new_y)
        self.turtles[0].forward(20)

    def add_tail(self):
        tur = Turtle(shape="square")
        tur.color("white")
        tur.penup()
        length = len(self.turtles)
        pos = self.turtles[length - 1].position()
        tur.goto(pos[0], pos[1])
        self.turtles.append(tur)

    def check(self):
        length = len(self.turtles)
        for n in range(1, length - 1):
            if self.turtles[0].distance(self.turtles[n]) < 1:
                return True

    def up(self):
        if self.turtles[0].heading() != DOWN:
            self.turtles[0].setheading(UP)

    def down(self):
        if self.turtles[0].heading() != UP:
            self.turtles[0].setheading(DOWN)

    def right(self):
        if self.turtles[0].heading() != LEFT:
            self.turtles[0].setheading(RIGHT)

    def left(self):
        if self.turtles[0].heading() != RIGHT:
            self.turtles[0].setheading(LEFT)
