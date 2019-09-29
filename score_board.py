import pygame.ftfont
from ship import Ship
from pygame.sprite import Group


class ScoreBoard:
    """ A class to report scoring information """

    def __init__(self, hub):
        self.game_hub = hub
        self.screen_rect = self.game_hub.main_screen.get_rect()

        self.text_color = (30, 30, 30)
        self.font = pygame.ftfont.SysFont(None, 48)

        # Prepare the initial score image.
        """ Turn the score into a rendered image """
        self.prep_score()

        # Initial high score image
        self.prep_highscore()

        # Prepare level image to display
        self.prep_level()

        # Prepare the ship lives
        self.prep_ships()

    def draw(self):
        """ Draw score onto the screen """
        self.game_hub.main_screen.blit(self.score_image, self.score_rect)
        self.game_hub.main_screen.blit(self.high_score_image, self.high_score_rect)
        self.game_hub.main_screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.game_hub.main_screen)

    def prep_score(self):
        """ Turn the score into a rendered image """
        self.score_str = "{:,}".format(self.game_hub.game_mode.score)
        self.score_image = self.font.render(self.score_str, True, self.text_color, self.game_hub.BG_COLOR)

        # Display the score at the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_highscore(self):
        """ Turn the high score into a rendered image. """
        self.high_score = int(round(self.game_hub.game_mode.high_score, -1))
        self.high_score_str = "{:,}".format(self.high_score)
        self.high_score_image = self.font.render(self.high_score_str, True, self.text_color, self.game_hub.BG_COLOR)

        # Center the high score at the top of the screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        """ Turn the level into a rendered image. """
        self.level_image = self.font.render(str(self.game_hub.game_mode.level), True,
                                            self.text_color, self.game_hub.BG_COLOR)
        # Position the level below the score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        """ Show how many ships are left. """
        self.ships = Group()
        for ship_number in range(self.game_hub.game_mode.player_lives):
            ship = Ship(self.game_hub)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
