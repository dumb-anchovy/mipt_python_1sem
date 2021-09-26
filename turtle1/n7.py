import turtle
import math

k = 1
a = 0.1
for i in range(1000):
	r = k*a
	x = math.cos(a)*r
	y = math.sin(a)*r
	turtle.goto(x, y)
	a += 0.1
turtle.exitonclick()
