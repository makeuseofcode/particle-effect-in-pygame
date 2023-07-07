
# Import the necessary libraries
import pygame
import random
import math

# Initialize Pygame
pygame.init()


# Particle class
class Particle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.angle = random.uniform(0, 2 * math.pi)
        self.speed = random.uniform(0.5, 1.5)

    def update(self):
        self.angle += 0.02
        self.x += math.cos(self.angle) * self.speed
        self.y += math.sin(self.angle) * self.speed

        if self.x < 0:
            self.x = window_width
        elif self.x > window_width:
            self.x = 0

        if self.y < 0:
            self.y = window_height
        elif self.y > window_height:
            self.y = 0

    def draw(self, window):
        color = (128, 128, 128)
        pos = (int(self.x), int(self.y))
        radius = int(self.radius)
        pygame.draw.circle(window, color, pos, radius)

# Particle system class
class ParticleSystem:
    def __init__(self):
        self.particles = []

    def add_particle(self, x, y, radius):
        self.particles.append(Particle(x, y, radius))

    def update(self):
        for particle in self.particles:
            particle.update()

    def draw(self, window):
        for particle in self.particles:
            particle.draw(window)

# Set up the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Simple Game")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Define player properties
player_width = 50
player_height = 50
player_x = (window_width - player_width) // 2
player_y = window_height - player_height

# Main game loop
running = True
clock = pygame.time.Clock()
# Create particle system for dust effect
particle_system = ParticleSystem()

# Main game loop
running = True
clock = pygame.time.Clock()
while running:
    dt = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    particle_x = random.randint(0, window_width)
    particle_y = random.randint(0, window_height)

    particle_system.add_particle(particle_x, particle_y, 1)

    particle_system.update()

    window.fill((0, 0, 0))
    particle_system.draw(window)

    pygame.display.flip()

# Quit the game
pygame.quit()
