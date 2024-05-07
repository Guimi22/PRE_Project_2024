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
    item1 = items(4, 20, 33434, 200, 300)
    item1 = items(4, 20, 33434, 160, 300)

    pantalla = pygame.display.set_mode((ancho_pantalla, alto_pantalla))
    clock = pygame.time.Clock()
    pantalla.blit(item1.image, item1.pos)
    pygame.display.set_caption("almacen")
    pantalla.fill(blanco)
    robotico = robot(20, 30, 344, 3, 3, 3)

    dirx = 560
    diry = 50
    def actpantalla():
        pantalla.fill(blanco)
        pantalla.blit(robotico.image, robotico.rect)
        pygame.display.flip()
        clock.tick(60)

    def ruta(x, y):
        pasa = 40
        pasb = 440
        print(robotico.rect.top - pasa, robotico.rect.top - pasb)
        if (robotico.rect.top - pasa) > abs(robotico.rect.top - pasb):
            pas = pasb
        else:
            pas = pasa

        if robotico.rect.bottom < pas:
            while robotico.rect.bottom < pas:
                robotico.mover(3)
                actpantalla()
        else:
            while robotico.rect.bottom > pas:
                robotico.mover(4)
                actpantalla()
        if robotico.rect.right < x:
            while robotico.rect.right < x:
                robotico.mover(1)
                actpantalla()
        else:
            while robotico.rect.right > x:
                robotico.mover(2)
                actpantalla()
        if robotico.rect.bottom < y:
            while robotico.rect.bottom < y:
                robotico.mover(3)
                actpantalla()
        else:
            while robotico.rect.bottom > y:
                robotico.mover(4)
                actpantalla()


    ruta(dirx, diry)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        pygame.display.update()


if __name__ == "__main__":
    main()
