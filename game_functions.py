import sys
import pygame
from star import Star
from random import randint
def check_events(hand):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,hand)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,hand)
def check_keydown_events(event,hand):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        hand.moving_right = True
    elif event.key == pygame.K_LEFT:
        hand.moving_left = True
    elif event.key == pygame.K_UP:
        hand.moving_up = True
    elif event.key == pygame.K_DOWN:
        hand.moving_down = True

    elif event.key == pygame.K_q:
        sys.exit()     
def check_keyup_events(event,hand):
    """响应松开"""
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            hand.moving_right = False
        elif event.key == pygame.K_LEFT:
            hand.moving_left = False
        elif event.key == pygame.K_UP:
            hand.moving_up = False
        elif event.key == pygame.K_DOWN:
            hand.moving_down = False
def update_screen(ai_settings,screen,stars,hand):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)  
    stars.draw(screen)   
    # 让最新绘制的屏幕可见
    hand.blitme() 
    pygame.display.flip()
def get_number_x(ai_settings,star_width):
    """计算每行可容纳多少个星星"""
    availabe_space_x = ai_settings.screen_width - 2 * star_width
    number_star_x = int(availabe_space_x/(1*star_width))
    return number_star_x
def get_number_rows(ai_settings,star_height):
    """计算行数"""
    availabe_space_y = (ai_settings.screen_height - 1*star_height)
    number_rows = int(availabe_space_y/(1*star_height))
    return number_rows
def create_star(ai_settings,screen,star_number,stars,row_number):
    """创建星星"""
    star = Star(ai_settings,screen)
    star_width = star.rect.width
    star.x = star_width + 1 * star_width* star_number
    star.rect.x = star.x
    star.rect.y = star.rect.height + 1 * star.rect.height * row_number
    stars.add(star)
def create_sky(ai_settings,screen,stars):
    """创建天空"""
    star = Star(ai_settings,screen)
    for x in range(15):
            create_star(ai_settings,screen,randint(1,get_number_x(ai_settings,star.rect.width)),stars,randint(1,get_number_rows(ai_settings,star.rect.height)))
    stars.add(star)
 

def update_stars(ai_settings,stats,hand,stars,screen):
    screen_rect = screen.get_rect()
    
    for star in stars.sprites():
        if  pygame.sprite.spritecollideany(hand,stars):
            stars.remove(star)        
        elif star.rect.bottom == screen_rect.bottom:
            stats.stars_pass +=1
            stars.remove(star) 
        else:
            star.rect.y += ai_settings.star_drop_speed
    
    
   

    

def check_star_hand_collision(stars,hand):
    collision = pygame.sprite.groupcollide(stars,hand,True,True)       
    
    
def drop_stars(ai_settings,screen,stars):
    """如果没有达到限制，就发射一颗子弹"""
    # 创建新子弹，并将其加入到编组bullets中
    if len(stars)< ai_settings.stars_allowed:
        new_star = Star(ai_settings,screen)
        stars.add(new_star)

       





