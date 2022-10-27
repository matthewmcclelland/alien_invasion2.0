import sys
import pygame
from settings import Settings
from ship import Ship
import time


# initialize the game and create a screen object
pygame.init()



#create an object for the class settings
ai_settings = Settings()
screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))

pygame.display.set_caption('Alien Invasion')

#set the background variable
bg_color = (ai_settings.bg_color)

#insert ship into game
#make ship

ship = Ship(screen)
# image = pygame.image.load('images/ship.bmp')
# rect = image.get_rect()
# screen_rect = screen.get_rect()
#
# #start each new ship at the center of the screen
# rect.centerx = screen_rect.centerx
# rect.bottom = screen_rect.centery


# draw the screen
screen.fill(ai_settings.bg_color)

# draw the ship at the location
ship.blitme()
#screen.blit(image, rect)

# make the most recently drawn screen visible
pygame.display.flip()

time.sleep(5)
sys.exit()