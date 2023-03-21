import pygame
import random
import sys

pygame.init()

size = (800, 800)
screen = pygame.display.set_mode(size)
font = pygame.font.Font(None, 20)
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
        # if self.x <= 0 or self.x >= size[0]: self.xv -= self.xv
        # if self.y <= 0 or self.y >= size[1]: self.yv-= self.yv

        if self.x <= 0 or self.x >= size[0]:
            self.xv = -self.xv
        if self.y <= 0 or self.y >= size[1]:
            self.yv = -self.yv

        # Velocity decay
        self.xv *= 0.99
        self.yv *= 0.99

    def draw(self):
        pygame.draw.circle(screen, self.color, (max(0, int(self.x)), max(0,int(self.y))), 5)

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

        # if event.type == pygame.MOUSEMOTION:
        #     particle = Particle(*pygame.mouse.get_pos())
        #     Particles.append(particle)


    # Clear previous screen
    screen.fill((0, 0, 0))

    if pygame.mouse.get_pressed()[0]:
        particle = Particle(*pygame.mouse.get_pos())
        Particles.append(particle)
    
    for particle in Particles:
        particle.move()
        particle.draw()

    text_surf = font.render(f"Particles: {len(Particles)}", False, 'Green').convert()
    screen.blit(text_surf, (10, 10))

    pygame.display.update()
    clock.tick(60)
