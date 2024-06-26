import pygame
from almacen import Almacen
from Ventana import MainWindow


ancho_pantalla = 640
alto_pantalla = 480
ini = (50, 440)
blanco = (255, 255, 255)
i = 0

def main():
    diccionario = {}
    pygame.init()
    # Creacion de objetos
    p = MainWindow(ancho_pantalla,alto_pantalla,2,3,3,3,3)
    A = Almacen(3,4,diccionario)
    # Lectura y orden de la comanda
    prova = A.update_stock('Libro1.csv')
    comanda, comanda_snqty = A.arange_order('Libro2.csv')
    print(comanda, comanda_snqty)

    i = 0
    n = 0
    # Recogida de los items de la comanda
    for item in comanda:
        i += 1
        n += 1
        MainWindow.ruta(p, item[0], item[1])
        MainWindow.recoger(p, n)
        A.update_items(comanda_snqty[i-1][0], comanda_snqty[i-1][1], 0)
        print(A.items)
        # Se llevan los items de 3 en 3 a la puerta
        if i%3 == 0:
            MainWindow.puerta(p)
            MainWindow.dejar(p)
            n = 0
    # El robot deja la ultima carga y vuelve al reposo
    MainWindow.puerta(p)
    MainWindow.dejar(p)
    MainWindow.home(p)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        pygame.display.update()


if __name__ == "__main__":
    main()
