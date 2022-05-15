from turtle import Turtle


class LineaMedioCampo(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.speed("fastest")
        self.pensize(3)
        self.goto(0, 300)
        self.goto(0, -300)
