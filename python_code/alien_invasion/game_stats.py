class GameStats:
    ''' track stats '''

    def __init__(self, ai_game):
        ''' initialize stats '''
        self.settings = ai_game.settings
        self.reset_stats()
        #start game in active state
        self.game_active = False
        #never reset high score
        self.high_score = 0

    def reset_stats(self):
        ''' initialize stats that change during game '''
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
