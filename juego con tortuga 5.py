import turtle
t = turtle.Pen()
turtle.bgcolor("black")
colors = ["red", "white", "green", "blue"]
name = ("juan")
for x in range(80):
    t.pencolor(colors[x%4])
    t.penup()
    t.forward(x*4)
    t.pendown()
    t. write(name, font=("arial", int((x+4)/4), "bold"))
    t.left(95)
