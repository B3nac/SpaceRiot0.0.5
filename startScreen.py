# -*- coding: cp1252 -*-
#Copyright © 2015 B3nac
import os
import sys
import random
import math
import pygame as pg
import galaxyMap
import topscore
from gamedata import player
from gamedata import constants as a
from gamedata import bullet

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
        self.health = 10
        self.lives = 4
        self.scene = 0

    def get_image(self, _path):
        image = self._image_library.get(_path) 
        if image == None:
            butt_path = _path.replace('/', os.sep).replace('\\', os.sep)
            image = pg.image.load(butt_path).convert_alpha()
            self._image_library[butt_path] = image
        return image
		#Not finished

    def startScreen(self):
        size = [800,500]
        screen = pg.display.set_mode(size)
        #Loop until the user clicks the close button.
        done=False
        clock=pg.time.Clock()
        display_instructions = True
        instruction_page = 1

        # -------- Instruction Page Loop -----------
        while done==False and display_instructions:
            for event in pg.event.get(): #User did something
                if event.type == pg.QUIT: #If user clicked close
                    done=True # Flag that we are done so we exit this loop
                    exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    instruction_page += 1
                    galaxyMap.main()
                if instruction_page == 2:
                    display_instructions = False
                    
                    
            #Set the screen background
            screen.fill(a.BLACK)
            screen.blit(self.get_image('resource/images/menubg.png'), [0,0])
            if instruction_page == 1:

                text = self.font.render("Click to start. WASD controls and Spacebar to shoot.", True, a.WHITE)
                screen.blit(text, [70, 300])
                
            clock.tick(20)

            pg.display.flip()  

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
    app.startScreen()
    pg.quit()
    sys.exit()

if __name__ == "__main__":
    main()
