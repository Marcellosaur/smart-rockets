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

        # Crash / success state for obstacle navigation
        self.crashed = False
        self.completed = False

    def get_rect(self):
        return pygame.Rect(int(self.position.x), int(self.position.y), self.width, self.height)

    def update(self, obstacles=None, target_position=None, target_radius=20):
        # Stop moving once crashed or reached the target
        if self.crashed or self.completed:
            return

        # Apply this frame's DNA force (if any genes left)
        if self.gene_index < len(self.dna.genes):
            self.acceleration += self.dna.genes[self.gene_index]
            self.gene_index += 1

        self.velocity += self.acceleration
        self.position += self.velocity

        # Reset so next frame only gets the next gene, not stacked forces
        self.acceleration = pygame.math.Vector2(0, 0)

        # Hit the target?
        if target_position is not None:
            center = self.position + pygame.math.Vector2(self.width / 2, self.height / 2)
            if center.distance_to(target_position) < target_radius:
                self.completed = True
                return

        # Crash into screen edges?
        if (
            self.position.x < 0
            or self.position.x + self.width > self.screen_width
            or self.position.y < 0
            or self.position.y + self.height > self.screen_height
        ):
            self.crashed = True
            return

        # Crash into any obstacle?
        if obstacles:
            rocket_rect = self.get_rect()
            for obstacle in obstacles:
                if obstacle.collides_with(rocket_rect):
                    self.crashed = True
                    return

    def draw(self, surface):
        # Draw crashed rockets darker so collisions are easy to see
        if self.crashed:
            color = (120, 120, 120)
        elif self.completed:
            color = (80, 200, 120)
        else:
            color = (255, 255, 255)
        dimensions = (int(self.position.x), int(self.position.y), self.width, self.height)
        pygame.draw.rect(surface, color, dimensions)

    def calculate_fitness(self, target_position):
        # Calculate the straight-line distance between rocket position and target position
        distance = self.position.distance_to(target_position)
        
        # Prevent a Division-by-Zero error if a rocket lands perfectly on the exact pixel center
        if distance < 1:
            distance = 1
            
        # Invert the distance so small distance = massive fitness score
        self.fitness = 1.0 / distance

        # Reward rockets that hit the target; punish those that crash
        if self.completed:
            self.fitness *= 10
        if self.crashed:
            self.fitness *= 0.1
