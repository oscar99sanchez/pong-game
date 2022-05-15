from turtle import Turtle


class Barra:
    def __init__(self, position_x):
        barra = Turtle("square")
        barra.color("red")
        barra.speed("fastest")
        barra.turtlesize(1, 3)
        barra.penup()
        barra.goto(position_x, 0)
        barra.setheading(90)
        self.barra = barra

    def up(self):
        if self.barra.heading() == 90:
            self.barra.forward(40)
        else:
            self.barra.setheading(90)
            self.barra.forward(40)

    def down(self):

        if self.barra.heading() == -90:
            self.barra.forward(40)
        else:
            self.barra.setheading(-90)
            self.barra.forward(40)
