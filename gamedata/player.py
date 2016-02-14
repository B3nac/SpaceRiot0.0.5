import pygame as pg
from . import bullet
from . import constants as a
import copy

class Player(pg.sprite.Sprite):
    """This class represents the Player."""
    def __init__(self, image, position, *groups):
        pg.sprite.Sprite.__init__(self, *groups)
        self.image = image
        self.rect = self.image.get_rect(topleft=position)
        self.speed = 5
        self.score = 0
        self.high_score = 0

    def shoot(self, *groups):
        """Create a bullet and add it to groups."""
        bullet.Bullet(self.rect.center, *groups)
        
    def update(self, keys, screen_rect):
        """Update the player's position and keep him on screen."""
        for key in a.DIRECT_DICT:
            if keys[key]:
                self.rect.x += a.DIRECT_DICT[key][0]*self.speed
                self.rect.y += a.DIRECT_DICT[key][1]*self.speed
        self.rect.clamp_ip(screen_rect) #Keep player on screen.


