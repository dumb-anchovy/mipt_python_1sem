import turtle as t

a = []
with open("n3.txt", "r") as f:
    a = f.readlines()

al = []
for i in range(10):
    s = a[i]
    k = [int(x) for x in s.split()]
    al.append(k)


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
