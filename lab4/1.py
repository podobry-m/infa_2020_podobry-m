import pygame
from pygame.draw import *

pygame.init()

FPS = 30
s = pygame.display.set_mode((400, 400))
s.fill((255,255,255))
circle(s, (255,255,0), (200, 200), 100)
circle(s, (255,0,0), (150, 180), 20)
circle(s, (0,0,0), (150, 180), 10)
circle(s, (255,0,0), (250, 180), 20)
circle(s, (0,0,0), (250, 180), 10)
rect(s, (100,0,0), (150, 250, 100, 20))
line(s, (0,0,0), (100,120),(180,170), 10)
line(s, (0,0,0), (220,170),(300,140), 10)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
