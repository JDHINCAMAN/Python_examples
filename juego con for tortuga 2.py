# lespiralcuadrada.py - esto es un comentario. dibujare una espural cuadrada
import turtle
t = turtle.Pen()
colors = ["blue", "yellow", "red", "purple"]
for x in range (1000):
    t.pencolor(colors[x%4])
    t.forward(x)
    t.left(89)
