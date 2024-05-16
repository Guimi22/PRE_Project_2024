import sys
import pygame
from pygame.locals import *

from almacen import *
from Ventana import MainWindow

ancho_pantalla = 640
alto_pantalla = 480
blanco = (255, 255, 255)

def main():

    pygame.init()
    item1 = items(4, 20, 33434, 200, 300,3)
    item1 = items(4, 20, 33434, 160, 300,3)

    p = MainWindow(ancho_pantalla,alto_pantalla,3,3,3,3,3)
    dirx = 560
    diry = 50

    MainWindow.ruta(p,dirx,diry)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        pygame.display.update()


if __name__ == "__main__":
    main()
