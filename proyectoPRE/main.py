import sys
import pygame
from pygame.locals import *
from robot import robot
from items import *
import os



ancho_pantalla = 640
alto_pantalla = 480

blanco = (255, 255, 255)

def main():
    pygame.init()
    pantalla = pygame.display.set_mode((ancho_pantalla, alto_pantalla))
    pygame.display.set_caption("almacen alimentacion chino")
    pantalla.fill(blanco)
    robotico = robot(20,30,344,3,3 ,3)
    item1 = items(4, 20, 33434, 200, 300)
    item1 = items(4, 20, 33434, 160, 300)
    clock = pygame.time.Clock()
    pantalla.blit(item1.image, item1.pos)
    def actpantalla():
        pantalla.fill(blanco)
        pantalla.blit(robotico.image, robotico.rect)
        pygame.display.flip()

    dirx = 300
    diry =200



    while robotico.rect.right < dirx:
        clock.tick(60)
        robotico.mover(1)
        actpantalla()
    while robotico.rect.right > dirx:
        clock.tick(60)
        robotico.mover(2)
        actpantalla()
    while robotico.rect.bottom < diry:
        clock.tick(60)
        robotico.mover(3)
        actpantalla()
    while robotico.rect.bottom > diry:
        clock.tick(60)
        robotico.mover(4)
        actpantalla()


    pantalla.blit(robotico.image, robotico.rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        pygame.display.update()


if __name__ == "__main__":
    main()
