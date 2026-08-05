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