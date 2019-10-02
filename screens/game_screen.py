import pygame
import sys
from pygame.locals import *
from pygame.sprite import Group
from players.bullet import Bullet
from players.ship import Ship
from enemies.enemy import Enemy
from time import sleep
from score_board import ScoreBoard
import random
from enemies.enemy_two import EnemyTwo
from enemies.enemy_three import EnemyThree
from enemies.ship_destruction import ShipDestruction
from enemies.ufo_enemy import UfoEnemy
from wall import Wall

class GameScreen:
    """ Game screen, were the game starts """
    def __init__(self, hub):
        """ Initializing default values """
        self.hub = hub
        self.screen = self.hub.main_screen
        # Initialize player ship: This will be remove as we will loading in levels soon
        self.player_ship = Ship(self.hub)

        # Create a group for bullets
        self.bullets = Group()

        # Create a group for enemies
        self.enemies = Group()

        # Create a group for player destruction
        self.destructions = Group()

        # Create a group for enemy destruction
        self.enemy_destructions = Group()

        # Create a group for random ufos
        self.ufos = Group()

        # Create a group for walls
        self.walls = Group()
        # Wall is only initialize onced during the entire game.
        self.create_walls()

        # Create enemy bullets when spawned
        self.enemy_bullets = Group()

        # Get a test enemy to get size and width
        self.enemy = Enemy(self.hub)

        self.available_space_x = self.hub.WINDOW_WIDTH - 2 * self.enemy.rect.width
        self.number_enemies_x = int(self.available_space_x / (2 * self.enemy.rect.width))
        self.number_of_rows = 3

        # Create score board
        self.sb = ScoreBoard(self.hub)

        # Background Image
        self.bg_image = pygame.image.load('imgs/Backgrounds/black.png')
        self.bg_image = pygame.transform.scale(self.bg_image, (self.hub.WINDOW_WIDTH, self.hub.WINDOW_HEIGHT))
        self.bg_rect = self.bg_image.get_rect()

    def run(self):
        self.run_event()
        self.run_update()
        self.run_draw()

    def run_event(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == K_a:
                    self.hub.controller['left'] = True
                    self.hub.controller['right'] = False
                if event.key == K_d:
                    self.hub.controller['right'] = True
                    self.hub.controller['left'] = False
                if event.key == K_SPACE:
                    self.hub.controller['shooting'] = True
                if event.key == K_t:
                    self.create_fleet()

            if event.type == KEYUP:
                if event.key == K_a:
                    self.hub.controller['left'] = False
                if event.key == K_d:
                    self.hub.controller['right'] = False
                if event.key == K_SPACE:
                    self.hub.controller['shooting'] = False

    def run_update(self):
        # add ufo
        random_ufo = random.randint(0, 500)
        if random_ufo is 0:
            print('ufo spawned')
            ufo = UfoEnemy(self.hub)
            self.ufos.add(ufo)

        if self.hub.controller['shooting'] is True and pygame.time.get_ticks() > self.hub.nextShot:
            self.hub.nextShot = pygame.time.get_ticks() + self.hub.delayShot
            self.add_bullet()

        self.player_ship.update()
        self.update_bullets()
        self.update_enemies()
        self.update_enemy_bullets()
        self.update_player_destruction()
        self.update_enemy_destruction()
        self.update_ufos()

    def run_draw(self):
        self.screen.blit(self.bg_image, self.bg_rect)

        self.draw_walls()
        self.player_ship.draw()
        self.draw_bullets()
        self.draw_enemies()
        self.enemy_bullets.draw(self.screen)
        self.draw_player_destruction()
        self.draw_enemy_destruction()
        self.draw_ufos()
        self.sb.draw()

    def add_bullet(self):
        new_bullet = Bullet(self.hub, self.player_ship)
        self.bullets.add(new_bullet)
        self.hub.shoot_sound.play()

    def update_bullets(self):
        for bullet in self.bullets:
            bullet.update()

            if bullet.rect.top < 0:
                self.bullets.remove(bullet)

        self.update_bullet_collision()

    def draw_bullets(self):
        for bullet in self.bullets:
            bullet.draw()

    def create_fleet(self):
        for enemy_number in range(self.number_enemies_x):
            for number_row in range(self.number_of_rows):
                # Create an alien and place it in the row
                random_number = random.randint(0, 2)
                if random_number is 0:
                    new_enemy = Enemy(self.hub)
                elif random_number is 1:
                    new_enemy = EnemyTwo(self.hub)
                elif random_number is 2:
                    new_enemy = EnemyThree(self.hub)
                else:
                    new_enemy = Enemy(self.hub)

                new_enemy.rect.x = self.enemy.rect.width + 2 * self.enemy.rect.width * enemy_number
                new_enemy.rect.y = self.enemy.rect.height + 2 * self.enemy.rect.height * number_row
                self.enemies.add(new_enemy)

    def create_walls(self):
        # Create left wall
        for i in range (0, 15):
            for j in range (0 ,5):
                wall = Wall(self.hub)
                wall.rect.x = (wall.rect.width * i) + 100
                wall.rect.y = (self.screen.get_rect().height - 200) + (wall.rect.height * j)
                self.walls.add(wall)

        # Create middle right wall
        for i in range (0, 15):
            for j in range (0, 5):
                wall = Wall(self.hub)
                wall.rect.x = (wall.rect.width * i) + self.screen.get_rect().centerx + 150
                wall.rect.y = (self.screen.get_rect().height - 200) + (wall.rect.height * j)
                self.walls.add(wall)

        # Create middle middle wall
        for i in range (0, 8):
            for j in range (0, 5):
                wall = Wall(self.hub)
                wall.rect.x = (wall.rect.width * i) + self.screen.get_rect().centerx
                wall.rect.y = (self.screen.get_rect().height - 200) + (wall.rect.height * j)
                self.walls.add(wall)

            for j in range(0, 5):
                wall = Wall(self.hub)
                wall.rect.x = self.screen.get_rect().centerx - (wall.rect.width * i)
                wall.rect.y = (self.screen.get_rect().height - 200) + (wall.rect.height * j)
                self.walls.add(wall)

        # Create middle left wall
        for i in range (0, 15):
            for j in range (0, 5):
                wall = Wall(self.hub)
                wall.rect.x = self.screen.get_rect().centerx - 150 - (wall.rect.width * i)
                wall.rect.y = (self.screen.get_rect().height - 200) + (wall.rect.height * j)
                self.walls.add(wall)

        # Create right wall
        for i in range (0, 15):
            for j in range (0, 5):
                wall = Wall(self.hub)
                wall.rect.x = self.screen.get_rect().width - 100 - (wall.rect.width * i)
                wall.rect.y = (self.screen.get_rect().height - 200) + (wall.rect.height * j)
                self.walls.add(wall)

    def update_enemies(self):
        # Loop through all the enemies in the list
        # Update the enemy
        for enemy in self.enemies:
            # Update the enemy
            enemy.update()

            # Check if the enemy has hit the bottom of the screen.
            if enemy.rect.top > self.hub.WINDOW_HEIGHT:
                self.enemies.remove(enemy)
                print(len(self.enemies))

            # Check if the enemy collided with the player
            if pygame.sprite.spritecollideany(self.player_ship, self.enemies):
                self.ship_hit()
                self.hub.enemy_dies_sound.play()

    def draw_enemies(self):
        for enemy in self.enemies:
            enemy.draw()

    def update_bullet_collision(self):
        collisions = pygame.sprite.groupcollide(self.bullets, self.enemies, True, True)
        # No more enemies on the screen, increase level
        if len(self.enemies) <= 0:
            self.bullets.empty()
            self.hub.game_mode.increase_speed()
            self.create_fleet()
            self.hub.game_mode.level += 1
            self.sb.prep_level()

        # Enemies has been hit
        if collisions:
            for enemies in collisions.values():
                self.hub.game_mode.score += self.hub.game_mode.enemy_point_value * len(enemies)
                self.hub.enemy_dies_sound.play()

                # add enemy destruction
                for enemy in enemies:
                    self.hub.game_mode.score += enemy.value
                    destruction = ShipDestruction(self.hub, enemy, type='enemy')
                    self.enemy_destructions.add(destruction)

            self.sb.prep_score()
            self.check_high_score()

        # Ufo has been hit
        collisions = pygame.sprite.groupcollide(self.bullets, self.ufos, True, True)
        if collisions:
            for ufos in collisions.values():
                for ufo in ufos:
                    self.hub.game_mode.score += ufo.value

    def ship_hit(self):
        """ Respond to ship being hit by aliens"""
        # Decrement ships left
        self.hub.game_mode.player_lives -= 1

        # Update scoreboard
        self.sb.prep_ships()

        # Empty the list of aliens and bullets
        self.enemies.empty()
        self.bullets.empty()
        self.enemy_bullets.empty()
        # Check if there is any lives left
        if self.hub.game_mode.player_lives > 0:
            # Create new fleet
            self.create_fleet()

        # Game Over
        if self.hub.game_mode.player_lives <= 0:
            self.hub.screen_mode = self.hub.screen_type['MainMenuScreen']
            pygame.mouse.set_visible(True)
            self.add_score()

        # Pause
        sleep(0.5)

    def check_high_score(self):
        """ Check to see if there's a new high score. """
        if self.hub.game_mode.score > self.hub.game_mode.high_score:
            self.hub.game_mode.high_score = self.hub.game_mode.score
            self.sb.prep_highscore()

    def add_score(self):
        # At the end of the game, we add the score to the score board.
        score_list = self.hub.high_score_board
        score = self.hub.game_mode.score
        self.hub.high_score_board.sort(reverse=True)
        if len(score_list) is 10:
            if score > score_list[-1]:
                score_list[-1] = score
                self.hub.high_score_board.sort(reverse=True)
        else:
            score_list.append(score)
            self.hub.high_score_board.sort(reverse=True)

    def update_enemy_bullets(self):
        # Remove the enemy bullets from the game if it reaches the bottom of the screen
        for enemy in self.enemy_bullets:
            enemy.update()
            if enemy.check_boundaries():
                self.enemy_bullets.remove()

        self.update_enemy_bullets_collision()

    def update_enemy_bullets_collision(self):
        """ Checks if the player is hit by the enemy's bullet """
        for bullet in self.enemy_bullets:
            if bullet.rect.colliderect(self.player_ship) and self.hub.game_mode.death is False:
                self.hub.game_mode.death = True
                destruction = ShipDestruction(self.hub, self.player_ship)
                self.destructions.add(destruction)
                break

        collisions = pygame.sprite.groupcollide(self.enemy_bullets, self.walls, True, True)
        collisions = pygame.sprite.groupcollide(self.bullets, self.walls, True, True)

    def draw_player_destruction(self):
        for destruction in self.destructions:
            destruction.draw()

    def update_player_destruction(self):
        for destruction in self.destructions:
            destruction.update()
            if destruction.check_if_finished():
                self.ship_hit()

    def draw_enemy_destruction(self):
        for destruction in self.enemy_destructions:
            destruction.draw()

    def update_enemy_destruction(self):
        for destruction in self.enemy_destructions:
            destruction.check_if_finished()
            destruction.update()

    def update_ufos(self):
        for ufo in self.ufos:
            ufo.update()

            if ufo.check_boundaries():
                self.ufos.remove(ufo)

    def draw_ufos(self):
        for ufo in self.ufos:
            ufo.draw()

    def draw_walls(self):
        for wall in self.walls:
            wall.draw()
