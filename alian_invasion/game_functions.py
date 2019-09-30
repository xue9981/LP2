import sys
import pygame

def check_events():
    """response keyboard and mouse click"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(ai_settings, screen, ship):
    """update screen's figure and update to new screen"""
    screen.fill(ai_settings.bg_color)
    ship.blitme()
     
    # show you the display recently created
    pygame.display.flip()
