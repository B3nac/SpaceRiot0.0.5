5# -*- coding: cp1252 -*-
#Copyright © 2015 B3nac
import os
import sys
import random
import math
import pygame as pg
from gamedata import constants as a
from gameobjects import galaxywh
from gamedata import player
from gamedata import bullet
import SpaceRiot

class Control(object):
    """Class that manages primary conrol flow for the whole program."""
    def __init__(self):
        pg.mixer.music.play(10)
        self.screen = pg.display.get_surface()
        self.screen_rect = self.screen.get_rect()
        self.clock = pg.time.Clock()
        self.fps = 20.0
        self.keys = pg.key.get_pressed()
        self.done = False
        self.font = pg.font.Font("resource/fonts/freesansbold.ttf", 24)
        self._image_library = {}
        self.setup_sprites()
        self.player = player.Player(self.get_image('resource/images/sprite.png'), (390,400), self.player_sprite)
        self.health = 10
        self.lives = 4
        self.level = 1
        self.scene = 0

    def get_image(self, _path):
        image = self._image_library.get(_path) 
        if image == None:
            butt_path = _path.replace('/', os.sep).replace('\\', os.sep)
            image = pg.image.load(butt_path).convert_alpha()
            self._image_library[butt_path] = image
        return image
		#Not finished
        
    def highScore(self):
        """ Main program is here. """
        try:
            self.high_score_file = open("high_score.txt", "r")
            self.player.high_score = int(self.high_score_file.read())
            self.high_score_file.close()
            print("The high score is", self.player.high_score)
        except IOError:
            print("There is no high score yet.")
        except ValueError:
            print("I'm confused. Starting with no high score.")
        except ValueError:
            print("I don't understand what you typed.")
        if self.player.score > self.player.high_score:
            print("Woot! New high score!")
            try:
            #Write the file to disk
               self.high_score_file = open("high_score.txt", "w")
               self.high_score_file.write(str(self.player.score))
               self.high_score_file.close()
            except IOError:
                #Hm, can't write it.
                print("Too bad I couldn't save it.")
            else:
                print("Better luck next time.")

    def setup_sprites(self):
        """Create all our sprite groups."""
        self.player_sprite = pg.sprite.Group()
        self.all_sprites = pg.sprite.Group()
        self.bullets = pg.sprite.Group()
        self.galaxywh = pg.sprite.Group()
        self.make_galaxywh(1)
      
    def make_galaxywh(self, amount):
        for i in range(amount):
            x = random.randrange(a.SCREEN_WIDTH-self.get_image('resource/images/galaxywh.png').get_width())
            y = random.randrange(100)
            galaxywh.Galaxy(self.get_image('resource/images/galaxywh.png'), (100,100), self.galaxywh)

    def galaxy(self):
        collide = pg.sprite.spritecollideany(self.player, self.galaxywh)
        if collide:
            collide.kill()
            self.scene = 2

    def event_loop(self):
        """Event loop for program; there can be only one."""
        for event in pg.event.get():
            if event.type == pg.QUIT or self.keys[pg.K_ESCAPE]:
                self.done = True
            if event.type == pg.KEYDOWN and event.key == pg.K_f:
                pg.display.toggle_fullscreen()
            elif event.type in (pg.KEYDOWN, pg.KEYUP):
                self.keys = pg.key.get_pressed()
            if self.keys[pg.K_SPACE]:
                self.player.shoot(self.bullets, self.all_sprites)
                LASER.play()

    def update(self):
        """Update all sprites and check collisions."""
        self.player_sprite.update(self.keys, self.screen_rect)
        self.all_sprites.update(self.keys, self.screen_rect)
        self.galaxy()
        if self.scene == 2:
            SpaceRiot.main()
        if self.lives == 0:
            main()

    def draw(self):
        """Draw all items to the screen."""
        self.screen.fill(a.WHITE)
        self.screen.blit(self.get_image('resource/images/spacebg.png'), [0,0])
        self.player_sprite.draw(self.screen)
        self.all_sprites.draw(self.screen)
        self.galaxywh.draw(self.screen)
        #for self.explosion in self.explosions:
            #self.explosion.display()
        text = self.font.render("Score: {}".format(self.player.score), True, a.WHITE)
        self.screen.blit(text, (10,5))
        text = self.font.render("Health: {}".format(self.health), True, a.WHITE)
        self.screen.blit(text, (10,35))
        text = self.font.render("Lives: {}".format(self.lives), True, a.WHITE)
        self.screen.blit(text, (10,65))
        text = self.font.render("Highscore: {}".format(self.player.high_score), True, a.WHITE)
        self.screen.blit(text, (550,5))
        
    def main_loop(self):

        while not self.done:
            self.event_loop()
            self.update()
            self.draw()
            pg.display.update()
            self.clock.tick(self.fps)

def main():

    global LASER, EXPLO
    pg.init()
    pg.mixer.pre_init(44100, -16, 2, 128)
    pg.display.set_mode((a.SCREEN_WIDTH, a.SCREEN_HEIGHT))
    pg.display.set_caption("SpaceRiot v0.0.5")
    #Convert all image_loads to use cache function.
    pg.mixer.music.load('resource/sounds/Its like Im walking on air.ogg')
    LASER = pg.mixer.Sound('resource/sounds/laser.ogg')
    EXPLO = pg.mixer.Sound('resource/sounds/explosion.ogg')
    app = Control()
    app.main_loop()
    pg.quit()
    sys.exit()

if __name__ == "__main__":
    main()
