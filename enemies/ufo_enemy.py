from pygame.sprite import Sprite
import pygame
import random


class UfoEnemy(Sprite):

    def __init__(self, hub):
        super().__init__()

        self.hub = hub
        self.screen = self.hub.main_screen

        self.image = pygame.image.load('imgs/ufoRed.png')
        self.rect = self.image.get_rect()

        self.random_velocity = random.randint(3, 15)
        self.value = random.randint(100, 200)

        self.prep_ufo()

    def update(self):
        self.rect.x += self.random_velocity

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def prep_ufo(self):
        self.rect.right = self.rect.left
        self.rect.y = 100

    def check_boundaries(self):
        if self.rect.left >= self.screen.get_rect().right:
            return True
        return False