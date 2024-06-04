import pygame
from almacen import Almacen
from Ventana import MainWindow


ancho_pantalla = 640
alto_pantalla = 480
ini =(50,440)
blanco = (255, 255, 255)
i = 0
def main():

    pygame.init()
    p = MainWindow(ancho_pantalla,alto_pantalla,3,3,3,3,3)
    diccionario = {}
    A = Almacen(3,4,diccionario)
    prova = A.update_stock('Libro1.csv')
    #prova1 = A.find_item('55572f')
    prova2 = A.items
    print(prova2)
    print(prova2['5433fg'][2])
    comanda = A.arange_order('Libro1.csv')
    print(comanda)
    i = 0
    for item in comanda:
        i += 1
        MainWindow.ruta(p, item[0], item[1])
        MainWindow.recoger(p,i)
        print(i)
    i = 0
    MainWindow.puerta(p)
    MainWindow.dejar(p)
    MainWindow.home(p)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


        pygame.display.update()


if __name__ == "__main__":
    main()
