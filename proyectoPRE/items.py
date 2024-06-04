import pygame
from pygame.locals import *
import sys

class items():
    def __init__(self, serialnumber, peso, tamano, columna, fila, stock):
        self.columnas = {'A': 75, 'B': 200, 'C': 320, 'D':460, 'E':560}
        self.filas = {'1': 400, '2': 320, '3': 240, '4': 160, '5':80}
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