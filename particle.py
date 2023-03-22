import pygame
import random
import sys
import math

pygame.init()

size = (600, 600)
screen = pygame.display.set_mode(size)
font = pygame.font.Font(None, 20)
clock = pygame.time.Clock()
pygame.display.set_caption("Particle System")

class Particle:
    def __init__(self, x, y):
        self.x = max(0, min(x, size[0]))
        self.y = max(0, min(y, size[1]))
        self.xv = random.uniform(-2, 2)
        self.yv = random.uniform(-2, 2)
        self.color = (random.randint(0, 255), random.randint(0, 255),random.randint(0, 225))
        self.life = 120

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

        # Define buffer distance
        buffer_dist = 5

        # Check if particle is colliding with rectangle
        if rectangle.left - buffer_dist <= self.x <= rectangle.right + buffer_dist and rectangle.top - buffer_dist <= self.y <= rectangle.bottom + buffer_dist:
            angle = math.atan2(self.y - rectangle.centery, self.x - rectangle.centerx)
            # Move in the opposite direction
            self.xv += math.cos(angle) * 0.5
            self.yv += math.sin(angle) * 0.5

        # if rectangle.collidepoint((self.x, self.y)):
        #     angle = math.atan2(self.y - rectangle.centery, self.x - rectangle.centerx)
        #     # Move in the opposite direction
        #     self.xv += math.cos(angle) * 0.5
        #     self.yv += math.sin(angle) * 0.5

        # Velocity decay
        self.xv *= 0.99
        self.yv *= 0.99
        self.life -= 1

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
    
    rectangle = pygame.Rect(100, 100, 100, 100)
    pygame.draw.rect(screen, 'Red', rectangle)
    
    if pygame.mouse.get_pressed()[0]:
        particle = Particle(*pygame.mouse.get_pos())
        Particles.append(particle)

    Particles = [part for part in Particles if part.life > 0]
    
    for particle in Particles:
        particle.move()
        particle.draw()

    text_surf = font.render(f"Particles: {len(Particles)}", False, 'Green').convert()
    screen.blit(text_surf, (10, 10))

    pygame.display.update()
    clock.tick(60)
