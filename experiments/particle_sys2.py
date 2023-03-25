import pygame
import random
import math
import sys

pygame.init()

SIZE = (800, 600)
FPS = 60

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
font = pygame.font.Font(None, 15)

# target = (450, 230)
target = (400, 300)

class Particle:
    def __init__(self, x, y):
        self.x = max(0, min(x, SIZE[0]))
        self.y = max(0, min(y, SIZE[1]))
        self.xv = random.uniform(-2, 2)
        self.yv = random.uniform(-2, 2)
        # self.color = (random.randint(0, 255), random.randint(0, 255),random.randint(0, 225))
        self.color = (0, 0,random.randint(100, 255))
        self.life = 120

    def collision(self):
        if rectangle.colliderect(pygame.Rect(self.x-5, self.y-5, 10, 10)):
            angle = math.atan2(self.y - rectangle.centery, self.x - rectangle.centerx)
            # self.xv += math.cos(angle) * 0.9
            # self.yv += math.sin(angle) * 0.9
            self.xv += math.cos(angle) 
            self.yv += math.sin(angle) 

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

        self.collision()

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

    screen.fill('Grey')

    rectangle = pygame.Rect(100, 100, 100, 100)
    pygame.draw.rect(screen, 'Red', rectangle)

    particles = [part for part in particles if part.life > 0]

    # for _ in range(10):
    #     x_pos = random.randint(0, 800)
    #     y_pos = random.randint(0, 600)
    #     particles.append(Particle(x_pos, y_pos))

    if pygame.mouse.get_pressed()[0]:
        if not rectangle.collidepoint(pygame.mouse.get_pos()):
            particles.append(Particle(*pygame.mouse.get_pos()))

    for part in particles:
        part.move()
        part.draw()

    target_surf = pygame.draw.circle(screen, 'Black', target, 10)

    part_count = font.render(f"Count: {len(particles)}", False, 'White')
    screen.blit(part_count, (20, 20))

    clock.tick(60)
    pygame.display.update()