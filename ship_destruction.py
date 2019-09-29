import pygame
from pygame.sprite import Sprite


class ShipDestruction(Sprite):
    def __init__(self, hub, player, type='player'):
        super().__init__()

        self.hub = hub
        self.player = player
        self.nextFrame = 120
        self.index = 0
        self.type = type
        self.images = [pygame.image.load('imgs/Damage/playerShip1_damage1.png'),
                       pygame.image.load('imgs/Damage/playerShip1_damage2.png'),
                       pygame.image.load('imgs/Damage/playerShip1_damage3.png')]
        self.rect = self.images[0].get_rect()
        self.clock = pygame.time.get_ticks()
        self.prep_destruction()

    def update(self):
        if pygame.time.get_ticks() > self.clock:
            self.clock = pygame.time.get_ticks() + self.nextFrame
            self.index = (self.index + 1) % len(self.images)

    def draw(self):
        self.hub.main_screen.blit(self.images[self.index], self.rect)

    def check_if_finished(self):
        if self.type == 'player':
            if self.index == len(self.images)-1:
                self.hub.game_screen.destructions.remove(self)
                return True
            return False
        elif self.type == 'enemy':
            if self.index == len(self.images)-1:
                try:
                    self.hub.game_screen.enemy_destructions.remove(self)
                except pygame.error:
                    print('error list')

    def prep_destruction(self):
        self.rect.center = self.player.rect.center

