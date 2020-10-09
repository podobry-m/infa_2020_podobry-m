import turtle

turtle.shape('turtle')

for k in range(10):
	for i in range(4):
		turtle.forward(50 * (k + 1))
		turtle.left(90)
	turtle.right(90)
	turtle.penup()
	turtle.forward(25)
	turtle.right(90)
	turtle.forward(25)
	turtle.right(180)
	turtle.pendown()
