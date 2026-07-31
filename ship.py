import pygame

class Ship:
    """A class that creates the ship. Player"""

    def __init__(self, game):
        """Initialize the ship and set its starting position"""
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        # Load the ship image
        self.image = pygame.image.load('Assets/ship.bmp')
        self.rect = self.image.get_rect()

        # Start the ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Movement flag; start with a ship that is not moving
        self.moving_right = False

    def update(self):
        """Update the ship position based on the movement flag"""
        if self.moving_right:
            self.rect += 3


    def blitme(self):
        """A draw function at its current location"""
        self.screen.blit(self.image, self.rect)
