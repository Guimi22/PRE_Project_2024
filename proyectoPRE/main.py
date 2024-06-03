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
    diccionario = {}
    A = Almacen(3,4,diccionario)
    prova = A.update_stock('Libro1.csv')
    #prova1 = A.find_item('55572f')
    prova2 = A.items
    print(prova2)
    #comanda = A.arange_order('Libro2.csv')

    # for item in comanda:
    #     MainWindow.ruta(p, item[0], item[1])
    #     p.image = pygame.image.load("robot2caja.png").convert_alpha()
    #     MainWindow.recoger(p)
    #     MainWindow.home(p)
    #     p.image = pygame.image.load("robot-preview.png").convert_alpha()
    #
    # dirx = 200
    # diry = 200
    #
    # MainWindow.ruta(p,dirx,diry)
    # p.image= pygame.image.load("robot2caja.png").convert_alpha()
    # MainWindow.recoger(p)
    # MainWindow.home(p)
    # p.image =  pygame.image.load("robot-preview.png").convert_alpha()
    #
    # for event in pygame.event.get():
    #     if event.type == pygame.QUIT:
    #         sys.exit()
    #
    #
    #     pygame.display.update()


if __name__ == "__main__":
    main()
