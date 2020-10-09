import turtle as t
import math

l=30
l2=l*math.sqrt(2)
ind=[
	(0, 0, l, 90, 2 * l, 90, l, 90, 2 * l, 90), 
	(l, 90, 2 * l,135, l2, 135), 
	(l, 180, l,-135, l2, 45, l, 90, l, 180),
	(0, 45, l2, 135, l, -135, l2, 135, l, 180),
	(l,90, 2*l, 180, l, -90, l, -90, l, -90),
	(0, 0, l, 90, l, 90, l, -90, l, -90, l),
	(0, 0, l, 90, l, 90, l, 90, l, 180, l, -45, l2, -45),
	(0, 90, l, -45, l2, 135, l, 180),
	(0, 0, l, 90, 2*l, 90, l, 90, 2*l, 180, l, -90, l),
	(0, 45, l2, 45, l, 90, l, 90, l, 90, l)
]
inp = open('input.txt', 'r')
number = inp.read().rstrip()
inp.close()

for k, digit in enumerate(number):
	t.penup()
	t.goto((k-len(number)/2)*(l+10),0)
	t.pendown();
	n = ind[int(digit)]
	t.penup()
	t.forward(n[0])
	t.left(n[1])
	t.pendown()
	for j in range(2, len(n)):
		if (j%2==0):
			t.forward(n[j])
		else:
			t.left(n[j])
t.exitonclick()
	

