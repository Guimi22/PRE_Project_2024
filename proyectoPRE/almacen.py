import sys
import pygame
from pygame.locals import *

from items import *

import os

pygame.init()

class Almacen:
    def __init__(self, rows, columns, diccionario):
        self.rows = rows
        self.columns = columns
        self.items = diccionario

    def funct_read_excel(self, filename):
        with open(filename, mode='r') as f:
            lines_aux1 = []
            lines_aux2 = []
            list_excel = []
            for line in f:
                lines_aux1 = line.split(';')
                len_line = len(lines_aux1)
                lines_aux2 = lines_aux1[len_line - 1].split('\n')
                lines_aux2.remove('')
                lines_aux1.remove(lines_aux1[len_line - 1])
                lines_aux1.append(lines_aux2[0])
                list_excel.append(lines_aux1)
        return list_excel

    def arange_order(self, filename):
        order = self.funct_read_excel(filename)
        order_new = []
        for item in order:
            #item_in_almacen = self.find_item(item[0])
            posx_aux = self.items[item[0]][2]
            posy_aux = self.items[item[0]][3]
            long = len(order_new)
            if long == 0:
                order_new = [[posx_aux, posy_aux]]
            else:
                closer_item_x = order_new[0][0]
                closer_item_y = order_new[0][1]
                if posx_aux < closer_item_x:
                    order_new = [0, order_new]
                    order_new[0] = [posx_aux, posy_aux]
                else:
                    if posy_aux < closer_item_y:
                        #order_new[long + 1] = order_new[long]
                        #order_new[long] = item
                        order_new.append([posx_aux, posy_aux])
                    else:
                        order_new.append([posx_aux, posy_aux])
        return order_new

    def update_stock(self, filename):
        list_stock = self.funct_read_excel(filename)
        item_str = 'item'
        for item in list_stock:
            #item_in_almacen = self.find_item(item[0])
            #if item_in_almacen == 0:
            num = str(len(self.items))
            var_name_aux = item_str + num
            globals()[var_name_aux] = items(item[0], item[1], item[2], item[3], item[4], item[5])
            dicc_item = globals()[var_name_aux].diccionario_item()
            self.items = self.items | dicc_item
            #self.update_almacen(globals()[var_name_aux])
            # else:
            #     item_in_almacen.st = item_in_almacen.st + int(item[len(item) - 1])
        return list_stock

    def update_almacen(self,varname):
        self.items.append(varname)

    def find_item(self,serial_num):

        for item in self.items:
            if item.SN == serial_num:
                return item
            else:
                return 0
