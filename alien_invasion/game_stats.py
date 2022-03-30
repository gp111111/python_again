class GameStats():
    """track the game statistics infomations"""

    def __init__(self,ai_settings):
        """initialize the statistics infomaions"""
        self.ai_settings = ai_settings
        self.reset_stats()
      
        #游戏启动的时候处于非活动状态,创建play键，按了play键之后才开始游戏
        self.game_active = False

        #任何情况下都不应该重置最高分
        self.high_score = 0


    def reset_stats(self):
        """initialize the changeable statistics infomations during the game."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1