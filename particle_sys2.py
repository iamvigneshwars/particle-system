import pygame
import random
import sys

pygame.init()

SIZE = (600, 400)
FPS = 60

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

class Particle:
    def __init__(self, x, y):
        self.x = max(0, min(x, SIZE[0]))
        self.y = max(0, min(y, SIZE[1]))
        self.xv = random.uniform(-2, 2)
        self.yv = random.uniform(-2, 2)
        self.color = (random.randint(0, 255), random.randint(0, 255),random.randint(0, 225))

    def move(self):
        self.x += self.xv
        self.y += self.yv 

        if self.x < 0 or self.x > SIZE[0] : self.xv *= -1
        if self.y < 0 or self.y > SIZE[1] : self.yv *= -1

        self.xv *= 0.999
        self.yv *= 0.999

    def draw(self):
        pygame.draw.circle(screen, self.color, (max(0, int(self.x)), int(self.y)), 5)


particles = []

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            sys.exit()


    # if pygame.mouse.get_pressed()[0]:
    #     particles.append(Particle(*pygame.mouse.get_pos()))
    x_pos = random.randint(0, 600)
    y_pos = random.randint(0, 400)
    particles.append(Particle(x_pos, y_pos))
        
    screen.fill('Black')

    for part in particles:
        part.move()
        part.draw()

    clock.tick(60)
    pygame.display.update()