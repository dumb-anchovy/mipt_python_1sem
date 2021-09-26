import turtle

turtle.shape('turtle')
for i in range(10, 300+1, 10):
	turtle.forward(i)
	turtle.left(90)
	turtle.forward(i)
	turtle.left(90)
turtle.exitonclick()
