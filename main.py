import pygame
import sys
from rockets import Rocket
from dna import DNA
from population import Population
from obstacles import Obstacle

# 1. Initialize Pygame modules
pygame.init()

# 2. Setup the display window (Width, Height)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 700
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Smart Rockets - Setup")

# 3. Setup a clock to control the frame rate
clock = pygame.time.Clock()

# Creating a rocket population with lifespan dna
POPULATION_SIZE = 100
LIFESPAN = 200 


# # Instantiate the entire pool at once
population = Population(POPULATION_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT, LIFESPAN)
# # --------------------------------

# --- NEW TARGET PROPERTIES ---
TARGET_RADIUS = 20
# Center the target horizontally, place it 100 pixels down from the top wall
target_x = SCREEN_WIDTH / 2
target_y = 100
target_position = pygame.math.Vector2(target_x, target_y)
# -----------------------------

# Horizontal barrier between the launch pad and the target
obstacles = [
    Obstacle(SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2, 300, 20),
]

lifecycle_counter = 0
# 4. The Core Game Loop
while True:
    # Handle user inputs/events (like clicking the "X" to close the window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen with a solid color (Red, Green, Blue)
    screen.fill((40, 44, 52))  # Dark gray background

    # --- DRAW TARGET ---
    # Pygame expects: (surface, color, center_coordinates_tuple, radius)
    target_color = (235, 87, 87)  # Soft red color
    pygame.draw.circle(screen, target_color, (int(target_position.x), int(target_position.y)), TARGET_RADIUS)
    # -------------------

    # --- DRAW OBSTACLES ---
    for obstacle in obstacles:
        obstacle.draw(screen)
    # ---------------------

    if lifecycle_counter < LIFESPAN:
        population.update(obstacles, target_position, TARGET_RADIUS)
        lifecycle_counter += 1
    else:
        population.evaluate(target_position)
        population.selection()
        lifecycle_counter = 0
        print("Generation finished! Selecting new population...")
    
    population.draw(screen)

    # Refresh the display to show the new frame
    pygame.display.flip()

    # Cap the frame rate at 60 frames per second
    clock.tick(60)
