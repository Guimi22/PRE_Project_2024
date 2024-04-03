import sys
import pygame
from pygame.locals import *
from robot import robot
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
    clock = pygame.time.Clock()


    while True:
        clock.tick(60)
        robotico.update()
        #robotico.rect.move_ip((0, robotico.speed[0]))
        pantalla.fill(blanco)
        pantalla.blit(robotico.image, robotico.rect)

        pygame.display.flip()



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.update()


if __name__ == "__main__":
    main()
