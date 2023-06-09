import pygame
import sys

pygame.init()

size = (1000, 400)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("FPT Testing")
font = pygame.font.Font(None, 20)
clock = pygame.time.Clock()
start = pygame.time.get_ticks()

def show_time():
    current_time = pygame.time.get_ticks() - start
    time_surf = font.render(f'{current_time}', False, 'Red')
    screen.blit(time_surf, (30, 30))


class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = 200
        self.vy = 0
        self.color = 'Red'
    
    def move(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt

        # if self.x < 0 or self.x > size[0] - 5:
        #     self.vx *= -1
        
        # if self.y < 0 or self.y > size[1] - 5:
        #     self.vy *= -1

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), 10)

ball = Ball(100, 200)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()

    # Clear previous screen
    if ball.x < size[0] - 5:
        screen.fill((0, 0, 0))
        dt = clock.tick() / 1000.0
        ball.move(dt)
        ball.draw()

        show_time()

        fps = int(clock.get_fps())
        HUD = font.render(f"FPS: {fps}",False, "Green")
        screen.blit(HUD, (550, 10))
        pygame.display.update()
