import turtle as t

t.shape('turtle')
t.tracer(False)

def d(r):
	n=180
	for i in range(n):
		t.forward(r)
		t.right(180 / n)
t.penup()		
t.goto(-300,0)
t.pendown()
t.left(90)
for k in range(50):
	d(1)
	d(1/4)

t.exitonclick()
