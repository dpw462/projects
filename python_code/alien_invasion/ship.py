import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    ''' a class to manage a ship '''

    def __init__(self, ai_game):
        ''' initialize the ship and set starting position '''
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        #load ship image and get rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        #start each new ship at bottom-center
        self.rect.midbottom = self.screen_rect.midbottom
        #store decimal value for ship horizontal position
        self.x = float(self.rect.x)
        #movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        ''' update the ship position based on movement flag '''
        #update ship x-value, not rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        #update rect object from self.x
        self.rect.x = self.x
        
    def blitme(self):
        ''' draw ship at location '''
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        ''' center ship on screen '''
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
