import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """ Player ship class """
    def __init__(self, hub):
        super().__init__()
        """ Initializing default values. """
        self.game_hub = hub

        # Create Ship
        self.image = pygame.image.load('imgs/playerShip1_blue.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.centerx = self.game_hub.WINDOW_WIDTH / 2
        self.rect.bottom = self.game_hub.WINDOW_HEIGHT - 20

        # Set Velocity
        self.velocity = self.game_hub.game_mode.ship_speed_factor

        # Set engine thruster default values
        self.thruster_index = 0
        self.thruster_nextFrame = 60
        self.thruster_clock = pygame.time.get_ticks() + self.thruster_nextFrame
        self.thruster_image = [pygame.image.load('imgs/Engine Thrusters/vertical-thrust-01.png'),
                      pygame.image.load('imgs/Engine Thrusters/vertical-thrust-02.png'),
                      pygame.image.load('imgs/Engine Thrusters/vertical-thrust-03.png'),
                      pygame.image.load('imgs/Engine Thrusters/vertical-thrust-04.png')]
        self.thruster_rect = self.thruster_image[self.thruster_index].get_rect()
        self.left_thruster_rect = self.thruster_image[self.thruster_index].get_rect()
        self.right_thruster_rect = self.thruster_image[self.thruster_index].get_rect()
        # Prep engine thruster
        self.prep_thrusters()

    def update(self):
        """ Update the logic of the ship """
        if self.game_hub.controller['right']:
            self.rect.x += self.velocity
        if self.game_hub.controller['left']:
            self.rect.x -= self.velocity

        # Check if the time to change thruster image
        if pygame.time.get_ticks() > self.thruster_clock:
            self.thruster_index = (self.thruster_index + 1) % len(self.thruster_image)
            self.thruster_clock = pygame.time.get_ticks() + self.thruster_nextFrame

        self.check_boundaries()
        self.prep_thrusters()

    def draw(self):
        self.game_hub.main_screen.blit(self.image, self.rect)
        self.game_hub.main_screen.blit(self.thruster_image[self.thruster_index], self.thruster_rect)
        self.game_hub.main_screen.blit(self.thruster_image[self.thruster_index], self.left_thruster_rect)
        self.game_hub.main_screen.blit(self.thruster_image[self.thruster_index], self.right_thruster_rect)


    def check_boundaries(self):
        if self.rect.centerx < 0:
            self.rect.centerx = 0
        if self.rect.centerx > self.game_hub.WINDOW_WIDTH:
            self.rect.centerx = self.game_hub.WINDOW_WIDTH

    def prep_thrusters(self):
        self.thruster_rect.centerx = self.rect.centerx
        self.thruster_rect.top = self.rect.bottom

        self.left_thruster_rect.left = self.rect.left - 5
        self.left_thruster_rect.centery = self.rect.centery + 25

        self.right_thruster_rect.right = self.rect.right + 5
        self.right_thruster_rect.centery = self.rect.centery + 25
