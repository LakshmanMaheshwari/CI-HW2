import pygame
import random

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Nuclear Explosion Simulation")

# Define colors
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
RED = (255, 0, 0)
GRAY = (128, 128, 128)
BLACK = (0, 0, 0)

class Particle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.radius = random.randint(1, 3)
        self.dx = random.uniform(-1, 1)
        self.dy = random.uniform(-1, 1)

    def move(self):
        self.x += self.dx
        self.y += self.dy

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

# Smoke Particles
num_particles = 1000
smoke_particles = [Particle(width // 2, height, GRAY) for _ in range(num_particles)]

# Fire Particles
num_fire_particles = 1000
fire_particles = [Particle(width // 2, height, ORANGE) for _ in range(num_fire_particles)]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(BLACK)
    for particle in smoke_particles:
        particle.move()
        particle.draw(screen)
        # Reset smoke particles if they go out of screen
        if particle.y < 0 or particle.x < 0 or particle.x > width:
            particle.x = width // 2
            particle.y = height
            particle.dx = random.uniform(-1, 1)
            particle.dy = random.uniform(-1, 1)

    for particle in fire_particles:
        particle.move()
        particle.draw(screen)
        # Reset fire particles if they go out of screen
        if particle.y < 0 or particle.x < 0 or particle.x > width:
            particle.x = width // 2
            particle.y = height
            particle.dx = random.uniform(-1, 1)
            particle.dy = random.uniform(-1, 1)

    pygame.display.update()

    pygame.time.Clock().tick(60)

pygame.quit()
