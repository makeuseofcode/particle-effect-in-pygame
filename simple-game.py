
# Import the necessary libraries
import pygame
import random

# Initialize Pygame
pygame.init()

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
while running:
    dt = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    boundary = player_x < window_width - player_width
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= 5
    if keys[pygame.K_RIGHT] and boundary:
        player_x += 5

    window.fill(BLACK)
    player_pos = (player_x, player_y, player_width, player_height)
    pygame.draw.rect(window, WHITE, player_pos)

    pygame.display.flip()

# Quit the game
pygame.quit()
