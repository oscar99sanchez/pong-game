from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()

    def move(self, grado):
        self.setheading(grado)
        self.forward(10)

    def end(self):
        self.goto(0, 600)
