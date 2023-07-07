
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
        self.lifetime = 60  

    def update(self):
        self.x += self.dx
        self.y += self.dy
        self.lifetime -= 1

    def draw(self, window):
        color = (200, 200, 200)
        position = (int(self.x), int(self.y))
        pygame.draw.circle(window, color, position, 2)

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

    particle_y = player_y + player_height // 2
    particle_x = player_x + player_width

    keys = pygame.key.get_pressed()
    boundary = player_x < window_width - player_width
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= 5
        particle_system.add_particle(particle_x, particle_y)
    if keys[pygame.K_RIGHT] and boundary:
        player_x += 5
        particle_system.add_particle(player_x, particle_y)

    particle_system.update()

    window.fill(BLACK)
    player_pos = (player_x, player_y, player_width, player_height)
    pygame.draw.rect(window, WHITE, player_pos)
    particle_system.draw(window)

    pygame.display.flip()

# Quit the game
pygame.quit()
