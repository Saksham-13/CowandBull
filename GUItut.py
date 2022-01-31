import os
from numpy import number
import pygame
# setup display
WIDTH,HEIGHT= 800,500
pygame.init()
WIN=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Cow and Bull")
icon = pygame.image.load("cow.png")
pygame.display.set_icon(icon)
# Load images
grass = pygame.image.load("graassland.png")
numbers = pygame.image.load("numbers1.png")
pygame.transform.smoothscale(grass,(WIDTH,HEIGHT))
# Setup GameLoop
clock = pygame.time.Clock()
run = True
FPS=60
while run:
    clock.tick(FPS)
    WIN.blit(grass,(0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                print(pos)
    pygame.display.update()


pygame.quit()
 