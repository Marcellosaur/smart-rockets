import pygame
import sys

# 1. Initialize Pygame modules
pygame.init()

# 2. Setup the display window (Width, Height)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 700
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Smart Rockets - Setup")

# 3. Setup a clock to control the frame rate
clock = pygame.time.Clock()

# ROCKET SIZE
ROCKET_WIDTH = 10
ROCKET_HEIGHT = 40

# ROCKET POSITION
rect_x = (SCREEN_WIDTH / 2) - (ROCKET_WIDTH / 2)
rect_y = SCREEN_HEIGHT - ROCKET_HEIGHT

# 4. The Core Game Loop
while True:
    # Handle user inputs/events (like clicking the "X" to close the window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen with a solid color (Red, Green, Blue)
    screen.fill((40, 44, 52))  # Dark gray background

    # DRAW ROCKET
    white_color = (255, 255, 255)
    rectangle_dimensions = (rect_x, rect_y, ROCKET_WIDTH, ROCKET_HEIGHT)
    
    pygame.draw.rect(screen, white_color, rectangle_dimensions)

    # Refresh the display to show the new frame
    pygame.display.flip()

    # Cap the frame rate at 60 frames per second
    clock.tick(60)
