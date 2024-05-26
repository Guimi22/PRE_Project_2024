import sys
import pygame
from pygame.locals import *

from items import *
from Ventana import *
import os

pygame.init()

class Almacen:
    def __init__(self, width, height):
        self.width=width
        self.height=height
        self.display = pygame.display.set_mode((self.width,self.height))
        pygame.display.set_caption("Caption")


    def actpantalla(self):
        self.display.fill(blanco)
        self.display.blit(robotico.image, robotico.rect)
        pygame.display.flip()
        clock.tick(60)

    def funct_read_order(self, filename):
        with open(filename, mode='r') as f:
            lines_aux1 = []
            lines_aux2 = []
            lines_aux3 = []
            list_order = []
            for line in f:
                lines_aux1 = line.split(';')
                lines_aux2 = lines_aux1[1].split('\n')
                lines_aux2.remove('')
                lines_aux3 = [lines_aux1[0], lines_aux2[0]]
                list_order.append(lines_aux3)
        return list_order

    def arange_order(self, order):

        order_new = []
        for item in order:
            pos_aux = item[0].pos
            long = len(order_new)
            if pos_aux[0] < order_new[long]:
                order_new[long + 1] = order_new[long]
                order_new[long] = item
            else:
                if pos_aux[1] < order_new[long]:
                    order_new[long + 1] = order_new[long]
                    order_new[long] = item
                else:
                    order_new.append(item)
        return order_new

    def update_stock(filename):
        with open(filename, mode='r') as f:
            lines_aux1 = []
            lines_aux2 = []
            list_stock = []
            for line in f:
                lines_aux1 = line.split(';')
                len_line = len(lines_aux1)
                lines_aux2 = lines_aux1[len_line - 1].split('\n')
                lines_aux2.remove('')
                lines_aux1.remove(lines_aux1[len_line - 1])
                lines_aux1.append(lines_aux2)
                list_stock.append(lines_aux1)
        return list_stock




