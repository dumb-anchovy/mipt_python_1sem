import turtle as t
from random import *

t.speed(10)
for i in range(1000):
    t.left(randint(0, 360))
    t.forward(randint(1, 100))
t.exitonclick()
