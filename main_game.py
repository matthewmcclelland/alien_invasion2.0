import pygame
from settings import Settings

# initialize the game and create a screen object
pygame.init()
image = pygame.image.load('images/images/ship.bmp')
rect

#create an object for the class settings
ai_settings = Settings()
screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))

pygame.display.set_caption('Alien Invasion')

#set the background variable
bg_color = (ai_settings.bg_color)

# draw the screen
screen.fill(bg_color)

# make the most recently drawn screen visible
pygame.display.flip()