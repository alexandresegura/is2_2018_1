import os
import pygame as pg
from .import constants as c
from .import resources_loader


GAME_CAPTION = c.GAME_CAPTION

# Game centered in the screen
os.environ['SDL_VIDEO_CENTERED'] = '1'

pg.init()
pg.event.set_allowed([pg.KEYDOWN, pg.KEYUP, pg.QUIT])
pg.display.set_caption(c.GAME_CAPTION)
SCREEN = pg.display.set_mode(c.SCREEN_SIZE)
SCREEN_RECT = SCREEN.get_rect()

# Resource loading (Fonts and music just contain path names).
FONTS = resources_loader.load_all_fonts(os.path.join("Resources", "Fonts"))
MUSIC = resources_loader.load_all_music(os.path.join("Resources", "Music"))
SFX = resources_loader.load_all_sfx(os.path.join("Resources", "Sound"))
GFX = resources_loader.load_all_gfx(os.path.join("Resources", "Graphics"))
