from enemies.enemy import Enemy
import pygame
import random
from enemies.enemy_bullet import EnemyBullet


class EnemyTwo(Enemy):
    """ EnemyTwo has the ability to shoot back"""
    def __init__(self, hub):
        super().__init__(hub)

        self.hub = hub
        self.game_screen = self.hub.game_screen

        self.image = pygame.image.load('imgs/Enemies/enemyBlack2.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()

        # Set up wing animation
        self.wing_clock = pygame.time.get_ticks()
        self.wing_nextFrame = 700
        self.wing_index = 0

        self.right_wing_rect = pygame.Rect((0, 0), (17, 55))
        self.left_wing_rect = pygame.Rect((0, 0), (17, 55))

        self.right_wing_list = [pygame.image.load('imgs/Parts/wingRed_0.png'),
                                pygame.image.load('imgs/Parts/wingRed_0_1.png')]
        self.left_wing_list = [pygame.transform.flip(self.right_wing_list[0], True, False),
                               pygame.transform.flip(self.right_wing_list[1], True, False)]
        self.prep_wing()

        # Shoot chance, the lower the number the higher the chance in shooting
        self.shoot_chance = 500

    def update(self):
        super().update()
        self.prep_wing()

        # check if enemy is shooting
        random_number = random.randint(0, self.shoot_chance)
        if random_number is 0:
            enemy_bullet = EnemyBullet(self.hub, self)
            self.game_screen.enemy_bullets.add(enemy_bullet)

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
        self.right_wing_rect.right = self.rect.right + 5
        self.right_wing_rect.top = self.rect.top

        self.left_wing_rect.left = self.rect.left - 5
        self.left_wing_rect.top = self.rect.top