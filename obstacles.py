import pygame


class Obstacle:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, surface):
        wall_color = (100, 104, 112)
        pygame.draw.rect(surface, wall_color, self.rect)

    def collides_with(self, rocket_rect):
        return self.rect.colliderect(rocket_rect)
