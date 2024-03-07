from turtle import Turtle, Screen

turtle = Turtle()
my_screen = Screen()


my_screen.canvheight = 500
my_screen.canvwidth = 500

turtle.shape("turtle")
turtle.color("red")
turtle.forward(100)

my_screen.exitonclick()

