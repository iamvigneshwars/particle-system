import pygame
import random

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
    def __init__(self, x, y, radius, color, mass, gravity):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass
        self.gravity = gravity
        self.vx = 0
        self.vy = 0

    def draw(self):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

    def move(self):
        self.x += self.vx
        self.y += self.vy
        self.vy += self.gravity

    def bounce(self, ground):
        if self.y + self.radius >= ground:
            self.vy *= -0.8
            self.y = ground - self.radius

# Set up the initial state of the simulation
ball = Ball(400, 100, 20, BLUE, 10, 1)
ground = 500

# Main game loop
done = False
while not done:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Clear the screen
    screen.fill(WHITE)

    # Move the ball
    ball.move()

    # Bounce the ball off the ground
    ball.bounce(ground)

    # Draw the ball and the ground
    ball.draw()
    pygame.draw.rect(screen, BLACK, (0, ground, size[0], size[1] - ground))

    # Update the screen
    pygame.display.flip()

    # Wait for the next frame
    clock.tick(60)

# Clean up Pygame
pygame.quit()
