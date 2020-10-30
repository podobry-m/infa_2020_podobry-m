import turtle
turtle.penup()
turtle.goto(-400,-300)
turtle.pendown()
turtle.shape('turtle')
turtle.speed(0)
turtle.tracer(0)
def gen(start, n):
	l = start
	l_new = ""
	for i in range(n):
		for s in l:
			l_new += rules[s]
		l = l_new
		l_new = ""
	return l
rules = {
	'F' : 'F+F-F-F+F',
	'-' : '-',
	'+' : '+',
}

funcs = {
	'F' : lambda: turtle.forward(15),
	'+' : lambda: turtle.left(90),
	'-' : lambda: turtle.right(90),
}
l = gen("F", 4)
#print(l)
for s in l:
	funcs[s]()


turtle.exitonclick()
