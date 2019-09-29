from customs.text import Text
import pygame
import sys
from customs.button import Button
from pygame.locals import *


class HighScoreScreen:
    """ High score screen shows all the highest scored earned in the game. """
    def __init__(self, hub):
        self.hub = hub
        self.screen = hub.main_screen
        self.bg_color = (155, 155, 155)

        # Create Title Text
        self.title_text = Text(self.screen, 'HIGH SCORE', background_color=self.bg_color)

        # Create back button
        self.back_button = Button(self.hub, 'Back')
        self.prep_back_button()

        # Create Score Text
        self.score_one = Text(self.screen, '1:', background_color=self.bg_color)
        self.score_two = Text(self.screen, '2:', background_color=self.bg_color)
        self.score_three = Text(self.screen, '3:', background_color=self.bg_color)
        self.score_four = Text(self.screen, '4:', background_color=self.bg_color)
        self.score_five = Text(self.screen, '5:', background_color=self.bg_color)
        self.score_six = Text(self.screen, '6:', background_color=self.bg_color)
        self.score_seven = Text(self.screen, '7:', background_color=self.bg_color)
        self.score_eight = Text(self.screen, '8:', background_color=self.bg_color)
        self.score_nine = Text(self.screen, '9:', background_color=self.bg_color)
        self.score_ten = Text(self.screen, '10:', background_color=self.bg_color)

        self.score_list = {
            0: self.score_one,
            1: self.score_two,
            2: self.score_three,
            3: self.score_four,
            4: self.score_five,
            5: self.score_six,
            6: self.score_seven,
            7: self.score_eight,
            8: self.score_nine,
            9: self.score_ten
        }
        self.prep_text()

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
                self.button_pressed(mouse_x, mouse_y)

    def run_draw(self):
        self.screen.fill(self.bg_color)
        # Draw all the text score
        for score_text in self.score_list.values():
            score_text.draw()

        # Draw the title
        self.title_text.draw()

        # Draw Back Button
        self.back_button.draw()

    def prep_text(self):
        # Prep Title
        self.title_text.msg_image_rect.centerx = self.screen.get_rect().centerx
        self.title_text.msg_image_rect.y = self.screen.get_rect().top + 50

        index = 1
        # Prep all the scores
        for score_text in self.score_list.values():
            score_text.msg_image_rect.left = self.title_text.msg_image_rect.left
            score_text.msg_image_rect.y = self.screen.get_rect().top + (index * 50) + 100
            index += 1
            score_text.update_message()

    def update_score(self):
        if self.hub.high_score_board != []:
            for index in range (0, len(self.hub.high_score_board)):
                self.score_list[index].message = str(index+1) + ': ' + str(self.hub.high_score_board[index])
                self.score_list[index].update_message()

    def prep_back_button(self):
        self.back_button.rect.left = self.screen.get_rect().left + 20
        self.back_button.rect.top = self.screen.get_rect().top + 20
        self.back_button.update_message_position()

    def button_pressed(self, mouse_x, mouse_y):
        if self.back_button.rect.collidepoint(mouse_x, mouse_y):
            self.hub.screen_mode = self.hub.screen_type['MainMenuScreen']