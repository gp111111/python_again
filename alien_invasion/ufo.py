import pygame
from pygame.sprite import Sprite

class UFO(Sprite):
    """represent the single ufo"""

    def __init__(self,ai_settings,screen):
        """initialize the ufo and the starting position"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #加载ufo图像
        self.image = pygame.image.load('images/ufo.bmp')
        self.rect = self.image.get_rect()

        #ufo初始位置最初都在屏幕左上角附近,左边距是一个ufo的宽，上边距是一个ufo的高
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #存储ufo准确位置
        self.x = float(self.rect.x)

    def update(self):
        """move the ufo to right"""
        self.x += (self.ai_settings.ufo_speed_factor * 
                        self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def check_edge(self):
        """If the ufo position is beside the edge, return the True."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def blitme(self):
        """draw the ufo in the setted position"""
        self.screen.blit(self.image,self.rect)