import pygame
from pygame.sprite import Sprite

class EnemyBullet(Sprite):
    def __init__(self, hub, enemy):
        super().__init__()

        self.hub = hub
        self.screen = self.hub.main_screen

        self.velocity = 3
        self.width = 5
        self.height = 25

        self.image = pygame.image.load('imgs/lasers/laserGreen04.png')
        self.rect = self.image.get_rect()

        self.rect.centerx = enemy.rect.centerx
        self.rect.top = enemy.rect.top

    def update(self):
        self.rect.y += self.velocity

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def check_boundaries(self):
        if self.rect.top >= self.screen.get_rect().height:
            return True
        return False