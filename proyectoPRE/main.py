import pygame
from almacen import Almacen
from Ventana import MainWindow


ancho_pantalla = 640
alto_pantalla = 480
ini = (50, 440)
blanco = (255, 255, 255)
i = 0
def main():

    pygame.init()
    p = MainWindow(ancho_pantalla,alto_pantalla,3,3,3,3,3)
    diccionario = {}
    A = Almacen(3,4,diccionario)
    prova = A.update_stock('Libro1.csv')
    valor = A.find_item('553f')
    print(valor)
    # #prova1 = A.find_item('55572f')
    # prova2 = A.items
    # print(prova2)
    # #print(prova2['5433fg'][2])
    # prova3 = A.funct_read_excel('Libro2.csv')
    # print(prova3)
    comanda,comanda_snqty = A.arange_order('Libro2.csv')
    print(comanda, comanda_snqty)

    # order = A.funct_read_excel('Libro2.csv')
    # item_positions = {}
    # for item in order:
    #     item_positions[item[0]] = [A.items[item[0]][2], A.items[item[0]][3]], A.items[item[0]][1], [item[0], item[1]]
    # # item_weights = {item[0]: self.items[item[0]][1] for item in order}
    # position = [50, 440]
    # # funcion que devuelva posicion actual del robot en el almacen
    # iter_finish = 1
    # weighted_distances = []
    # order_route = []
    # order_snqty = []
    # snqty_lista = []
    #
    # for item in item_positions:
    #     weighted_distances.append(item_positions[item][1] * A.distance(position, item_positions[item][0]))
    #     snqty_lista.append(item_positions[item][2])
    # next_node = min(weighted_distances)
    # indice_lista = weighted_distances.index(next_node)
    # order_route.append(item_positions[snqty_lista[indice_lista][0]][0])
    # print(order_route, item_positions, snqty_lista, indice_lista)
    i = 0
    for item in comanda:
        i += 1
        MainWindow.ruta(p, item[0], item[1])
        MainWindow.recoger(p, i)
        A.update_items(comanda_snqty[i-1][0], comanda_snqty[i-1][1], 0)
        print(A.items)
    MainWindow.puerta(p)
    MainWindow.dejar(p)
    MainWindow.home(p)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        pygame.display.update()


if __name__ == "__main__":
    main()
