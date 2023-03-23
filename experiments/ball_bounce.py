import pygame
import random
import math

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Initialize Pygame
pygame.init()

# Set up the display window
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Bouncing Ball")

# Set up the clock for the game loop
clock = pygame.time.Clock()

# Define the Ball class
class Ball:
    def __init__(self, x, y, radius, color, mass, height):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass
        self.height = height
        self.vx = 0
        self.vy = 0
        self.time = 0
        self.bounces = 0

    def draw(self):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

    def update(self, dt):
        g = 9.81  # acceleration due to gravity
        self.time += dt
        if self.bounces == 0:
            self.vy = math.sqrt(2 * g * self.height)
        else:
            self.vy += g * dt
        self.x += self.vx * dt
        self.y += self.vy * dt + 0.5 * g * dt ** 2
        print(self.vy * dt + 0.5 * g * dt ** 2)

    def bounce(self, ground):
        if self.y + self.radius >= ground:
            self.vy *= -0.8
            self.y = ground - self.radius
            self.bounces += 1

# Set up the initial state of the simulation
ball = Ball(400, 100, 20, BLUE, 10, 100)
ground = 500

# Main game loop
done = False
max_bounces = 10
# while not done and ball.bounces < max_bounces:
while not done:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Update the ball
    dt = clock.tick(60) / 1000.0
    ball.update(dt)

    # Bounce the ball off the ground
    ball.bounce(ground)

    # Draw the ball and the ground
    screen.fill(WHITE)
    ball.draw()
    pygame.draw.rect(screen, BLACK, (0, ground, size[0], size[1]-ground))

    # Update the screen
    pygame.display.flip()

# Clean up
pygame.quit()
