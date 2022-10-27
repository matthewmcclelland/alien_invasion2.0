import pygame
from settings import Settings
from ship import Ship
import time
import sys

class AlienInvasion():

    def __init__(self):

        # initialize the game and create a screen object
        pygame.init()



        #create an object for the class settings
        self.ai_settings = Settings()
        self.screen = pygame.display.set_mode((self.ai_settings.screen_width, self.ai_settings.screen_height))

        pygame.display.set_caption('Alien Invasion')

        #set the background variable
        bg_color = (self.ai_settings.bg_color)

        #insert ship into game
        #make ship

        self.ship = Ship(self.screen)

    def run_game(self):
        while True:

            # draw the screen
            self.screen.fill(self.ai_settings.bg_color)

            # draw the ship at the location
            self.ship.blitme()
            #screen.blit(image, rect)

            # make the most recently drawn screen visible
            pygame.display.flip()

            time.sleep(5)
            sys.exit()

if __name__ == '__main__':
  # Make a game instance, and run the game.
  ai = AlienInvasion()
  ai.run_game()