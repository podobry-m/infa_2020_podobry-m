import turtle

turtle.shape('turtle')
n=15
for i in range(n):
	turtle.forward(200)
	turtle.right(180)
	turtle.forward(200)
	turtle.left(180 - 360 / n)
	
