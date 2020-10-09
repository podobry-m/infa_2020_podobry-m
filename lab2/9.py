import turtle as t
import numpy as np
t.shape('turtle')
def f(n,r):
	t.penup()
	t.forward(20)
	t.pendown()
	t.left(90)
	for j in range(n):
		t.left(360 / n)
		t.forward(2 * r * np.sin(np.pi / n))
	t.left(90)
	t.penup()
	t.forward(20)
	t.left(180)
		
		

for i in range(3, 13):
	t.forward(20)
	f(i, 20 * i)
	
