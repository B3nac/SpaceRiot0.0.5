import pygame as pg
import copy

class Bullet(pg.sprite.Sprite):
    """This class represents the bullet."""
    def __init__(self, position, *groups):
        pg.sprite.Sprite.__init__(self, *groups)
        self.image = pg.image.load('resource/images/laser.png').convert()
        self.rect = self.image.get_rect(center=position)
        self.speed = 6

    def update(self, keys, screen_rect):
        """Move the bullet; kill if it travels off screen."""
        self.rect.y -= self.speed
        if not self.rect.colliderect(screen_rect):
            self.kill()

    def get_copy(self):
        return copy.copy(self)
