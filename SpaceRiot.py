#Copyright © 2015 B3nac
import os
import sys
import random
import math
import pygame as pg
from gamedata import constants as a
from gameobjects import blocks
from gameobjects import enemies
from gameobjects import speedpowerup
from gamedata import player
from gamedata import bullet
from explosion import Explosion
from vector import Vector

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
        self.player = player.Player(self.get_image('resource/images/sprite.png'), (390,400), self.all_sprites)
        self.health = 10
        self.lives = 4
        self.score = 0
        self.level = 1
        self.high_score = 0
        self.shields = 0
        self.explosion.rect = self.blocks.rect.copy
        self.explosions = []
        self.explosion = Explosion(self.screen, Vector(0, 0), max_power=5, max_radius=35)

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
                if instruction_page == 2:
                    display_instructions = False
                    self.highScore()
            #Set the screen background
            screen.fill(a.BLACK)
            screen.blit(self.get_image('resource/images/menubg.png'), [0,0])
            if instruction_page == 1:

                text = self.font.render("Click to start. WASD controls and Spacebar to shoot.", True, a.WHITE)
                screen.blit(text, [70, 300])

            clock.tick(20)

            pg.display.flip()

    def highScore(self):
        """ Main program is here. """
        try:
            self.high_score_file = open("high_score.txt", "r")
            self.high_score = int(self.high_score_file.read())
            self.high_score_file.close()
            print("The high score is", self.high_score)
        except IOError:
            print("There is no high score yet.")
        except ValueError:
            print("I'm confused. Starting with no high score.")
        except ValueError:
            print("I don't understand what you typed.")
        if self.score > self.high_score:
            print("Woot! New high score!")
            try:
            #Write the file to disk
               self.high_score_file = open("high_score.txt", "w")
               self.high_score_file.write(str(self.score))
               self.high_score_file.close()
            except IOError:
            #Hm, can't write it.
               print("Too bad I couldn't save it.")
        else:
            print("Better luck next time.")

    def setup_sprites(self):
        """Create all our sprite groups."""
        self.all_sprites = pg.sprite.Group()
        self.blocks = pg.sprite.Group()
        self.spowerup = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        self.bullets = pg.sprite.Group()
        self.explosion = pg.sprite.Group()
        self.make_blocks(10)
        self.make_enemies(3)
        self.make_spowerup(1)


    def make_blocks(self, amount):
        """Create block instances, placing them in the appropriate groups."""
        for i in range(amount):
            x = random.randrange(a.SCREEN_WIDTH-self.get_image('resource/images/rock.png').get_width())
            y = random.randrange(100)
            blocks.Block(self.get_image('resource/images/rock.png'), (x,y), self.blocks, self.all_sprites)

    def make_enemies(self, amount):
        """Create enemy instances, placing them in the appropriate groups."""
        for i in range(amount):
            x = random.randrange(a.SCREEN_WIDTH-self.get_image('resource/images/enemy.png').get_width())
            y = random.randrange(50)
            enemies.Enemy(self.get_image('resource/images/enemy.png'), (x,y), self.enemies, self.all_sprites)

    def make_spowerup(self, amount):
        """Create block instances, placing them in the appropriate groups."""
        for i in range(amount):
            x = random.randrange(a.SCREEN_WIDTH-self.get_image('resource/images/s.png').get_width())
            y = random.randrange(10)
            speedpowerup.Powerup(self.get_image('resource/images/s.png'), (x,y), self.spowerup, self.all_sprites)

    def collision(self):
        collide = pg.sprite.spritecollideany(self.player,self.blocks)
        
        if collide:
            EXPLO.play()
            self.score -= 10
            self.health -= 1
            self.timer = pg.time.get_ticks()
            collide.kill()
        if self.health <= 0:
            self.lives -= 1
            self.health += 10
        if self.lives <= 0:
            self.highScore()

    def collision2(self):
        collide = pg.sprite.spritecollideany(self.player,self.enemies)
        if collide:
            EXPLO.play()
            self.score -= 40
            self.health -= 4
            self.timer = pg.time.get_ticks()
            collide.kill()
        if self.health <= 0:
            self.lives -= 1
            self.health += 10
        if self.lives <= 0:
            self.highScore()

    def collision3(self):
        collide = pg.sprite.spritecollideany(self.player, self.spowerup)
        if collide:
			#Need different sound effect here.
            self.player.speed += 10
            self.timer = pg.time.get_ticks()
            collide.kill()



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

            for self.explosion in self.explosions:
                if not self.explosion.is_alive:
                    self.explosions.remove(self.explosion)
                    continue

    def update(self):
        """Update all sprites and check collisions."""
        self.all_sprites.update(self.keys, self.screen_rect)
        self.collision()
        self.collision2()
        self.collision3()
        self.explosion.update()
        hits = pg.sprite.groupcollide(self.bullets, self.blocks, True, True)
        hits2 = pg.sprite.groupcollide(self.bullets, self.enemies, True, True)
        for hit in hits:
            self.explosion.build(20)
            self.explosions.append(self.explosion)
            EXPLO.play()
            self.score += 10
        for hit in hits2:
            EXPLO.play()
            self.score += 40
        if not self.blocks:
            self.level += 1
            self.make_blocks(self.level*10)
            self.make_enemies(self.level*3)
            self.fps += 5
        if self.lives == 0:
            main()

    def draw(self):
        """Draw all items to the screen."""
        self.screen.fill(a.WHITE)
        self.screen.blit(self.get_image('resource/images/spacebg.png'), [0,0])
        self.all_sprites.draw(self.screen)
        for self.explosion in self.explosions:
            self.explosion.display()
        text = self.font.render("Score: {}".format(self.score), True, a.WHITE)
        self.screen.blit(text, (10,5))
        text = self.font.render("Health: {}".format(self.health), True, a.WHITE)
        self.screen.blit(text, (10,35))
        text = self.font.render("Lives: {}".format(self.lives), True, a.WHITE)
        self.screen.blit(text, (10,65))
        text = self.font.render("Highscore: {}".format(self.high_score), True, a.WHITE)
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
    app.startScreen()
    app.main_loop()
    pg.quit()
    sys.exit()

if __name__ == "__main__":
    main()
