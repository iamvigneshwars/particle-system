import pygame
import math
import random

pygame.init()

size = (600, 600)
fps = 60
active = True

screen = pygame.display.set_mode(size)
clock  = pygame.time.Clock()

while active:

    for event in pygame.event.get():

        # Check for exit conditions
        if (event.type == pygame.QUIT):
            active = False
        if (event.type == pygame.KEYDOWN):
            if event.key == pygame.K_ESCAPE:
                active = False

    screen.fill("Grey")
    pygame.display.update()
    clock.tick(fps)

pygame.quit()

