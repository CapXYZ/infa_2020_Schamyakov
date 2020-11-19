import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

'''
x1 = 100; y1 = 100
x2 = 300; y2 = 200
N = 15
color = (255, 0, 255)
rect(screen, color, (x1, y1, x2 - x1, y2 - y1), 2)
h = (x2 - x1) // (N + 1)
x = x1 + h
for i in range(N):
    line(screen, color, (x, y1), (x, y2))
    x += h
'''
rect(screen, (225, 225, 225), (0, 0, 400, 400)) #фон
circle(screen, (255, 255, 0), (200, 200), 150) #голова
circle(screen, (0, 0, 0), (200, 200), 150, 2) #обводка головы

circle(screen, (255, 0, 0), (130, 150), 40) #левый глаз
circle(screen, (0, 0, 0), (130, 150), 40, 2) #обводка
circle(screen, (0, 0, 0), (130, 150), 15) #зрачек

circle(screen, (255, 0, 0), (270, 150), 30) #правый глаз
circle(screen, (0, 0, 0), (270, 150), 30, 2) #обводка
circle(screen, (0, 0, 0), (270, 150), 10) #зрачек

line(screen, 0, (50, 60), (180, 120), 20) #левая бровь
line(screen, 0, (230, 125), (330, 85), 20) #правая бровь

line(screen, 0, (140, 280), (260, 280), 30) #рот

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()