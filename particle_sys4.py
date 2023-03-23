import pygame
import math
import random
import sys

pygame.init()

size = (800, 600)
fps = 60

screen = pygame.display.set_mode(size)
clock  = pygame.time.Clock()

platform_surf = pygame.Surface((600, 100))
platform_surf.fill('Red')
platform_rect = platform_surf.get_rect(midbottom = (400, 400))

obs_cord = pygame.Rect(200, 200, 100, 100)
targets = [(400, 400), (200, 200)]
targets = [
    {'pos': (400, 400)},
    {'pos': (200, 200)}
]
radius = 10

font = pygame.font.Font(None, 15)

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

    # def colloid(self):
    #     if self.ret.colliderect(obs_cord):
    #         # Calculate the angle to the obstacle
    #         angle = math.atan2(self.y - obs_cord.centery, self.x - obs_cord.centerx)
    #         self.vx += math.cos(angle)  
    #         self.vy += math.sin(angle)  

    # if self.ret.colliderect(obs_cord):
    #     # Calculate the normal vector of the obstacle
    #     normal = pygame.math.Vector2(self.x - obs_cord.centerx, self.y - obs_cord.centery).normalize()

    #     # Calculate the particle's velocity vector
    #     velocity = pygame.math.Vector2(self.vx, self.vy)

    #     # Calculate the dot product of velocity and normal vectors
    #     dot_product = velocity.dot(normal)

    #     if dot_product < 0:
    #         # Reverse the velocity vector in the direction of the normal vector
    #         velocity -= 2 * dot_product * normal
    #         self.vx, self.vy = velocity.x, velocity.y

    def move(self):

        distance = sys.maxsize
        dx = 0
        dy = 0

        for target in targets:
            dist_x = target['pos'][0]- self.x
            dist_y = target['pos'][1] - self.y
            d = math.sqrt(dist_x ** 2 + dist_y **2)
            if d < distance:
                distance = d
                dx = dist_x
                dy = dist_y

        if distance <= 10:
            self.life = 0

        if distance > 0:
            self.vx += dx / distance * 0.1
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
drag =False
while True:
    for event in pygame.event.get():
        # Check for exit conditions
        if (event.type == pygame.QUIT):
            sys.exit()
        if (event.type == pygame.KEYDOWN):
            if event.key == pygame.K_ESCAPE:
                sys.exit()


        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for target in targets:
                if (mouse_x - target['pos'][0])**2 + (mouse_y - target['pos'][1]) ** 2 <= radius **2:
                    offset_x = target['pos'][0] - mouse_x
                    offset_y = target['pos'][1] - mouse_y
                    target['selected'] = True
                    target['offset'] = (offset_x, offset_y)

        elif event.type == pygame.MOUSEBUTTONUP:
            # Deselect all circles
            for target in targets:
                target['selected'] = False

        elif event.type == pygame.MOUSEMOTION:
                mouse_x, mouse_y = pygame.mouse.get_pos()

                for target in targets:
                    if target.get('selected', False):
                        print(target)
                        target['pos']  = (mouse_x + target['offset'][0], mouse_y + target['offset'][1])


    screen.fill('Grey')
    dt = clock.tick(60) / 1000.0

    particles.append(Particle(10, 10))
    particles.append(Particle(10, size[1] - 10))
    particles.append(Particle(size[0] - 10, size[1]- 10))
    particles.append(Particle(size[0] - 10, 10))

    # Draw targets
    for target in targets:
        pygame.draw.circle(screen, 'Black', target['pos'], radius)

    # print(targets[0], targets[1])
    particles = [particle for particle in particles if particle.life > 0]
    for particle in particles:
        particle.move()
        particle.draw()

    particle_count = font.render(f"Count: {len(particles)}", False,'Black')
    screen.blit(particle_count, (380, 20))


    pygame.display.update()


