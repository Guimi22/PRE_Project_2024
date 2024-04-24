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
                if self.rect.left < 0 or self.rect.right > 640:
                    self.speed[0] = -self.speed[0]
                if self.rect.top < 0 or self.rect.bottom > 480:
                    self.speed[1] = -self.speed[1]
                self.rect.move_ip((self.speed[1], 0))
            case 2:
                if self.rect.left < 0 or self.rect.right > 640:
                    self.speed[0] = -self.speed[0]
                if self.rect.top < 0 or self.rect.bottom > 480:
                    self.speed[1] = -self.speed[1]
                self.rect.move_ip((-self.speed[1], 0))
            case 3:
                if self.rect.left < 0 or self.rect.right > 640:
                    self.speed[0] = -self.speed[0]
                if self.rect.top < 0 or self.rect.bottom > 480:
                    self.speed[1] = -self.speed[1]
                self.rect.move_ip((0, self.speed[1]))
            case 4:
                if self.rect.left < 0 or self.rect.right > 640:
                    self.speed[0] = -self.speed[0]
                if self.rect.top < 0 or self.rect.bottom > 480:
                    self.speed[1] = -self.speed[1]
                self.rect.move_ip((0, -self.speed[1]))
    def ruta(self):
        if self.rect(1) > 240:
            diry = 450
            while robotico.rect.bottom > diry:
                clock.tick(60)
                self.mover(4)
                pantalla.fill(blanco)
                pantalla.blit(robotico.image, robotico.rect)
                pygame.display.flip()
        elif self.rect(1) < 240:
            diry = 30
            while robotico.rect.bottom > diry:
                clock.tick(60)
                self.mover(4)
                pantalla.fill(blanco)
                pantalla.blit(robotico.image, robotico.rect)
                pygame.display.flip()






        pass

    def espera(self):
        self.rect.move_ip(0,0);
    def recoger(self, item):
        self.car = item.sn
    def dejar(self, item):
        self.car = 0;

