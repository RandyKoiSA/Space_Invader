import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """ A class to manage bullets fired from the ship """

    def __init__(self, hub, player):
        # Initialize default values
        super().__init__()
        self.game_hub = hub
        self.velocity = self.game_hub.game_mode.bullet_speed_factor
        self.width = 5
        self.height = 25

        self.image = pygame.image.load('imgs/lasers/laserBlue02.png')
        self.rect = self.image.get_rect()

        # position the bullet
        self.rect.centerx = player.rect.centerx
        self.rect.top = player.rect.top

    def update(self):
        """ Update the logic of the bullet """
        self.rect.y -= self.velocity

    def draw(self):
        """ Display the bullet onto the screen """
        self.game_hub.main_screen.blit(self.image, self.rect)
