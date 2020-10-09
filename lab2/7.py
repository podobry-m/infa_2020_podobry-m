import turtle
import numpy as m
turtle.shape('turtle')
turtle.speed(0)
n = 2000
fi = 0
for i in range(n):
	turtle.forward(m.sqrt(1 + i * i) / 200)
	turtle.left(2)
turtle.exitonclick()
