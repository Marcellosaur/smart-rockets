import random
from rockets import Rocket

class Population:
    def __init__(self, size, screen_width, screen_height, lifespan):
        # Store our list of rocket objects
        self.rockets = []
        self.pop_size = size
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.lifespan = lifespan
        
        # Instantiate a population full of distinct rocket instances
        for _ in range(self.pop_size):
            self.rockets.append(Rocket(screen_width, screen_height, lifespan=lifespan))

    def update(self, obstacles=None, target_position=None, target_radius=20):
        # Update every single rocket in our pool
        for rocket in self.rockets:
            rocket.update(obstacles, target_position, target_radius)

    def draw(self, surface):
        # Draw every single rocket onto the screen
        for rocket in self.rockets:
            rocket.draw(surface)

    def evaluate(self, target_pos):
        max_fitness = 0
        for rocket in self.rockets:
            rocket.calculate_fitness(target_pos)
            if rocket.fitness > max_fitness:
                max_fitness = rocket.fitness
                
        # 2. Normalize fitness scores between 0 and 1
        # This makes scaling the mating pool much easier
        if max_fitness > 0:
            for rocket in self.rockets:
                rocket.fitness /= max_fitness

    def selection(self):
        mating_pool = []
        
        # 1. Build the mating pool list
        for rocket in self.rockets:
            # Turn normalized fitness into an integer score (0 to 100)
            n = int(rocket.fitness * 100)
            for _ in range(n):
                mating_pool.append(rocket.dna)
                
        # 2. Handle edge case: if nobody got near the target, fill pool with everyone
        if len(mating_pool) == 0:
            mating_pool = [rocket.dna for rocket in self.rockets]

        # 3. Create a brand-new generation of rocket objects
        new_rockets = []
        for _ in range(self.pop_size):
            # Pick two random parent DNA profiles from our weighted pool
            parent_a = random.choice(mating_pool)
            parent_b = random.choice(mating_pool)
            
            # Combine their DNA and apply mutations
            child_dna = parent_a.crossover(parent_b)
            child_dna.mutate(mutation_rate=0.01)
            
            # Create a brand new rocket using this unique child DNA
            new_rockets.append(Rocket(self.screen_width, self.screen_height, dna=child_dna, lifespan=self.lifespan))
            
        # Overwrite the old dead population with the new generation
        self.rockets = new_rockets