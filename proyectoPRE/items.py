import pygame
from pygame.locals import *
import sys

class items():
    def __init__(self, serialnumber, peso, tamano, columna, fila, stock):
        self.columnas = {'A': 5, 'B': 10, 'C': 15}
        self.filas = {'1': 5, '2': 10, '3': 15, '4': 20}
        self.SN = serialnumber
        self.W = int(peso)
        self.S = int(tamano)
        self.posx = self.posicion_x(columna)
        self.posy = self.posicion_y(fila)
        self.st = int(stock)

    def espera(self):
        self.rect.move_ip(0,0);
    def recoger(self, item):
        self.car = item.sn
    def dejar(self, item):
        self.car = 0
    def posicion_x(self,columna):
        valor = self.columnas[columna]
        return valor
    def posicion_y(self,fila):
        valor = self.filas[fila]
        return valor
    def diccionario_item(self):
        vector_aux = [self.W, self.S, self.posx, self.posy, self.st]
        dicc = {self.SN:vector_aux}
        return dicc