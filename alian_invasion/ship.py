import pygame

class Ship():

    def __init__(self, ai_settings, screen):
        """initialize ship's location and other settings"""
        self.screen = screen
        self.ai_settings = ai_settings
        
        # load ship's figure and obtain its
        #self.image = pygame.image.load('images/ship.bmp')
        # use other bmp image
        self.image = pygame.image.load('images/ff-225_resize.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # the ship will be located in the bottom center of
        # the display
        self.rect.bottom = self.screen_rect.bottom
        self.rect.centerx = self.screen_rect.centerx

        # put float number in the ship's center attribute
        self.center = float(self.rect.centerx)

        # move marker
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """create ship at pointted position"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """moving marker to change ship's position"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        elif self.moving_left and self.rect.left > self.screen_rect.left:
            self.center -= self.ai_settings.ship_speed_factor

        # renew rect object based on center
        self.rect.centerx = self.center


            

