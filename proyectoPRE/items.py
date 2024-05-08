import pygame
from pygame.locals import *
import sys

class items():
    def __init__(self, peso, tamaño, serialnumber, columna, fila, stock):
        self.W = peso
        self.S = tamaño
        self.SN = serialnumber
        self.pos = (columna,fila)
        self.st = stock
    def espera(self):
        self.rect.move_ip(0,0);
    def recoger(self, item):
        self.car = item.sn
    def dejar(self, item):
        self.car = 0;

