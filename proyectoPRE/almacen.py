import sys
import pygame
from pygame.locals import *

from items import *
import heapq
import math
import os

pygame.init()

class Almacen:
    def __init__(self, rows, columns, diccionario):
        self.rows = rows
        self.columns = columns
        self.items = diccionario

    #funct_read_excel(self, filename) --> Método de la clase almacen que se usa para la lectura de los ficheros .csv que
    #devuelven una lista de listas, con los valores de cada celda por fila.
    def funct_read_excel(self, filename):
        with open(filename, mode='r') as f:
            list_excel = []
            for line in f:
                lines_aux1 = line.split(';')
                len_line = len(lines_aux1)
                lines_aux2 = lines_aux1[len_line - 1].split('\n')
                if '' in lines_aux2:
                    lines_aux2.remove('')
                lines_aux1.remove(lines_aux1[len_line - 1])
                lines_aux1.append(lines_aux2[0])
                list_excel.append(lines_aux1)
        return list_excel

    # def arange_order(self, filename):
    #     order = self.funct_read_excel(filename)
    #     order_new = []
    #     order_new_snqty = []
    #
    #     for item in order:
    #         #item_in_almacen = self.find_item(item[0])
    #         posx_aux = self.items[item[0]][2]
    #         posy_aux = self.items[item[0]][3]
    #         sn_item = item[0]
    #         qty_item = item[1]
    #         lista_aux1 = [posx_aux, posy_aux]
    #         lista_aux2 = [sn_item, qty_item]
    #         long = len(order_new)
    #         if long == 0:
    #             order_new = [lista_aux1]
    #             order_new_snqty = [lista_aux2]
    #         else:
    #             i = 0
    #             for element in order_new:
    #                 i += 1
    #                 closer_item_x = element[0]
    #                 closer_item_y = element[1]
    #                 if posx_aux < closer_item_x:
    #                     order_new.insert(i-1, lista_aux1)
    #                     order_new_snqty.insert(i-1, lista_aux2)
    #                     break
    #                 elif posx_aux == closer_item_x:
    #                     if posy_aux < closer_item_y:
    #                         order_new.insert(i-1, lista_aux1)
    #                         order_new_snqty.insert(i-1, lista_aux2)
    #                         break
    #                     else:
    #                         order_new.insert(i, lista_aux1)
    #                         order_new_snqty.insert(i, lista_aux2)
    #                         break
    #                 else:
    #                     if i == long:
    #                         order_new.append(lista_aux1)
    #                         order_new_snqty.append(lista_aux2)
    #                         break
    #                     else:
    #                         break
    #     return order_new, order_new_snqty

    #distance(self, pos1, pos2) --> Método de la clase almcen que devuelve el módulo del vector que va de pos1 a pos2; es
    # decir, la distancia entre los dos puntos. Se utiliza en la función arange_order(self, filename) para definir el orden de
    #la comanda.
    def distance(self, pos1, pos2):
        return math.sqrt((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2)

    # def arange_order(self, filename):
    #     order = self.funct_read_excel(filename)
    #     item_positions = {item[0]: (self.items[item[0]][2], self.items[item[0]][3]) for item in order}
    #     item_weights = {item[0]: self.items[item[0]][1] for item in order}
    #
    #     # Assume the starting point is the origin (0,0)
    #     start_position = (0, 0)
    #     order_list = []
    #
    #     # Priority queue to store (cost, current_position, path_taken)
    #     pq = [(0, start_position, [])]
    #     visited = set()
    #
    #     while pq:
    #         current_cost, current_position, path = heapq.heappop(pq)
    #
    #         if current_position in visited:
    #             continue
    #         visited.add(current_position)
    #
    #         if current_position in item_positions.values():
    #             item = next(k for k, v in item_positions.items() if v == current_position)
    #             order_list.append((item, item_weights[item]))
    #             path.append(item)
    #             del item_positions[item]
    #             if not item_positions:
    #                 break
    #
    #         for next_item, next_position in item_positions.items():
    #             if next_position not in visited:
    #                 distance = self.distance(current_position, next_position)
    #                 weight = float(item_weights[next_item])
    #                 heapq.heappush(pq, (current_cost + distance + weight, next_position, path[:]))
    #     return order_list

    def arange_order(self, filename):
        order = self.funct_read_excel(filename)
        item_positions = {}
        for item in order:
            item_positions[item[0]] = [self.items[item[0]][2], self.items[item[0]][3]], self.items[item[0]][1], [item[0], item[1]]
        # item_weights = {item[0]: self.items[item[0]][1] for item in order}
        position = [50, 440]
        # funcion que devuelva posicion actual del robot en el almacen
        iter_finish = 1
        weighted_distances = []
        order_route = []
        order_snqty = []
        snqty_lista = []

        while iter_finish:
            for item in item_positions:
                weighted_distances.append(item_positions[item][1] * self.distance(position, item_positions[item][0]))
                snqty_lista.append(item_positions[item][2])
            next_node = min(weighted_distances)
            indice_lista = weighted_distances.index(next_node)
            order_route.append(item_positions[snqty_lista[indice_lista][0]][0])
            order_snqty.append(snqty_lista[indice_lista])
            position = order_route[len(order_route) - 1]
            del (item_positions[snqty_lista[indice_lista][0]])
            weighted_distances = []
            snqty_lista = []
            if len(item_positions) == 0:
                iter_finish = 0
        return order_route, order_snqty

    #update_stock(self, filename) --> Metodo que actualiza el stock de items en el almacen a partir de un fichero con
    #el número de serie, el peso, el tamaño, la posición en el almacén y la cantidad de items.
    def update_stock(self, filename):
        list_stock = self.funct_read_excel(filename)
        item_str = 'item'
        for item in list_stock:
            item_in_almacen = self.find_item(item[0])
            if item_in_almacen == 0:
                num = str(len(self.items))
                var_name_aux = item_str + num
                globals()[var_name_aux] = items(item[0], item[1], item[2], item[3], item[4], item[5], var_name_aux)
                dicc_item = globals()[var_name_aux].diccionario_item()
                self.items = self.items | dicc_item
            else:
                self.update_items(item_in_almacen, item[5], 1)
        return list_stock


    def find_item(self, serial_num):
        for item in self.items:
            if item == serial_num:
                return item
        return 0

    def update_items(self, serialnum, quantity, operation):
        new_dicc = globals()[self.items[serialnum][5]].update_stock_item(quantity, operation)
        self.items[serialnum] = new_dicc[serialnum]
