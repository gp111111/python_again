class Settings():
    """Storage the all settings in ALIEN INVASION"""

    def __init__(self):
        """Iinitialize the game static setting"""
        #screen setting
        self.screen_width = 700
        self.screen_height = 700
        self.bg_color =(160,224,0)

        #ship设置
        self.ship_limit = 3

        #bullet设置
        
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed = 3

        #ufo设置
        self.fleet_drop_speed = 4
        
        #速度调整scale
        self.speedup_scale = 1.5
        
        #外星人点数提高速度
        self.score_scale = 1.5
        
        #初始化随游戏进程变化的设置参数ship，bullet，ufo速度
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """initialize the setting changing as the game process"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.ufo_speed_factor = 1
        self.ufo_points = 10

        #fleet_direction为1表示向右移，-1表示向左移
        self.fleet_direction = 1

    def increase_speed(self):
        """raise the speed """
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.ufo_speed_factor *= self.speedup_scale
        self.ufo_points  = int(self.ufo_points * self.score_scale)
        print(self.ufo_points)