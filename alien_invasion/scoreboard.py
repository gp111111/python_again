from turtle import screensize
import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard():
    """show the score informations"""

    def __init__(self,ai_settings,screen,stats):
        """iniitialize the score-reffered attributions"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        #显示字体的设置
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None,20)

        #准备初始得分图像
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """turn the score text into a rendered image"""
        score_str = "your current score: " + "{:,}".format(self.stats.score)
        self.score_image = self.font.render(score_str,True,self.text_color,
            self.ai_settings.bg_color)

        #将得分image放到右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """turn the best score text into a rendered image"""
        high_score = int(self.stats.high_score)
        high_score_str = "Best score: " + "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str,True,
        self.text_color,self.ai_settings.bg_color)

        #最高分放在屏幕中间顶部
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = 20

    def prep_level(self):
        """turn the level into a rendered image"""
        self.level_image = self.font.render(str("Level: " + 
            str(self.stats.level)),True,self.text_color,
                self.ai_settings.bg_color)

        #将等级放在比分下面
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        """show the left ships"""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings,self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.bottom = self.screen_rect.bottom
            self.ships.add(ship)

    def show_score(self):
        """show the score in the screen"""
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
        self.screen.blit(self.level_image,self.level_rect)
        #绘制飞船
        self.ships.draw(self.screen)