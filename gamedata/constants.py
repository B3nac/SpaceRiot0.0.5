import pygame as pg

BLACK    = (  0,   0,   0)
WHITE    = (255, 255, 255)
RED      = (255,   0,   0)
BLUE     = (  0,   0, 255)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500

DIRECT_DICT = {pg.K_a  : (-1, 0),
               pg.K_d : ( 1, 0),
               pg.K_w    : ( 0,-1),
               pg.K_s  : ( 0, 1)}

