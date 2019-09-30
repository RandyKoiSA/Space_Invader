class GameMode:
    """ Tracks statistics and the win / lose condition """
    def __init__(self, hub):
        """ Initializing default values """
        self.hub = hub
        self.player_lives = 3
        self.speedup_scale = 1.1
        self.ship_speed_factor = 3
        self.bullet_speed_factor = 2
        self.enemy_speed_factor = 3
        self.level = 0
        self.score = 0
        self.enemy_point_value = 50
        self.high_score = 0
        self.death = False

    def reset_stats(self):
        self.player_lives = 3
        self.level = 0
        self.score = 0
        self.enemy_point_value = 50

    def increase_speed(self):
        """ Increase speed """
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.enemy_speed_factor *= self.speedup_scale
        self.enemy_speed_factor *= self.speedup_scale
        self.enemy_point_value += 50

    def add_new_high_score(self):
        # when the board is empty or less than 10
        if self.hub.high_score_board is [] or len(self.hub.high_score_board) < 10:
            self.hub.high_score_board.append(self.score)
        # check if the high score board is full
        if len(self.hub.high_score_board) >= 10:
            if self.score > self.hub.high_score_board[-1]:
                self.hub.high_score_board[-1] = self.score
