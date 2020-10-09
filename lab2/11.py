import turtle

turtle.shape('turtle')
turtle.tracer(False)
n = 500
turtle.left(90)
for k in range(7):
	for i in range(n):
		turtle.forward((k+1)/10)
		turtle.left(360/n)
	turtle.left(180)
	for i in range(n):
		turtle.forward((k+1)/10)
		turtle.left(360/n)
turtle.exitonclick()
