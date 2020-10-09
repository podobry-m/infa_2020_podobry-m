import pygame
import math
from pygame.draw import *
from random import randint
pygame.init()

N = 0
SCREEN_X=1200
SCREEN_Y=900
FPS = 60
V = int(800/FPS)
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
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

def create_new_ball():
    super_ball = randint(0, 7)
    x = randint(100,1000)
    y = randint(100,700)
    vx = randint(-V,V)
    vy = randint(-V,V)
    if(super_ball > 0):
        r = randint(30,50)
        c = COLORS[randint(0, 5)]
        return [r, x, y, vx, vy, c, 0]
    else:
        r = 15
        c = (255, 255, 255)
        return [r, x, y, vx, vy, c, 2]
    
    

for i in range(5):
    balls.append(create_new_ball())

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
                    V += 1
                    balls[i] = create_new_ball()
    text = font.render(str(N), 1, (255,255,255))
    screen.blit(text, (0,0))
    for ball in balls:
        circle(screen, ball[5], (ball[1], ball[2]), ball[0], ball[6])
        if(ball[1]+ball[0]>=SCREEN_X or ball[1]-ball[0]<=0):
            ball[3]*=-1
        if(ball[2]+ball[0]>=SCREEN_Y or ball[2]-ball[0]<=0):
            ball[4]*=-1
        ball[1]+=ball[3]
        ball[2]+=ball[4]
    pygame.display.update()
    screen.fill(BLACK)
    
pygame.quit()
