import turtle as t
from random import randint

t.penup()
t.goto(-200, -200)
t.pendown()
t.goto(200, -200)
t.goto(200, 200)
t.goto(-200, 200)
t.goto(-200, -200)

number_of_turtles = 10
steps_of_the_time_number = 10000

pool = [t.Turtle(shape='circle') for i in range(number_of_turtles)]
for unit in pool:
    unit.turtlesize(0.4)
    unit.penup()
    unit.speed(randint(0, 10))
    unit.goto(randint(-200, 200), randint(-200, 200))
    unit.seth(randint(0, 360))

for i in range(steps_of_the_time_number):
    for j in range(len(pool)):
        ang = pool[j].heading()
        (x, y) = pool[j].pos()
        if x < -200 or x > 200:
            pool[j].seth(180 - ang)
        elif y <= -200 or y >= 200:
            pool[j].seth(-ang)
        pool[j].forward(5)
