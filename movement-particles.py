
# Import the necessary libraries
import pygame
import random

# Initialize Pygame
pygame.init()

# Particle class
class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dx = random.uniform(-1, 1)
        self.dy = random.uniform(-1, 1)
        self.lifetime = 60  # Number of frames the particle will exist

    def update(self):
        self.x += self.dx
        self.y += self.dy
        self.lifetime -= 1

    def draw(self, window):
        pygame.draw.circle(window, (200, 200, 200), (int(self.x), int(self.y)), 2)

# Particle system class
class ParticleSystem:
    def __init__(self):
        self.particles = []

    def add_particle(self, x, y):
        self.particles.append(Particle(x, y))

    def update(self):
        for particle in self.particles:
            particle.update()
            if particle.lifetime <= 0:
                self.particles.remove(particle)

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

# Define player properties
player_width = 50
player_height = 50
player_x = (window_width - player_width) // 2
player_y = window_height - player_height

# Main game loop
running = True
clock = pygame.time.Clock()
# Create particle system
particle_system = ParticleSystem()

# Main game loop
running = True
clock = pygame.time.Clock()
while running:
    dt = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= 5
        particle_system.add_particle(player_x + player_width, player_y + player_height // 2)
    if keys[pygame.K_RIGHT] and player_x < window_width - player_width:
        player_x += 5
        particle_system.add_particle(player_x, player_y + player_height // 2)

    particle_system.update()

    window.fill(BLACK)
    pygame.draw.rect(window, WHITE, (player_x, player_y, player_width, player_height))
    particle_system.draw(window)

    pygame.display.flip()

# Quit the game
pygame.quit()
