import pygame


class Rocket:
    def __init__(self, screen_width, screen_height):
        # Storing screen dimensions for position calculations
        self.screen_width = screen_width
        self.screen_height = screen_height
        
        # Dimensions of individual rocket
        self.width = 10
        self.height = 40
        
        # Physics Vectors
        # Start at the bottom center launchpad position
        start_x = (self.screen_width / 2) - (self.width / 2)
        start_y = self.screen_height - self.height
        self.position = pygame.math.Vector2(start_x, start_y)
        
        # Starts completely still
        self.velocity = pygame.math.Vector2(0, 0)
        
        # Acceleration dictates how much velocity changes per frame
        # We start with a constant upward thrust (negative Y goes UP)
        self.acceleration = pygame.math.Vector2(0, -0.1)

    def update(self):
        # 1. Update velocity by adding acceleration
        self.velocity += self.acceleration
        
        # 2. Update position by adding velocity
        self.position += self.velocity
        
        # 3. Reset acceleration so it doesn't infinitely compound exponentially
        # (For now, we keep it constant, but later DNA forces will require resetting)

    def draw(self, surface):
        # Draw the rocket instance onto the provided screen surface
        white_color = (255, 255, 255)
        dimensions = (int(self.position.x), int(self.position.y), self.width, self.height)
        pygame.draw.rect(surface, white_color, dimensions)