import turtle

n = input()
n = int(n)
a = 360/n
for i in range(1, n+1):
	turtle.shape('turtle')
	turtle.forward(100)
	turtle.stamp()
	turtle.backward(100)
	turtle.left(a)
turtle.exitonclick()
