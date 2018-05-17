
"""Este modulo crea los diccionarios de recursos e inicializa el display."""

import os
import pygame
from . import means
from . import constants

ORIGINAL_CAPTION = constants.ORIGINAL_CAPTION

# Juego centrado en la pantalla
os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.init()
pygame.event.set_allowed([pygame.KEYDOWN, pygame.KEYUP, pygame.QUIT])
pygame.display.set_caption(constants.ORIGINAL_CAPTION)
SCREEN = pygame.display.set_mode(constants.SCREEN_SIZE)
SCREEN_RECT = SCREEN.get_rect()

FONTS = means.load_fonts(os.path.join("Resources", "Fonts"))
MUSIC = means.load_music(os.path.join("Resources", "Music"))
GFX = means.load_gfx(os.path.join("Resources", "Graphics"))
SFX = means.load_sfx(os.path.join("Resources", "Sound"))
