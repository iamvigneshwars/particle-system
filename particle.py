import pygame
import random
import sys

pygame.init()

size = (600, 600)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

class Particle:
    def __init__(self, x, y):
        self.x = max(0, min(x, size[0]))
        self.y = max(0, min(y, size[1]))
        self.xv = random.uniform(-2, 2)
        self.yv = random.uniform(-2, 2)
        self.color = (random.randint(0, 255), random.randint(0, 255),random.randint(0, 225))

    def move(self):
        self.x += self.xv
        self.y += self.yv

        # Check for boundary conditions
        if self.x <= 0 or self.x >= size[0]: self.xv -= self.xv
        if self.y <= 0 or self.y >= size[1]: self.yv-= self.yv

        # Velocity decay
        self.xv *= 0.9
        self.xv *= 0.9

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (max(0, int(self.x)), int(self.y)), 5)

# Store particles
Particles = []

while True:

    for event in pygame.event.get():
        # Press Escape key to quit
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()

        # Quit by closing the window
        if event.type == pygame.QUIT:
            sys.exit()

    # Clear previous screen
    screen.fill((0, 0, 0))

    if pygame.mouse.get_pressed()[0]:
        particle = Particle(*pygame.mouse.get_pos())
        Particles.append(particle)
    
    for particle in Particles:
        particle.move()
        particle.draw(screen)

    pygame.display.update()
    clock.tick(60)
