import pygame

# Initialize Pygame
pygame.init()

# Set up the display
width = 640
height = 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Click and Move Circle")

# Set up the circle
radius = 20
x = width // 2
y = height // 2
color = (255, 255, 255)

# Set up the game loop
running = True
dragging = False
while running:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the click was inside the circle
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if (mouse_x - x) ** 2 + (mouse_y - y) ** 2 <= radius ** 2:
                dragging = True
                offset_x = x - mouse_x
                offset_y = y - mouse_y
        elif event.type == pygame.MOUSEBUTTONUP:
            dragging = False
        elif event.type == pygame.MOUSEMOTION:
            if dragging:
                # Move the circle
                mouse_x, mouse_y = pygame.mouse.get_pos()
                x = mouse_x + offset_x
                y = mouse_y + offset_y

    # Fill the screen with black
    screen.fill((0, 0, 0))

    # Draw the circle
    pygame.draw.circle(screen, color, (x, y), radius)

    # Update the screen
    pygame.display.update()

# Quit Pygame
pygame.quit()
