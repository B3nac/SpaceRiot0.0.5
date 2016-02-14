import random
import pygame as pg
import copy

class Galaxy(pg.sprite.Sprite):
    """This class represents the block."""
    def __init__(self, image, position, *groups):
        pg.sprite.Sprite.__init__(self, *groups)
        self.image = image
        self.rect = self.image.get_rect(topleft=position)
        self.speed = 0

    def reset_pos(self, screen_rect):
        """Reset block to a random location slightly above the screen."""
        self.rect.x = random.randrange(screen_rect.width-self.rect.width)
        self.rect.y = random.randrange(-100, -20)

    def update(self, keys, screen_rect):
        """Update the position of the block; reset if it leaves the screen."""
        self.rect.y += self.speed
        if self.rect.y > screen_rect.bottom:
            self.reset_pos(screen_rect)

    def get_copy(self):
        return copy.copy(self)
