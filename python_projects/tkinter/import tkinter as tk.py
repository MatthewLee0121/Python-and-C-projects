import pygame
import sys
# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
GOLD_COLOR = (255, 215, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple RTS Game")

# Game variables
gold = 0
workers = 0
soldiers = 0

# Load images
worker_img = pygame.image.load(r"C:\Users\mat_m\Downloads\image0.gif")  # Replace 'worker.png' with your image file
soldier_img = pygame.image.load(r"C:\Users\mat_m\Downloads\image0.gif")  # Replace 'soldier.png' with your image file
base_img = pygame.image.load(r"C:\Users\mat_m\Downloads\image0.gif")  # Replace 'base.png' with your image file

# Define game objects
base_rect = base_img.get_rect(center=(WIDTH // 2, HEIGHT // 2))
worker_rect = worker_img.get_rect(center=(50, 50))
soldier_rect = soldier_img.get_rect(center=(50, 150))

# Variables for unit movement
selected_unit = None
selected_rect = None

# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                if worker_rect.collidepoint(event.pos):
                    selected_unit = 'worker'
                    selected_rect = worker_rect
                elif soldier_rect.collidepoint(event.pos):
                    selected_unit = 'soldier'
                    selected_rect = soldier_rect
                else:
                    if selected_unit:
                        selected_rect.center = event.pos
                        selected_unit = None

    # Clear the screen
    screen.fill(WHITE)

    # Draw base and units
    screen.blit(base_img, base_rect)
    screen.blit(worker_img, worker_rect)
    screen.blit(soldier_img, soldier_rect)

    # Draw resource count
    font = pygame.font.Font(None, 36)
    text_surface = font.render(f'Gold: {gold}', True, GOLD_COLOR)
    screen.blit(text_surface, (10, 10))

    # Draw unit counts
    text_surface = font.render(f'Workers: {workers}', True, GOLD_COLOR)
    screen.blit(text_surface, (10, 50))
    text_surface = font.render(f'Soldiers: {soldiers}', True, RED)
    screen.blit(text_surface, (10, 90))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
