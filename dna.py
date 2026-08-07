import random
import pygame


class DNA:
    def __init__(self, num_genes):
        self.genes = []
        for _ in range(num_genes):
            # Random direction, then normalize so length is 1
            gene = pygame.math.Vector2(
                random.uniform(-1, 1),
                random.uniform(-1, 1),
            )
            if gene.length() > 0:
                gene = gene.normalize()
            self.genes.append(gene)

    def crossover(self, partner_dna):
        # Create a new blank DNA instance for the child
        child_dna = DNA(len(self.genes))
        child_dna.genes = [] # Clear the random vectors generated during init
        
        # Pick a random midpoint in the genetic array split
        midpoint = random.randint(0, len(self.genes) - 1)
        
        # Take genes before the midpoint from Parent A, and after from Parent B
        for i in range(len(self.genes)):
            if i < midpoint:
                child_dna.genes.append(self.genes[i])
            else:
                child_dna.genes.append(partner_dna.genes[i])
                
        return child_dna

    def mutate(self, mutation_rate=0.01):
        # 0.01 mutation rate means roughly a 1% chance for each gene to change
        for i in range(len(self.genes)):
            if random.random() < mutation_rate:
                # Replace with a brand new, normalized random force vector
                gene = pygame.math.Vector2(random.uniform(-1, 1), random.uniform(-1, 1))
                if gene.length() > 0:
                    gene = gene.normalize()
                    gene *= 0.2
                self.genes[i] = gene
        