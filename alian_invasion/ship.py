import pygame

class Ship():

    def __init__(self, screen):
        """initialize ship's location and other settings"""
        self.screen = screen

        # load ship's figure and obtain its
        #self.image = pygame.image.load('images/ship.bmp')
        # use other bmp image
        self.image = pygame.image.load('images/ff-225_resize.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # the ship will be located in the bottom center of
        # the display
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """create ship at pointted position"""
        self.screen.blit(self.image, self.rect)

    
