import pygame
import random
import math
import sys

pygame.init()

SIZE = (600, 400)
FPS = 60

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
font = pygame.font.Font(None, 15)

target = (450, 230)

class Particle:
    def __init__(self, x, y):
        self.x = max(0, min(x, SIZE[0]))
        self.y = max(0, min(y, SIZE[1]))
        self.xv = random.uniform(-2, 2)
        self.yv = random.uniform(-2, 2)
        self.color = (random.randint(0, 255), random.randint(0, 255),random.randint(0, 225))
        self.life = 120

    def move(self):

        dx = target[0] - self.x
        dy = target[1] - self.y
        distance = math.sqrt(dx**2 + dy**2)

        if distance > 0:
            self.xv += dx / distance * 0.2
            self.yv += dy / distance * 0.2

        self.x += self.xv
        self.y += self.yv 

        if self.x < 0 or self.x > SIZE[0] : self.xv *= -1
        if self.y < 0 or self.y > SIZE[1] : self.yv *= -1

        self.xv *= 0.999
        self.yv *= 0.999
        # self.life -= 1

        if distance < 50: 
            self.life = 0

    def draw(self):
        pygame.draw.circle(screen, self.color, (max(0, int(self.x)), int(self.y)), 5)


particles = []

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            sys.exit()


    particles = [part for part in particles if part.life > 0]

    x_pos = random.randint(0, 600)
    y_pos = random.randint(0, 400)
    particles.append(Particle(x_pos, y_pos))
        
    screen.fill('Black')

    for part in particles:
        part.move()
        part.draw()

    target_surf = pygame.draw.circle(screen, 'Red', target, 50)

    part_count = font.render(f"Count: {len(particles)}", False, 'White')
    screen.blit(part_count, (20, 20))

    clock.tick(60)
    pygame.display.update()