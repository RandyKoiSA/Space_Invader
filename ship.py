import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """ Player ship class """
    def __init__(self, hub):
        super().__init__()
        """ Initializing default values. """
        self.game_hub = hub

        self.image = pygame.image.load('imgs/playerShip1_blue.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.centerx = self.game_hub.WINDOW_WIDTH / 2
        self.rect.bottom = self.game_hub.WINDOW_HEIGHT - 5
        self.velocity = self.game_hub.game_mode.ship_speed_factor

    def update(self):
        """ Update the logic of the ship """
        if self.game_hub.controller['right']:
            self.rect.x += self.velocity
        if self.game_hub.controller['left']:
            self.rect.x -= self.velocity

        self.check_boundaries()

    def draw(self):
        self.game_hub.main_screen.blit(self.image, self.rect)

    def check_boundaries(self):
        if self.rect.centerx < 0:
            self.rect.centerx = 0
        if self.rect.centerx > self.game_hub.WINDOW_WIDTH:
            self.rect.centerx = self.game_hub.WINDOW_WIDTH
