# lespiralcuadrada.py - esto es un comentario. dibujare una espural cuadrada
import turtle
t = turtle.Pen()
colors = ["blue", "yellow", "red", "purple", "orange", "green", "grey", "pink"]
for x in range (1000):
    t.pencolor(colors[x%6])
    t.forward(x)
    t.left(75)
    t.forward(x)
    t.right (96)
