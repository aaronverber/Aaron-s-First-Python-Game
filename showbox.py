import pygame
from pygame.locals import *
from boxes import Box

pygame.init()
screen = pygame.display.set_mode([150, 150])
b = Box([255, 0, 0], [0, 0])
screen.blit(b.image, b.rect)
pygame.display.update()
while pygame.event.poll().type != KEYDOWN: pygame.time.delay(10)