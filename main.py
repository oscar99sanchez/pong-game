from turtle import Screen
from tablero import LineaMedioCampo
from barra import Barra
from pelota import Ball
from score import Scoreboard
import random

import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("silver")
screen.tracer(0)

score = Scoreboard(200, 200)
score2 = Scoreboard(-200, 200)
linea_medio_campo = LineaMedioCampo()
ball = Ball()
barra = Barra(350)
barra2 = Barra(-350)


# grado = random.randint(-80, 80)
grado = 45
game_is_on = True
while game_is_on:
    screen.update()
    screen.listen()
    screen.onkeypress(barra.up, "w")
    screen.onkeypress(barra.down, "s")
    screen.onkeypress(barra2.up, "o")
    screen.onkeypress(barra2.down, "l")
    screen.onkeypress(ball.end, "k")

    time.sleep(0.02)
    ball.move(grado)

    if ball.ycor() >= 600:
        game_is_on = False
        score.game_over()

    if ball.xcor() > 340 or ball.xcor() < -340:
        if ball.xcor() > 340:
            score2.increase_score()
        if ball.xcor() < -340:
            score.increase_score()

        ball.goto(0, 0)

    else:
        if ball.ycor() > 290 or ball.ycor() < -290:
            grado = grado * -1
            print(grado)

        # grados del rebote para la barra derecha
        if ball.xcor() > barra.barra.xcor() - 20 and barra.barra.ycor() + 50 > ball.ycor() > barra.barra.ycor() - 40:
            if -1 > grado > - 89 and barra.barra.ycor() + 50 > ball.ycor() > barra.barra.ycor():
                grado = random.randint(110, 160)
                print(grado)

            if -1 > grado > - 89 and barra.barra.ycor() > ball.ycor() > barra.barra.ycor() - 50:
                grado = random.randint(-160, -110)
                print(grado)

            if 89 > grado > 1 and barra.barra.ycor() + 50 > ball.ycor() > barra.barra.ycor():
                grado = random.randint(110, 160)
                print(grado)

            if 89 > grado > 1 and barra.barra.ycor() > ball.ycor() > barra.barra.ycor() - 50:
                grado = random.randint(-160, -110)
                print(grado)

        # grados del rebote para la barra izquierda
        if ball.xcor() < barra2.barra.xcor() + 20 and barra2.barra.ycor() + 50 > ball.ycor() > barra2.barra.ycor() - 50:
            if -91 > grado > - 179 and barra2.barra.ycor() + 50 > ball.ycor() > barra2.barra.ycor():

                grado = random.randint(20, 70)
                print(grado)

            if -91 > grado > - 179 and barra2.barra.ycor() > ball.ycor() > barra2.barra.ycor() - 50:
                grado = random.randint(-80, -20)
                print(grado)

            if 179 > grado > 91 and barra2.barra.ycor() + 50 > ball.ycor() > barra2.barra.ycor():
                grado = random.randint(20, 70)
                print(grado)

            if 179 > grado > 91 and barra2.barra.ycor() > ball.ycor() > barra2.barra.ycor() - 50:
                grado = random.randint(-80, -20)
                print(grado)

screen.exitonclick()
