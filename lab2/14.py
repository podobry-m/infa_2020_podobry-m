import turtle as t

t.shape('turtle')
def z(n):
	for k in range(n):
		t.forward(200)
		t.right(180 - 180 / n)
t.penup()
t.goto(-300,0)
t.pendown()
z(5)
t.penup()
t.goto(200,0)
t.pendown()

z(11)

t.exitonclick();

