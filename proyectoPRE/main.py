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


    dirx = 300
    diry =200

    while robotico.rect.right < dirx:
        clock.tick(60)
        robotico.updatehd()
        #robotico.rect.move_ip((0, robotico.speed[0]))
        pantalla.fill(blanco)
        pantalla.blit(robotico.image, robotico.rect)
        pygame.display.flip()
    while robotico.rect.right > dirx:
        clock.tick(60)
        robotico.updatehiz()
        #robotico.rect.move_ip((0, robotico.speed[0]))
        pantalla.fill(blanco)
        pantalla.blit(robotico.image, robotico.rect)
        pygame.display.flip()
    while robotico.rect.bottom < diry:
        clock.tick(60)
        robotico.updateva()
        #robotico.rect.move_ip((0, robotico.speed[0]))
        pantalla.fill(blanco)
        pantalla.blit(robotico.image, robotico.rect)
        pygame.display.flip()
    while robotico.rect.bottom > diry:
        clock.tick(60)
        robotico.updatevb()
        #robotico.rect.move_ip((0, robotico.speed[0]))
        pantalla.fill(blanco)
        pantalla.blit(robotico.image, robotico.rect)
        pygame.display.flip()

    pantalla.blit(robotico.image, robotico.rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        pygame.display.update()


if __name__ == "__main__":
    main()
