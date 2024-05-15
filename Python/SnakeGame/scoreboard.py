from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.color("White")
        self.update_score()

    def update_score(self):
        self.penup()
        self.clear()
        self.goto(0,270)
        self.write(f"Score : {self.score}", False, align="center", font=("Protest Guerrilla", 20, "normal"))
        self.score += 1
        self.goto(-500,250)
        self.pendown()
        self.goto(500,250)


    def gameover(self):
        self.goto(0, 0)
        self.write(f"Game Over!!", False, align="center", font=("Protest Guerrilla", 50, "normal"))