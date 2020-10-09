from random import randint
import turtle
import math
X=turtle.window_width()
Y=turtle.window_height()
K=0.01
number_of_turtles = 10
steps_of_time_number = 1000


pool = [turtle.Turtle(shape='circle') for i in range(number_of_turtles)]
v = [[randint(-4, 4), randint(-4, 4)] for _ in range(number_of_turtles)]
for unit in pool:
    unit.penup()
    unit.speed(0)
    unit.goto(randint(-200, 200), randint(-200, 200))


for i in range(steps_of_time_number):
	for j in range(number_of_turtles):
		unit = pool[j]
		pos = unit.pos()
		for unit1 in pool:
			if (unit1!=unit):
				dx=(unit1.pos()[0]-unit.pos()[0])
				dy=(unit1.pos()[1]-unit.pos()[1])
				d=math.sqrt(dx**2+dy**2)
				v[j][0]-= K/((d/30)**3)*dx
				v[j][1]-= K/((d/30)**3)*dy
		if (pos[0]<=-X/2 or pos[0]>=X/2):
			v[j][0]*=-1
		if (pos[1]<=-Y/2 or pos[1]>=Y/2):
			v[j][1]*=-1
		
		unit.goto(pos+v[j])
