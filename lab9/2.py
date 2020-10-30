import turtle as t
t.penup()
t.goto(-400, 100)
t.pendown()
t.shape('turtle')
t.speed(0)
t.tracer(0)
pos=[]
angle=[]
def save():
	pos.append(t.pos())
	angle.append(t.heading())
def restore():
	t.penup()
	t.goto(pos[-1])
	t.setheading(angle[-1])
	del pos[-1]
	del angle[-1]
	t.pendown()
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
	'F' : 'FF',
	'X' : 'F-[[X]+X]+F[+FX]-X',
	'+' : '+',
	'-' : '-',
	'[' : '[',
	']' : ']'
}

funcs = {
	'F' : lambda: t.forward(5),
	'-' : lambda: t.left(25),
	'+' : lambda: t.right(25),
	'[' : save,
	']' : restore
}
l = gen("X", 6)
#print(l)
for s in l:
	if s not in funcs:
		continue
	funcs[s]()


t.exitonclick()
