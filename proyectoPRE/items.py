import pygame
from pygame.locals import *
import sys

class items():
    def __init__(self, serialnumber, peso, tamano, columna, fila, stock):
        self.SN = serialnumber
        self.W = int(peso)
        self.S = int(tamano)
        self.posx = int(columna)
        self.posy = int(fila)
        self.st = int(stock)
    def espera(self):
        self.rect.move_ip(0,0);
    def recoger(self, item):
        self.car = item.sn
    def dejar(self, item):
        self.car = 0;
