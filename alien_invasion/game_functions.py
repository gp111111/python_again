from re import S
import sys
from matplotlib.style import available
from numpy import flip
import pygame
from time import sleep
from bullet import Bullet
from scoreboard import Scoreboard
from ufo import UFO

def check_keydown_events(event,ai_settings,screen,ship,bullets):
    """response the keydown events"""
    if event.key == pygame.K_RIGHT:
        #向右移动飞船
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        #向左移动飞船
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        #向上移动飞船
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        #向下移动飞船
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
       fire_bullet(ai_settings,screen,ship,bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event,ship):
    """response the keyup events"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    if event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False

def fire_bullet(ai_settings,screen,ship,bullets):
    """if the number of bullets does not reach the allowed bullets, 
    fire a bullet"""
    if len(bullets) < ai_settings.bullets_allowed:
        #空格创建子弹，所以需要screen吧，前面只是飞船的行为，飞船是一直存在的，不用创建
        new_bullet = Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)

def check_events(ai_settings,screen,stats,sb,play_button,ship,ufos,bullets):
    """response the keyboard and the mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()#退出游戏
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings,screen,stats,sb,play_button,ship,ufos,
                bullets,mouse_x,mouse_y)

def check_play_button(ai_settings,screen,stats,sb,play_button,ship,ufos,bullets,
        mouse_x,mouse_y):
    """begin the new game when player press the 'play' button"""
    button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
    #在游戏过程中，鼠标再点击play这个位置就不起作用了not stats.game_active
    if button_clicked and not stats.game_active:

        #重置游戏设置
        ai_settings.initialize_dynamic_settings()
        #隐藏光标，防止影响游戏
        pygame.mouse.set_visible(False)
        #重置游戏信息的统计信息,只是单纯的更新了属性的值，但是显示的还是旧的，需要重新绘制
        stats.reset_stats()
        stats.game_active = True

        #绘制新的记分牌图像
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        #清空ufos列表和子弹列表
        ufos.empty()
        bullets.empty()

        #创建一群新的ufos，并且让ship居中
        create_fleet(ai_settings,screen,ship,ufos)
        ship.center_ship()

def get_number_ufos_x(ai_settings,ufo_width):
    """calculate the x limited number of ufos """
    available_space_x = ai_settings.screen_width - 2 *ufo_width
    number_ufos_x = int(available_space_x /  (2 * ufo_width))
    return number_ufos_x

def get_number_ufo_rows(ai_settings,ship_height,ufo_height):
    """calculate the y limited number of ufos"""
    available_space_y = (ai_settings.screen_height - 
                            (3 * ufo_height) - ship_height)
    number_rows = int(available_space_y / (2 * ufo_height))
    return number_rows

def create_ufo(ai_settings,screen,ufos,ufo_number,row_number):
    """create the ufo and put it into the row"""
    ufo = UFO(ai_settings,screen)
    ufo_width = ufo.rect.width
    ufo.x = ufo_width + 2 * ufo_width * ufo_number
    ufo.rect.x = ufo.x
    ufo.rect.y = ufo.rect.height + 2 * ufo.rect.height * row_number
    ufos.add(ufo)

def create_fleet(ai_settings,screen,ship,ufos):
    """create the ufo fleet"""
    #创建一个ufo
    #ufo间距就是ufo的宽度
    ufo = UFO(ai_settings,screen)
    number_ufos_x = get_number_ufos_x(ai_settings,ufo.rect.width)
    number_rows = get_number_ufo_rows(ai_settings,ship.rect.height,
        ufo.rect.height)

    #创建第一行ufo
    for row_number in range(number_rows):
        for ufo_number in range(number_ufos_x):
            create_ufo(ai_settings,screen,ufos,ufo_number,row_number)

def update_screen(ai_settings,screen,stats,sb,ship,ufos,bullets,play_button):
    """update the image of screen and change to the new screen"""
    #每次循环都重绘屏幕
    #背景色填充屏幕，接受一个实参，一种颜色
    screen.fill(ai_settings.bg_color)
    #在飞船后面重绘子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    ufos.draw(screen)
    #显示得分
    sb.show_score()

    #如果游戏处于非活动状态，就画play按钮
    if not stats.game_active:
        play_button.draw_button()

    #让最近绘制的屏幕可见
    pygame.display.flip()

def update_bullets(ai_settings,screen,stats,sb,ship,ufos,bullets):
    """update the position of bullets and delete the unseeing bullets"""
    #更新子弹位置
    bullets.update()

    #删除已经消失的子弹，防止对内存的占用导致越来越慢
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_ufo_collisions(ai_settings,screen,stats,sb,ship,ufos,bullets)

def check_bullet_ufo_collisions(ai_settings,screen,stats,sb,ship,ufos,bullets):
    """response the bullets and ufos collisions"""
    ##检查是否有子弹击中了ufo
    #若果是这样，就删除相应的子弹和ufo,True告诉Pygame删除子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets,ufos,True,True)
    #每次击中，都加分
    if collisions:
        for ufos in collisions.values():
            stats.score += ai_settings.ufo_points * len(ufos)
            sb.prep_score()
        check_high_score(stats,sb)

    if len(ufos) == 0:
        #删除现有的子弹，并且新建一群ufo
        bullets.empty()
        ai_settings.increase_speed()

        #提高等级
        stats.level += 1
        sb.prep_level()
        create_fleet(ai_settings,screen,ship,ufos)

def check_high_score(stats,sb):
    """check if the best score has become"""
    if stats.high_score < stats.score:
        stats.high_score = stats.score
        sb.prep_high_score()

def ship_hit(ai_settings,stats,sb,screen,ship,ufos,bullets):
    """response the ship hitted by the ufo"""
    if stats.ships_left > 0:
        #将ship_left减1
        stats.ships_left -= 1

        sb.prep_ships()

        #清空外星人和子弹列表
        ufos.empty()
        bullets.empty()

        #创建一群新的外星人，并将飞船放到屏幕底端中央
        create_fleet(ai_settings,screen,ship,ufos)
        ship.center_ship()

        #暂停
        sleep(0.5)
    
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_ufos_bottom(ai_settings,stats,sb,screen,ship,ufos,bullets):
    """check if any ufos reach the bottom"""
    screen_rect = screen.get_rect()
    for ufo in ufos.sprites():
        if ufo.rect.bottom >= screen_rect.bottom:
            #像飞船被撞到一样处理
            ship_hit(ai_settings,stats,sb,screen,ship,ufos,bullets)
            break

def update_ufos(ai_settings,stats,sb,screen,ship,ufos,bullets):
    """update the position of ufos"""
    check_fleet_edges(ai_settings, ufos)
    ufos.update()

    #检测ufos和飞船之间的撞船
    if pygame.sprite.spritecollideany(ship,ufos):
        ship_hit(ai_settings,stats,sb,screen,ship,ufos,bullets)

    #检测ufos是否撞到底端
    check_ufos_bottom(ai_settings,stats,sb,screen,ship,ufos,bullets)

def check_fleet_edges(ai_settings, ufos):
    """take some measures if any ufo reach the screen edge"""
    for ufo in ufos.sprites():
        if ufo.check_edge():
            change_fleet_direction(ai_settings,ufos)
            break

def change_fleet_direction(ai_settings,ufos):
    """the hole fleet moves down and change the ufos directions"""
    for ufo in ufos.sprites():
        ufo.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1