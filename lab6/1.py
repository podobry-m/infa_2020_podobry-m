import pygame
import math
from pygame.draw import *
from random import randint
pygame.init()

N = 0
K=5
SCREEN_X=1800
SCREEN_Y=1000
FPS = 60
V = 600/FPS
DV = V/20
screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
font = pygame.font.Font(None, 50)
balls = []

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [BLUE, YELLOW, GREEN, MAGENTA, CYAN]
SUPER = False
def create_new_ball(pol):
    
    global SUPER
    if (SUPER==False):
        super_ball = randint(0, 7)
    else: super_ball = 1
    x = randint(100,1500)
    y = randint(100,700)
    angle = randint(0, 360)/180*math.pi
    vx = V*math.cos(angle)
    vy = V*math.sin(angle)
    if(pol):
        r = 30
        c = RED
        return [r, x, y, vx/2, vy/2, c, 6]
    if(super_ball > 0):
        r = randint(30,50)
        c = COLORS[randint(0, 4)]
        return [r, x, y, vx, vy, c, 0]
    else:
        SUPER = True
        r = 30
        c = (255, 255, 255)
        return [r, x, y, vx, vy, c, 2]
    
    

for i in range(K):
    balls.append(create_new_ball(False))
balls.append(create_new_ball(True))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            x=pos[0]
            y=pos[1]
            for i, ball in enumerate(balls):
                if(math.sqrt((x-ball[1])**2+(y-ball[2])**2) <= ball[0]):
                    N+=(1+ball[6])
                    balls[K][0]+=1
                    balls[K][3]+=DV
                    balls[K][4]+=DV
                    if(ball[6]>0):
                        SUPER=False
                    V +=DV
                    balls[i] = create_new_ball(False)
    text = font.render(str(N), 1, (255,255,255))
    screen.blit(text, (0,0))
    for ball in balls:
        circle(screen, ball[5], (int(ball[1]), int(ball[2])), ball[0], ball[6])
        if(ball[6]>0):
            (xm, ym) = pygame.mouse.get_pos()
            dx = (ball[1]-xm)
            dy = (ball[2]-ym)
            rm = (dx**2+dy**2)**0.5
            v = (ball[3]**2+ball[4]**2)**0.5
            if(ball[6] < 3):
                if((rm < 1.5 * ball[0]) & (rm > ball[0])):
                    ball[3] = (dx/rm*v)
                    ball[4] = (dy/rm*v)
            else:
                if(rm<ball[0]):
                    finished = True
                   
                ball[3] = -(dx/rm*v)
                ball[4] = -(dy/rm*v)
                
        
        if(ball[1]+ball[0]>=SCREEN_X or ball[1]-ball[0]<=0):
            ball[3] *= -1
        if(ball[2]+ball[0]>=SCREEN_Y or ball[2]-ball[0]<=0):
            ball[4] *= -1
        ball[1]+=ball[3]
        ball[2]+=ball[4]
    pygame.display.update()
    screen.fill(BLACK)
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()
