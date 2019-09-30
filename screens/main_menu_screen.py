import pygame
import sys
from pygame.locals import *
from customs.button import Button
from customs.text import Text
from screens.game_screen import GameScreen

class MainMenuScreen:
    def __init__(self, hub):
        self.hub = hub
        self.screen = hub.main_screen

        # Title text
        self.title_text = Text(self.screen, "SPACE INVADER")
        self.prep_title_text()

        # Credit text
        self.credit_text = Text(self.screen, "MADE BY RANDY LE")
        self.prep_credit_text()

        # Play button
        self.play_button = Button(self.hub, "Play")
        self.prep_play_button()

        # Exit button
        self.exit_button = Button(self.hub, "Exit")
        self.prep_exit_button()

        # High Score Button
        self.high_score_button = Button(self.hub, "High Score")
        self.prep_high_score_button()

        # Background Image
        self.bg_image = pygame.image.load('imgs/Backgrounds/black.png')
        self.bg_image = pygame.transform.scale(self.bg_image, (self.hub.WINDOW_WIDTH, self.hub.WINDOW_HEIGHT))
        self.bg_rect = self.bg_image.get_rect()

        # Create enemy score images
        self.enemy_one_score = pygame.image.load('imgs/enemy_one_score.png')
        self.enemy_one_score_rect = self.enemy_one_score.get_rect()
        self.enemy_two_score = pygame.image.load('imgs/enemy_two_score.png')
        self.enemy_two_score_rect = self.enemy_two_score.get_rect()
        self.enemy_three_score = pygame.image.load('imgs/enemy_three_score.png')
        self.enemy_three_score_rect = self.enemy_three_score.get_rect()
        self.prep_enemy_score()

    def run(self):
        self.run_event()
        # self.run_update()
        self.run_draw()

    def run_event(self):
        for event in pygame.event.get():
            if event.type == QUIT:
               pygame.quit()
               sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                self.check_buttons_clicked(mouse_x, mouse_y)

    def run_update(self):
        print('update')

    def run_draw(self):
        self.screen.blit(self.bg_image, self.bg_rect)
        self.title_text.draw()
        self.credit_text.draw()
        self.play_button.draw()
        self.exit_button.draw()
        self.high_score_button.draw()

        self.screen.blit(self.enemy_one_score, self.enemy_one_score_rect)
        self.screen.blit(self.enemy_two_score, self.enemy_two_score_rect)
        self.screen.blit(self.enemy_three_score, self.enemy_three_score_rect)


    def check_buttons_clicked(self, mouse_x, mouse_y):
        if self.play_button.rect.collidepoint(mouse_x, mouse_y):
            self.hub.screen_mode = self.hub.screen_type['GameScreen']
            self.hub.game_screen = GameScreen(self.hub)
            self.hub.game_mode.reset_stats()
        if self.exit_button.rect.collidepoint(mouse_x, mouse_y):
            pygame.quit()
            sys.exit()
        if self.high_score_button.rect.collidepoint(mouse_x, mouse_y):
            self.hub.screen_mode = self.hub.screen_type['HighScoreScreen']
            self.hub.high_score_board.sort(reverse=True)
            self.hub.high_score_screen.update_score()

    def prep_play_button(self):
        self.play_button.rect.center = self.screen.get_rect().center
        self.play_button.rect.centery -= 75
        self.play_button.update_message_position()

    def prep_exit_button(self):
        self.exit_button.rect.center = self.screen.get_rect().center
        self.exit_button.rect.centery += 75
        self.exit_button.update_message_position()

    def prep_high_score_button(self):
        self.high_score_button.rect.center = self.screen.get_rect().center
        self.high_score_button.update_message_position()

    def prep_title_text(self):
        self.title_text.msg_image_rect.centerx = self.screen.get_rect().centerx
        self.title_text.msg_image_rect.y = 50
        self.title_text.update_message()

    def prep_credit_text(self):
        self.credit_text.msg_image_rect.centerx = self.screen.get_rect().centerx
        self.credit_text.msg_image_rect.y = self.screen.get_rect().height - 50
        self.credit_text.update_message()

    def prep_enemy_score(self):
        self.enemy_one_score_rect.centerx = self.screen.get_rect().centerx
        self.enemy_one_score_rect.y = 100

        self.enemy_two_score_rect.centerx = self.screen.get_rect().centerx
        self.enemy_two_score_rect.y = 150

        self.enemy_three_score_rect.centerx = self.screen.get_rect().centerx
        self.enemy_three_score_rect.y = 200
