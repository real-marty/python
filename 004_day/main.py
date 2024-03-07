from turtle import Turtle, Screen
import heroes 
import random

turtle = Turtle()

turtle.speed(0)

def line(angle):
    turtle.forward(15)
    turtle.right(angle)
    print(heroes.gen())


turtle.shape("turtle")


# random wal
for i in range(4, 1000):
    for _ in range(i):
        turtle.pencolor(random.random(), random.random(), random.random())
        turtle.pensize(5)
        line(random.choice([90, 180, 270, 360]))







screen = Screen()
screen.exitonclick()


