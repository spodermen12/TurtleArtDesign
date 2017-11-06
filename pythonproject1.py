import turtle
from mystar import *
bob = turtle.Turtle()
bob.speed(0)

turtle.bgcolor("black")

for times in range(500):
    bob.penup()
    bob.color("white")
    polygon(bob,50,3)
    bob.forward(times)
    bob.left(41)
    bob.pendown()

    bob.penup()
    bob.color("blue")
    polygon(bob,50,3)
    bob.forward(times)
    bob.left(41)
    bob.pendown()

    bob.penup()
    bob.color("yellow")
    polygon(bob,50,3)
    bob.forward(times)
    bob.left(41)
    bob.pendown()

    bob.penup()
    bob.color("red")
    polygon(bob,50,3)
    bob.forward(times)
    bob.left(41)
    bob.pendown()
    
