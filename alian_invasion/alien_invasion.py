import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # initialize game and create a display
    pygame.init()
    #ai_settings = Settings('skyblue')
    ai_settings = Settings('gray')
    #ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,
         ai_settings.screen_height))
    pygame.display.set_caption("Alian Invasion")

    # create an ship object
    ship = Ship(screen)

    # start game loop
    while True:
        # monitor keyboard and mouse click
        gf.check_events()

        # refill the screen in the loop
        gf.update_screen(ai_settings, screen, ship)

run_game()
