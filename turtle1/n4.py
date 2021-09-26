import turtle
import math

def crcl(R):
    for i in range(360):
        turtle.forward(math.pi * (R/180))
        turtle.left(1)

turtle.shape('turtle')
turtle.speed(0)
crcl(50)
turtle.exitonclick()
