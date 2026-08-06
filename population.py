from rockets import Rocket

class Population:
    def __init__(self, size, screen_width, screen_height, lifespan):
        # Store our list of rocket objects
        self.rockets = []
        self.pop_size = size
        
        # Instantiate a population full of distinct rocket instances
        for _ in range(self.pop_size):
            self.rockets.append(Rocket(screen_width, screen_height, lifespan=lifespan))

    def update(self):
        # Update every single rocket in our pool
        for rocket in self.rockets:
            rocket.update()

    def draw(self, surface):
        # Draw every single rocket onto the screen
        for rocket in self.rockets:
            rocket.draw(surface)

    def evaluate(self, target_pos):
        # 1. Command every rocket to calculate its own fitness score
        for rocket in self.rockets:
            rocket.calculate_fitness(target_pos)