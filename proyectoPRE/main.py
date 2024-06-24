import pygame
from almacen import Almacen
from Ventana import MainWindow


ancho_pantalla = 640
alto_pantalla = 480
ini =(50,440)
blanco = (255, 255, 255)
i = 0
def main():

    # pygame.init()
    # p = MainWindow(ancho_pantalla,alto_pantalla,3,3,3,3,3)
    diccionario = {}
    A = Almacen(3,4,diccionario)
    prova = A.update_stock('Libro1.csv')
    #prova1 = A.find_item('55572f')
    prova2 = A.items
    print(prova2)
    #print(prova2['5433fg'][2])
    prova3 = A.funct_read_excel('Libro2.csv')
    print(prova3)
    comanda, comanda_snqty = A.arange_order('Libro2.csv')
    print(comanda, comanda_snqty)
    # i = 0
    # for item in comanda:
    #     i += 1
    #     MainWindow.ruta(p, item[0], item[1])
    #     MainWindow.recoger(p, i)
    #     A.update_items(comanda_snqty[i-1][0], comanda_snqty[i-1][1])
    #     print(A.items)
    # i = 0
    # MainWindow.puerta(p)
    # MainWindow.dejar(p)
    # MainWindow.home(p)
    #
    #
    # for event in pygame.event.get():
    #     if event.type == pygame.QUIT:
    #         sys.exit()
    #
    #
    #     pygame.display.update()


if __name__ == "__main__":
    main()
