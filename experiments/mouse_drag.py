import pygame

pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Moving Circles")

# Set up the colors
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Set up the circles
circles = [
    {'color': red, 'pos': (100, 100), 'radius': 50},
    {'color': green, 'pos': (200, 200), 'radius': 50},
    {'color': blue, 'pos': (300, 300), 'radius': 50},
    {'color': white, 'pos': (400, 400), 'radius': 50},
]

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the click is inside a circle
            mouse_pos = pygame.mouse.get_pos()
            for circle in circles:
                if ((mouse_pos[0]-circle['pos'][0])**2 + (mouse_pos[1]-circle['pos'][1])**2) < circle['radius']**2:
                    # Set the circle as selected and remember the offset
                    circle['selected'] = True
                    circle['offset'] = (circle['pos'][0]-mouse_pos[0], circle['pos'][1]-mouse_pos[1])
        elif event.type == pygame.MOUSEBUTTONUP:
            # Deselect all circles
            for circle in circles:
                circle['selected'] = False
        elif event.type == pygame.MOUSEMOTION:
            # Move the selected circle
            mouse_pos = pygame.mouse.get_pos()
            for circle in circles:
                if circle.get('selected', False):
                    circle['pos'] = (mouse_pos[0]+circle['offset'][0], mouse_pos[1]+circle['offset'][1])

    # Draw the circles
    screen.fill((0, 0, 0))
    for circle in circles:
        pygame.draw.circle(screen, circle['color'], circle['pos'], circle['radius'])
    pygame.display.flip()

pygame.quit()
