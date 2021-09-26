import math
import turtle

def pg(n, R):
	k = 0
	n = int(n)
	a = math.radians(360/n)
	c = math.cos(a)
	l = (2 * (1-c) * R**2) ** 0.5
	ang = 180 - 180*(n-2)/n
	ang1 = 180 * (n-2) / (2*n)
	turtle.shape('turtle')
	turtle.left(ang + ang1)
	while (k < n):
		turtle.forward(l)
		turtle.left(ang)
		k += 1
	turtle.right(ang + ang1)

q = 3
r = 15
while (q < 14):
	pg(q, r)
	turtle.penup()
	turtle.forward(15)
	turtle.pendown()
	q += 1
	r += 15
turtle.exitonclick()
