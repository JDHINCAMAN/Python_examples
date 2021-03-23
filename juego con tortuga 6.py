import turtle
t = turtle.Pen()
turtle.bgcolor("black")
colors = ["red", "blue", "yellow", "green"]
lados = int(4)
for n in range (lados):
    t.pencolor(colors[n%4])
    t.pendown()
    t.circle(60)
    t.right(360/lados)
for m in range (5,75):
    t.pencolor(colors[m%4])
    t.left(360/lados + 5)
    t.width(m//25+1)
    t.penup()
    t.forward(m*4)
    t.pendown()
    if(m%2==0):
        for n in range(lados):
                       t.circle(m/3)
                       t.right(360/lados)
    else:
        for n in range(lados):
            t.forward(m)
            t.right(360/lados)
            
