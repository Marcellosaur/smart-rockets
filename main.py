import pygame
import sys
from rockets import Rocket

# 1. Initialize Pygame modules
pygame.init()

# 2. Setup the display window (Width, Height)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 700
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Smart Rockets - Setup")

# 3. Setup a clock to control the frame rate
clock = pygame.time.Clock()

# Creating a rocket instance
my_rocket = Rocket(SCREEN_WIDTH, SCREEN_HEIGHT)

# 4. The Core Game Loop
while True:
    # Handle user inputs/events (like clicking the "X" to close the window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen with a solid color (Red, Green, Blue)
    screen.fill((40, 44, 52))  # Dark gray background

    # Update physics, then draw the rocket
    my_rocket.update()
    my_rocket.draw(screen)

    # Refresh the display to show the new frame
    pygame.display.flip()

    # Cap the frame rate at 60 frames per second
    clock.tick(60)
