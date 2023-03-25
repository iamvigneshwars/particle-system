import pygame
import math

# Initialize Pygame
pygame.init()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define window size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Create a window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the window title
pygame.display.set_caption("Bouncing Ball")
clock = pygame.time.Clock()

# Define ball properties
BALL_RADIUS = 20
BALL_COLOR = WHITE
BALL_START_X = SCREEN_WIDTH // 2
BALL_START_Y = BALL_RADIUS
# GRAVITY = 0.5
GRAVITY = 1
BOUNCE_LOSS = 0.8
MAX_BOUNCES = 5

class Ball:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.vel_x = 0
        self.vel_y = 0
        self.bounces = 0

    def update(self):
        # Apply gravity to the velocity
        self.vel_y += GRAVITY

        # Update the position based on the velocity
        self.x += self.vel_x
        self.y += self.vel_y

        # Check for collision with the ground
        if self.y + self.radius > SCREEN_HEIGHT:
            self.y = SCREEN_HEIGHT - self.radius
            self.vel_y = -self.vel_y * BOUNCE_LOSS
            self.bounces += 1

            # Reduce the velocity on each bounce
            self.vel_x *= BOUNCE_LOSS
            self.vel_y *= BOUNCE_LOSS

        # # Check for max bounces
        # if self.bounces >= MAX_BOUNCES:
        #     self.vel_x = 0
        #     self.vel_y = 0

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

# Create a ball object
ball = Ball(BALL_START_X, BALL_START_Y, BALL_RADIUS, BALL_COLOR)

# Run the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BLACK)

    # Update the ball
    ball.update()

    # Draw the ball
    ball.draw(screen)

    # Update the display
    pygame.display.update()
    clock.tick(60)

# Quit Pygame
pygame.quit()
