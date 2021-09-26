import turtle

for l in range(10, 210, 20):
	turtle.shape('turtle')
	turtle.forward(l)
	turtle.left(90)
	turtle.forward(l)
	turtle.left(90)
	turtle.forward(l)
	turtle.left(90)
	turtle.forward(l)
	turtle.penup()
	turtle.forward(10)
	turtle.left(90)
	turtle.backward(10)
	turtle.pendown()
turtle.exitonclick()
