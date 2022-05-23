import pygame
from settings import Settings
import game_functions as gf
from star import Star
from pygame.sprite import Group
from hand import Hand
from game_stats import GameStats
def paint_stars():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
   
    
    pygame.display.set_caption('bedroom')
    hand = Hand(ai_settings,screen)
    star = Star(ai_settings,screen)
    stars = Group()
    
    gf.create_sky(ai_settings,screen,stars)
    stats = GameStats(ai_settings)
    while True:
        gf.check_events(hand)
        hand.update()
        gf.update_stars(ai_settings,stats,hand,stars,screen)
        print(stats.stars_pass)
        gf.update_screen(ai_settings,screen,stars,hand)
paint_stars()
