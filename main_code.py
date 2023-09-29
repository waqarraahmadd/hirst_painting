import turtle
from turtle import Turtle, Screen
import random

colors = [
    (202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40),
    (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148),
    (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171),
    (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100),
    (107, 127, 153), (174, 94, 97), (176, 192, 209)
]

simba = Turtle()
simba.penup()
simba.hideturtle()
simba.seth(225)
simba.forward(300)
simba.seth(0)
turtle.colormode(255)
simba.speed("fastest")


def forward_jump():
    for _ in range(10):
        simba.pendown()
        random_color = random.choice(colors)
        simba.dot(20, random_color)
        simba.penup()
        simba.forward(50)


def high_jump():
    simba.left(90)
    simba.forward(50)
    simba.left(90)
    simba.forward(500)
    simba.seth(0)


for x in range(10):
    forward_jump()
    high_jump()

screen = Screen()
screen.exitonclick()
