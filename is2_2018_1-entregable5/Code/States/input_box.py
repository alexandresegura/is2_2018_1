import pygame as pg
import sys
from pygame.locals import *
from . import load_screen
from .. import prepare_game
from .. import control
from .. import constants as c
from .. import music_sound
from ..Classes import labels


class InputBox(load_screen.LoadScreen):
    
    """
    State of Input Box
    """

    def __init__(self):

        """
        Initializes the state
        """

        load_screen.LoadScreen.__init__(self)

    def startup(self, current_time, persist):

        """
        Called every time the game's state becomes this one.  Initializes
        certain values
        """

        self.start_time = current_time
        self.persist = persist
        self.game_info = self.persist
        self.next = self.set_next_state()
        info_state = self.set_overhead_info_state()
        self.overhead_labels = labels.OverheadLabels(self.game_info, info_state)
        self.sound_manager = music_sound.Sound(self.overhead_labels)

    def set_next_state(self):

        """
        Sets the next state
        """

        return c.LOAD_SCREEN

    def set_overhead_info_state(self):

        """
        Sets the state to send to the overhead info object
        """

        return c.INPUT_BOX

    def update(self, surface, keys, current_time):

        """
        Updates the Input Box
        """
        NOMBRE=""
        name = ""
        font = pg.font.Font(None, 50)
        done = False
        while not done:
            for evt in pg.event.get():
                if evt.type == KEYDOWN:
                    if evt.unicode.isalpha():
                        name += evt.unicode
                    elif evt.key == K_BACKSPACE:
                        name = name[:-1]
                    elif evt.key == K_RETURN:
                        done = True
                        NOMBRE=name
                        break
                elif evt.type == QUIT:
                    return

            surface.fill(c.BLACK)
            self.overhead_labels.update(self.game_info)
            self.overhead_labels.draw(surface)
            block = font.render(name, True, c.WHITE)
            rect = block.get_rect()
            rect.center = surface.get_rect().center
            surface.blit(block, rect)
            pg.display.flip()
            self.done = True
        print(NOMBRE)
