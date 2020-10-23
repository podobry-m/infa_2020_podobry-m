from random import randrange as rnd, choice
import random
import tkinter as tk
import math
import time



root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)


class ball():
    g = 0.5
    def __init__(self, x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(['blue', 'green', 'black'])
        self.id = canv.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill=self.color
        )
        self.live = 30

    def set_coords(self):
        canv.coords(
                self.id,
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r
        )

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        
        if(self.x + self.r > 800 or self.x - self.r < 0 or self.y + self.r > 600 or self.y - self.r < 0):
            balls.remove(self)
            canv.delete(self.id)
            global points
            points-=1
            canv.itemconfig(p, text = str(points))
        else:    
            self.x += self.vx
            self.y -= self.vy
            self.vy -= self.g*z/0.03
            self.set_coords()

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if((self.x-obj.x)**2+(self.y-obj.y)**2<=(self.r+obj.r)**2):
            return True
        else:
            return False


class gun():
    f2_power = 10
    f2_on = 0
    an = 1
    def __init__(self):
        self.id = canv.create_line(20,450,50,420,width=7) 

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = ball()
        new_ball.r += 5
        self.an = math.atan((event.y-new_ball.y) / (event.x-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)*z/0.03
        new_ball.vy = - self.f2_power * math.sin(self.an)*z/0.03
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event=0):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.y-450) / (event.x-20))
        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, 20, 450,
                    20 + max(self.f2_power, 20) * math.cos(self.an),
                    450 + max(self.f2_power, 20) * math.sin(self.an)
                    )

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 70:
                self.f2_power += 1*z/0.01
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')


class target():
    
    live = 1
    def __init__(self):
        self.id = canv.create_oval(0,0,0,0)
        self.vx = random.randint (1,400)*z
        self.vy = random.randint (1,400)*z
        x = self.x = rnd(600, 780)
        y = self.y = rnd(300, 550)
        r = self.r = rnd(10, 30)
        color = self.color = 'red'
        canv.coords(self.id, x-r, y-r, x+r, y+r)
        canv.itemconfig(self.id, fill=color)

    def hit(self, points=1):
        """Попадание шарика в цель."""
        self.x = self.y = -10
        canv.delete(self.id)
        targets.remove(self)
        self.vx=self.vy=0
        
    def set_coords(self):
        canv.coords(
                self.id,
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r
        )
    def move(self):
        """Переместить цель по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        
        if(self.x + self.r > 800 or self.x - self.r < 0):
            self.vx*=-1
            
        if(self.y + self.r > 600 or self.y - self.r < 0):
            self.vy*=-1
        self.x += self.vx
        self.y -= self.vy
        self.set_coords()

N=3
points=0
p = canv.create_text(30, 30, text = str(points), font = 'Arial 15')
g1 = gun()
bullet = 0
balls = []
targets = []
z = 0.005
def new_game(event=''):
    global gun, t1, screen1, balls, bullet
    for i in range(N):
        targets.append(target())
    bullet = 0
    balls = []
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targetting)
    
    
    live = N
    while live>0:
        for t in targets:
            t.move()
        for b in balls:
            b.move()
            for t in targets:
                if b.hittest(t):
                    live -=1
                    balls.remove(b)
                    canv.delete(b.id)
                    t.hit()
                    global p, points
                    points += 1
                    canv.itemconfig(p, text = str(points))
                
        canv.update()
        time.sleep(z)
        g1.targetting()
        g1.power_up()
    for b in balls:
        canv.delete(b.id)
    balls=[]
    canv.delete(gun)
    new_game()


new_game()

tk.mainloop()
