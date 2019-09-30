import pygame
from pygame.sprite import Sprite


class Wall(Sprite):

    def __init__(self, hub):
        super().__init__()

        self.hub = hub
        self.screen = self.hub.main_screen
        self.color = (189,183,107)
        self.rect = pygame.Rect((0,0), (10, 10))

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
