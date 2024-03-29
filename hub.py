import pygame
from screens.game_screen import GameScreen
from gamemode import GameMode
from screens.main_menu_screen import MainMenuScreen
from screens.high_score_screen import HighScoreScreen

class Hub:
    """ HUB class, provide a central place to hold all the properties that are constantly being accessed """
    def __init__(self):
        """ Initializing properties """
        self.WINDOW_WIDTH = 1280
        self.WINDOW_HEIGHT = 720
        self.BG_COLOR = (125, 125, 125)
        self.main_screen = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.WINDOW_TITLE = "Space Invader by Randy Le"

        self.CLOCK = pygame.time.Clock()

        self.game_mode = GameMode(self)

        self.shoot_sound = pygame.mixer.Sound('wav/Laser.wav')
        self.enemy_dies_sound = pygame.mixer.Sound('wav/Enemy_Dies.wav')
        self.bg_music = pygame.mixer.Sound('wav/bg_music.wav')
        self.prep_sounds()
        self.play_bg_music()

        self.controller = {
            'up': False,
            'down': False,
            'left': False,
            'right': False,
            'shooting': False
        }

        self.delayShot = 360
        self.nextShot = pygame.time.get_ticks() + self.delayShot

        self.game_screen = GameScreen(self)
        self.main_menu_screen = MainMenuScreen(self)
        self.high_score_screen = HighScoreScreen(self)

        self.screen_type = {
            'GameScreen': 1,
            'MainMenuScreen': 2,
            'HighScoreScreen': 3
        }

        self.screen_mode = 2

        self.high_score_board = [400, 600, 300, 25, 120, 1500]

    def displayscreen(self):
        # Display Game Screen
        if self.screen_mode == 1:
            self.game_screen.run()
        elif self.screen_mode == 2:
            self.main_menu_screen.run()
        # Display Main Menu Screen
        elif self.screen_mode == 3:
            self.high_score_screen.run()

    def prep_sounds(self):
        pygame.mixer.music.set_volume(0.1)
        self.enemy_dies_sound.set_volume(0.2)
        self.shoot_sound.set_volume(0.2)

    def play_bg_music(self):
        pygame.mixer.music.load('wav/bg_music.wav')
        pygame.mixer.music.play(-1, 0.0)