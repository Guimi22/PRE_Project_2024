import sys
import pygame
from pygame.locals import *
from robot import robot
from items import *
from robot import *
import os

pygame.init()

class MainWindow:
    def __init__(self, width, height):
        self.width=width
        self.height=height
        self.display = pygame.display.set_mode((self.width,self.height))
        pygame.display.set_caption("Caption")


    def background(self):
        img = pygame.image.load("caja.png")
        self.display.blit(img, (0,0))
    def actpantalla(self):
        self.display.fill(blanco)
        self.display.blit(robotico.image, robotico.rect)
        pygame.display.flip()
        clock.tick(60)

