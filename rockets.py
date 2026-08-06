import pygame
from dna import DNA


class Rocket:
    def __init__(self, screen_width, screen_height, dna=None, lifespan=200):
        
        self.fitness = 0
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
        self.acceleration = pygame.math.Vector2(0, -0)

        # DNA dictates the rocket's force vector, or a random one if none provided
        self.dna = dna if dna is not None else DNA(lifespan)
        self.gene_index = 0  # which gene to use this frame

    def update(self):
        # Apply this frame's DNA force (if any genes left)
        if self.gene_index < len(self.dna.genes):
            self.acceleration += self.dna.genes[self.gene_index]
            self.gene_index += 1

        self.velocity += self.acceleration
        self.position += self.velocity

        # Reset so next frame only gets the next gene, not stacked forces
        self.acceleration = pygame.math.Vector2(0, 0)

    def draw(self, surface):
        # Draw the rocket instance onto the provided screen surface
        white_color = (255, 255, 255)
        dimensions = (int(self.position.x), int(self.position.y), self.width, self.height)
        pygame.draw.rect(surface, white_color, dimensions)

    def calculate_fitness(self, target_position):
        # Calculate the straight-line distance between rocket position and target position
        distance = self.position.distance_to(target_position)
        
        # Prevent a Division-by-Zero error if a rocket lands perfectly on the exact pixel center
        if distance < 1:
            distance = 1
            
        # Invert the distance so small distance = massive fitness score
        self.fitness = 1.0 / distance
