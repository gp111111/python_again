#from turtle import screensize
import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """Manage the ship behaviors"""

    def __init__(self,ai_settings,screen):
        """Initialize the ship and the position"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        
        #获取飞船图像，并且获取外接矩形
        #这个函数返回了一个表示飞船的surface，并且将这个surface存储到self.image里
        self.image = pygame.image.load('images/ship.bmp') 
        #获取surface相应属性rect，处理矩形一样处理游戏元素
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        #将每艘新飞船放在屏幕底部中央,飞船矩形和screen的矩形
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #在飞船属性center中存储小数值
        self.center_1 = float(self.rect.centerx)
        self.center_2 = float(self.rect.centery)

        #移动的标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """adjust the center not the rect只是更改了center的值
           上下左右移动，并且在画框内"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center_1 += self.ai_settings.ship_speed_factor
        #这里不能用elif代码块，因为这样的话会使右键处于优先地位，两个if会让他不动
        if self.moving_left and self.rect.left > 0 :
            self.center_1 -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.center_2 -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center_2 += self.ai_settings.ship_speed_factor
        
        #根据center位置更新rect，更新飞船的值但是centerx还是只显示整数部，但是问题不大
        self.rect.centerx = self.center_1
        self.rect.centery = self.center_2

    def center_ship(self):
        """make the ship in the center of  the bottom"""
        self.center_1 = self.screen_rect.centerx
        self.center_2 = self.screen_rect.bottom - (self.rect.height / 2)

    def blitme(self):
        """draw the ship in the position setted"""
        #将图像绘制到屏幕上
        self.screen.blit(self.image,self.rect)