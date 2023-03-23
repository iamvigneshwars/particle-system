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

obs_cord = pygame.Rect(200, 200, 100, 100)
target = (400, 400)

class Particle:
    def __init__(self, x, y):
        self.x = max(0, min(x, size[0]))
        self.y = max(0, min(y, size[1]))
        self.vx = random.uniform(-2, 2)
        self.vy = random.uniform(-2, 2)
        self.surf = pygame.Surface((10, 10))
        self.surf.fill((0, 0, random.randint(100, 255)))
        self.ret = self.surf.get_rect(center=(self.x, self.y))
        self.life = 100


    # def move(self, dt):

    #     dx = target[0] - self.x
    #     dy = target[1] - self.y
    #     distance = math.sqrt(dx**2 + dy**2)

    #     if self.ret.colliderect(obs_cord):
    #         # Calculate the angle to the obstacle
    #         angle = math.atan2(self.y - obs_cord.centery, self.x - obs_cord.centerx)
    #         self.vx += math.cos(angle)  
    #         self.vy += math.sin(angle)  

    #     if distance <= 10:
    #         self.life = 0

    #     if distance > 0:
    #         # self.vx += dx / distance * 0.9
    #         # self.vy += dy / distance * 0.2
    #         self.vx += dx * 0.9
    #         self.vy += dy * 0.2

    #     if self.x < 0 or self.x > size[0] : self.vx *= -1
    #     if self.y < 0 or self.y > size[1] : self.vy *= -1

    #     self.x += self.vx 
    #     self.y += self.vy 

    #     self.vx *= 0.99
    #     self.vy *= 0.99

    def move(self, dt):
        dx = target[0] - self.x
        dy = target[1] - self.y
        distance = math.sqrt(dx**2 + dy**2)

        if self.ret.colliderect(obs_cord):
            # Calculate the normal vector of the obstacle
            normal = pygame.math.Vector2(self.x - obs_cord.centerx, self.y - obs_cord.centery).normalize()

            # Calculate the particle's velocity vector
            velocity = pygame.math.Vector2(self.vx, self.vy)

            # Calculate the dot product of velocity and normal vectors
            dot_product = velocity.dot(normal)

            if dot_product < 0:
                # Reverse the velocity vector in the direction of the normal vector
                velocity -= 2 * dot_product * normal
                self.vx, self.vy = velocity.x, velocity.y

        if distance <= 10:
            self.life = 0

        if distance > 0:
            self.vx += dx / distance * 0.9
            self.vy += dy / distance * 0.2

        if self.x < 0 or self.x > size[0] : self.vx *= -1
        if self.y < 0 or self.y > size[1] : self.vy *= -1

        self.x += self.vx 
        self.y += self.vy 

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
    dt = clock.tick(60) / 1000.0

    if pygame.mouse.get_pressed()[0]:
        if not obs_cord.collidepoint(pygame.mouse.get_pos()):
            particles.append(Particle(*pygame.mouse.get_pos()))

    pygame.draw.rect(screen, 'Red', obs_cord)

    particles = [particle for particle in particles if particle.life > 0]
    for particle in particles:
        particle.move(dt)
        particle.draw()


    pygame.display.update()


