import pygame
import math
import random
import sys

pygame.init()

size = (600, 600)
fps = 60

screen = pygame.display.set_mode(size)
clock  = pygame.time.Clock()

platform_surf = pygame.Surface((600, 100))
platform_surf.fill('Red')
platform_rect = platform_surf.get_rect(midbottom = (400, 400))

class Particle:
    def __init__(self, x, y):
        self.x = max(0, min(x, size[0]))
        self.y = max(0, min(y, size[1]))
        self.vx = random.uniform(-2, 2)
        self.vy = random.uniform(-2, 2)
        self.surf = pygame.Surface((10, 10))
        self.surf.fill((0, 0, random.randint(0, 255)))
        self.ret = self.surf.get_rect(center=(self.x, self.y))

    def move(self):
        self.x += self.vx
        self.y += self.vy

        if self.x < 0 or self.x > size[0] : self.vx *= -1
        if self.y < 0 or self.y > size[1] : self.vy *= -1

        self.vx *= 0.99
        self.vy *= 0.99


    def draw(self):
        self.ret.center = (self.x, self.y)
        screen.blit(self.surf, self.ret)


particles = []

while True:
    for event in pygame.event.get():
        # Check for exit conditions
        if (event.type == pygame.QUIT):
            sys.exit()
        if (event.type == pygame.KEYDOWN):
            if event.key == pygame.K_ESCAPE:
                sys.exit()

    screen.fill('Grey')

    if pygame.mouse.get_pressed()[0]:
        particles.append(Particle(*pygame.mouse.get_pos()))

    for particle in particles:
        particle.move()
        particle.draw()


    pygame.display.update()
    clock.tick(fps)


