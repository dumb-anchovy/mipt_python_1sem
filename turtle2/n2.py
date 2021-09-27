import turtle as t

a0 = [0, 0, 40, 0, 0, -80, -40, 0, 0, 80, 0, 0]
a1 = [0, -40, 40, 40, 0, -80, -40, 80]
a2 = [0, 0, 40, 0, 0, -40, -40, -40, 40, 0, -40, 80]
a3 = [0, 0, 40, 0, -40, -40, 40, 0, -40, -40, 0, 80]
a4 = [0, 0, 0, -40, 40, 0, 0, -40, 0, 80, -40, 0]
a5 = [40, 0, -40, 0, 0, -40, 40, 0, 0, -40, -40, 0, 0, 80]
a6 = [40, 0, -40, -40, 0, -40, 40, 0, 0, 40, -40, 0, 0, 40]
a7 = [0, 0, 40, 0, -40, -40, 0, -40, 0, 80]
a8 = [0, 0, 40, 0, 0, -40, -40, 0, 0, -40, 40, 0, 0, 40, -40, 0, 0, 40, 0, 0]
a9 = [0, -80, 40, 40, 0, 40, -40, 0, 0, -40, 40, 0, -40, 40]

al = [a0, a1, a2, a3, a4, a5, a6, a7, a8, a9]


def ch(a):
    x = t.xcor()
    y = t.ycor()
    for n in range(0, len(a), 2):
        if (n == 0) or (n == len(a) - 2):
            x += a[n]
            y += a[n + 1]
            t.penup()
            t.goto(x, y)
            t.pendown()
        else:
            x += a[n]
            y += a[n + 1]
            t.goto(x, y)


x = -370
y = 0
t.penup()
t.goto(x, y)
t.pendown()
#141700
k = [1, 4, 1, 7, 0, 0]
for j in k:
    ch(al[j])
    x = t.xcor()
    y = t.ycor()
    t.penup()
    t.goto(x + 80, y)
    t.pendown()
t.exitonclick()
