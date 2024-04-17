import pygame
from pygame.locals import *
import sys

class items(pygame.sprite.Sprite):
    def __init__(self, peso, tamaño, serialnumber, columna, fila):
        self.image = pygame.image.load("caja.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = columna
        self.rect.centery = fila
        self.SZ = tamaño
        self.PS = peso
        self.SN = serialnumber
        self.pos = [columna, fila]
        self.cajas = pygame.sprite.Group()
    def espera(self):
        self.rect.move_ip(0,0);
    def recoger(self, item):
        self.car = item.sn
    def dejar(self, item):
        self.car = 0;

