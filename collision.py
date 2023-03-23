import pygame
import math

pygame.init()

# set up the screen
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# define the colors
black = (0, 0, 0)
white = (255, 255, 255)

# set up the circle
circle_radius = 20
circle_x = 100
circle_y = 100
circle_color = white

# set up the rectangle
rectangle_width = 50
rectangle_height = 100
rectangle_x = 300
rectangle_y = 200
rectangle_color = white

# set up the clock
clock = pygame.time.Clock()

# define a function to check for collision
def is_collision(circle_x, circle_y, circle_radius, rectangle_x, rectangle_y, rectangle_width, rectangle_height):
    # calculate the distance between the center of the circle and the center of the rectangle
    dist_x = abs(circle_x - rectangle_x - rectangle_width/2)
    dist_y = abs(circle_y - rectangle_y - rectangle_height/2)

    if dist_x > (rectangle_width/2 + circle_radius):
        return False
    if dist_y > (rectangle_height/2 + circle_radius):
        return False

    if dist_x <= (rectangle_width/2):
        return True
    if dist_y <= (rectangle_height/2):
        return True

    corner_distance_sq = (dist_x - rectangle_width/2)**2 + (dist_y - rectangle_height/2)**2

    return (corner_distance_sq <= (circle_radius**2))

# main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # fill the screen with black
    screen.fill(black)

    # move the rectangle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        rectangle_x -= 5
    if keys[pygame.K_RIGHT]:
        rectangle_x += 5
    if keys[pygame.K_UP]:
        rectangle_y -= 5
    if keys[pygame.K_DOWN]:
        rectangle_y += 5

    # draw the circle and rectangle
    pygame.draw.circle(screen, circle_color, (circle_x, circle_y), circle_radius)
    pygame.draw.rect(screen, rectangle_color, (rectangle_x, rectangle_y, rectangle_width, rectangle_height))

    # check for collision
    if is_collision(circle_x, circle_y, circle_radius, rectangle_x, rectangle_y, rectangle_width, rectangle_height):
        circle_color = (255, 0, 0)
        rectangle_color = (255, 0, 0)
    else:
        circle_color = white
        rectangle_color = white

    # update the screen
    pygame.display.update()

    # set the frame rate
    clock.tick(60)
