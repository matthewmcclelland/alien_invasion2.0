import pygame
import settings

# initialize the game and create a screen object
pygame.init()

screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Alien Invasion')

#set the background variable
bg_color = (0,0,255)

# draw the screen
screen.fill(bg_color)

# make the most recently drawn screen visible
pygame.display.flip()