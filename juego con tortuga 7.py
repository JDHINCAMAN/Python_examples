import turtle
t = turtle.Pen()
turtle.bgcolor ("black")
colors = ["red", "blue", "yellow", "green"]
for x in range(100):
    t.pencolor(colors[x%4])
    t.forward(x)
    t.left(91)
    t.backward(x)
    t.left(89)
    t.penup()
    t.forward(x*2)
    t.pendown()


colors = ["orange", "purple", "pink", "white"]
for y in range(100):
    t.pencolor(colors[y%4])
    t.penup()
    t.forward(y*5)
    t.pendown()
    t.forward(y)
    t.left(91)


colors = ["red", "purple", "blue", "white"]
for z in range(100):
    t.pencolor(colors[z%4])
    t.penup()
    t.backward(z*5)
    t.pendown()
    t.forward(z)
    t.left(89)    

    
