import pygame
from almacen import Almacen
from Ventana import MainWindow


ancho_pantalla = 640
alto_pantalla = 480
ini =(50,440)
blanco = (255, 255, 255)

def main():

    pygame.init()
    p = MainWindow(ancho_pantalla,alto_pantalla,3,3,3,3,3)

    dirx = 200
    diry = 200

    MainWindow.ruta(p,dirx,diry)
    p.image= pygame.image.load("robot2caja.png").convert_alpha()
    MainWindow.recoger(p)
    MainWindow.home(p)
    p.image =  pygame.image.load("robot-preview.png").convert_alpha()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


        pygame.display.update()


if __name__ == "__main__":
    main()
