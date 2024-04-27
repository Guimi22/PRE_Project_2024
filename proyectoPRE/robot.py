import pygame
from pygame.locals import *
import sys
class robot(pygame.sprite.Sprite):
    def __init__(self, peso, tamaño, carga1, carga2, carga3, direccion):
        self.image = pygame.image.load("robot-preview.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = 500
        self.rect.centery = 400
        self.speed = [1, 1]
        self.TL = tamaño #limite del robot
        self.PL = peso
        self.car = (carga1,carga2,carga3) #objetos que lleva encima (sus numeros de serie)
    def mover (self,dir):
        match (dir):
            case 1:
                 self.rect.move_ip((self.speed[1], 0))
            case 2:
                self.rect.move_ip((-self.speed[1], 0))
            case 3:
                self.rect.move_ip((0, self.speed[1]))
            case 4:
                self.rect.move_ip((0, -self.speed[1]))

    def espera(self):
        self.rect.move_ip(0,0);
    def recoger(self, item):
        self.car = item.sn
    def dejar(self, item):
        self.car = 0;

