from enemies.enemy import Enemy
import pygame
from enemies.enemy_laser import EnemyLaser
import random


class EnemyThree(Enemy):
    """ Enemy THree has the ability to shoot lasers, but laser is slow """
    def __init__(self, hub):
        super().__init__(hub)

        self.hub = hub
        self.game_screen = self.hub.game_screen

        # Set up enemy
        self.image = pygame.image.load('imgs/Enemies/enemyBlue4.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()

        # Set up wing animations
        self.wing_clock = pygame.time.get_ticks()
        self.wing_nextFrame = 700
        self.wing_index = 0

        self.right_wing_rect = pygame.Rect((0, 0), (30, 58))
        self.left_wing_rect = pygame.Rect((0, 0), (30, 58))

        self.right_wing_list = [pygame.image.load('imgs/Parts/wingBlue_1.png'),
                                pygame.image.load('imgs/Parts/wingBlue_1_1.png')]
        self.left_wing_list = [pygame.transform.flip(self.right_wing_list[0], True, False),
                               pygame.transform.flip(self.right_wing_list[1], True, False)]
        self.prep_wing()

        # Set up shoot rate, the higher the number, the lower chance enemy will fire
        self.shoot_chance = 700

    def update(self):
        super().update()
        self.prep_wing()
        # Random Shooting
        random_number = random.randint(0, self.shoot_chance)
        if random_number is 0:
            enemy_bullet = EnemyLaser(self.hub, self)
            self.game_screen.enemy_bullets.add(enemy_bullet)

        # Check for next animation
        if pygame.time.get_ticks() > self.wing_clock:
            self.wing_clock = pygame.time.get_ticks() + self.wing_nextFrame
            self.wing_index = (self.wing_index + 1) % len(self.right_wing_list)

    def draw(self):
        self.hub.main_screen.blit(self.right_wing_list[self.wing_index], self.right_wing_rect)
        self.hub.main_screen.blit(self.left_wing_list[self.wing_index], self.left_wing_rect)
        super().draw()


    def check_boundaries(self):
        super().check_boundaries()

    def prep_wing(self):
        self.right_wing_rect.right = self.rect.right + 10
        self.right_wing_rect.top = self.rect.top

        self.left_wing_rect.left = self.rect.left - 10
        self.left_wing_rect.top = self.rect.top