import pygame
from pygame.draw import *
from pygame import surface
from pygame import Color, transform
import math
from math import pi

pygame.init()
FPS = 30
screen = pygame.display.set_mode((795, 1025))

rect(screen, (102, 255, 255), (0, 0, 795, 620))
rect(screen, (255, 255, 255), (0, 620, 795, 405))
line(screen, (0, 0, 0), [0, 620], [795, 620])

#
def fish(x0, y0, a, l):
    k = 220 / l
    sfish = pygame.Surface((220, 115))
    polygon(sfish, (255, 153, 153), ((160, 60), (171, 58), (196, 73), (168, 88)), width=0)
    arc(sfish, (163, 194, 194), (65, 33, 148, 50), 0.4, 2.74, 30)
    arc(sfish, (163, 194, 194), (65, 13, 148, 50), 3.44, 6, 30)
    polygon(sfish, (163, 194, 194), ((67, 45),
            (14, 80), (4, 35)), width=0)  # хвост рыбы
    polygon(sfish, (255, 153, 153), ((135, 33), (94, 0), (164, 15),
            (172, 24), (171, 35)), width=0)  # верхний плавник
    polygon(sfish, (255, 153, 153), ((97, 59),
            (80, 79), (112, 84), (114, 62)), width=0)  # нижний плавник
    circle(sfish, (51, 102, 204), (170, 47), 7, width=0)  # глаз
    circle(sfish, (0, 0, 26), (170, 47), 5, width=0)

    sfish = transform.rotate(sfish, a)
    sfish = transform.rotozoom(sfish, 0, k)
    sfish.set_colorkey((0, 0, 0))
    screen.blit(sfish, (x0, y0))


def bear(x0, y0, a, l):
    k = 220 / l
    sbear = pygame.Surface((790, 690))
    ellipse(sbear, (255, 255, 255), (130, 110, 180, 100)) #голова
    ellipse(sbear, (0, 0, 1), (130, 110, 180, 100), 1)
    ellipse(sbear, (255, 255, 250), (10, 180, 260, 450))#тельце
    ellipse(sbear, (0, 0, 1), (10, 180, 260, 450), 1)
    lines(sbear, (0, 0, 1), 0, ((262, 378), (317, 276), (383, 203), (467, 130), (541, 81), (627, 20)), 5)#удочка
    line(sbear, (0, 0, 1), (640, 510), (627, 20), 3)
    ellipse(sbear, (255, 255, 250), (210, 270, 125, 60))#ручка
    ellipse(sbear, (0, 0, 1), (210, 270, 125, 60), 1)
    ellipse(sbear, (255, 255, 250), (140, 490, 190, 150))#ножка
    ellipse(sbear, (0, 0, 1), (140, 490, 190, 150), 1)
    ellipse(sbear, (255, 255, 250), (250, 610, 140, 50))
    ellipse(sbear, (0, 0, 1), (250, 610, 140, 50), 1)
    ellipse(sbear, (255, 255, 250), (145, 105, 35, 30))#морда
    ellipse(sbear, (0, 0, 1), (145, 105, 35, 30), 1)
    ellipse(sbear, (0, 0, 1), (205, 140, 15, 13))
    ellipse(sbear, (0, 0, 1), (300, 150, 15, 13))
    lines(sbear, (0, 0, 1), 0, ((210, 183), (266, 183), (295, 178), (305, 177)), 1)
    ellipse(sbear, (61, 92, 92), (440, 460, 315, 105))#лунка
    ellipse(sbear, (0, 0, 1), (440, 460, 315, 105), 1)
    ellipse(sbear, (133, 173, 173), (440, 460, 315, 105))
    ellipse(sbear, (0, 0, 1), (450, 480, 295, 85), 1)
    #масштаб
    sbear = transform.rotate(sbear, a)
    sbear = transform.rotozoom(sbear, 0, k)
    sbear.set_colorkey((0, 0, 0))
    screen.blit(sbear, (x0, y0))


fish(470, 920, 0, 220)
bear(10, 330, 0, 250)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()