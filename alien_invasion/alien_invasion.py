import pygame
#这个Group类类似列表
from pygame.sprite import Group
from scoreboard import Scoreboard
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
import game_functions as gf

def run_game():
    """initialize the game and create a screen object"""
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_width))
    pygame.display.set_caption("Alien Invasion")#标题

    #创建button按钮
    play_button = Button(ai_settings,screen,"Play")
    
    #创建一艘飞船对象
    ship = Ship(ai_settings,screen)
    #创建一组子弹对象，如果再while内的话，会创造上千个子弹编组，游戏会变慢
    bullets = Group()
    #创建一ufo编组，创建外星人群，fleet：舰队，车队
    ufos = Group()
    gf.create_fleet(ai_settings,screen,ship,ufos)

    #创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)
    #创建记分牌实例
    sb = Scoreboard(ai_settings,screen,stats)

    #begin the game loop
    while True:

        #monitor the keyboard and the mouse events
        gf.check_events(ai_settings,screen,stats,sb,play_button,ship,ufos,
            bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings,screen,stats,sb,ship,ufos,bullets)
            gf.update_ufos(ai_settings,stats,sb,screen,ship,ufos,bullets)
            
        #repaint the screen every loop
        gf.update_screen(ai_settings,screen,stats,sb,ship,ufos,bullets,
            play_button)

run_game()