import pygame
from pygame.draw import *

pygame.init()

FPS = 30
s = pygame.display.set_mode((1000, 800))
s.fill((255,255,255))
circle(s, (255,255,200), (500, 400), 200)
font = pygame.font.Font('freesansbold.ttf', 10)
textsurf=font.render('PYTHON is AMAZING', True, (0,0,0), (0,255,0))
textRect=textsurf.get_rect()
textRect.center=(500,30)
s.blit(textsurf, textRect)
rect(s, (0,255,0), (0, 0, 1000, 80))
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
