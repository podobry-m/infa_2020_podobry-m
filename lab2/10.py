import turtle

turtle.shape('turtle')
turtle.tracer(False)
n = 500
j = 8
for k in range(j):
	for i in range(n):
		turtle.forward(1)
		turtle.left(360/n)
	turtle.right(360 / j)
turtle.exitonclick()
