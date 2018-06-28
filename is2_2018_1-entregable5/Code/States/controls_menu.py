import pygame as pg
import sys
from . import load_screen
from .. import prepare_game
from .. import control
from .. import constants as c
from .. import music_sound
from ..Classes import labels


class ControlsMenu(load_screen.LoadScreen):

    """
    State of Controls Menu
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

        return c.MAIN_MENU

    def set_overhead_info_state(self):

        """
        Sets the state to send to the overhead info object
        """

        return c.CONTROLS_MENU

    def update(self, surface, keys, current_time):

        """
        Updates the Controls Menu
        """

        if (current_time - self.start_time) < 3000:
            surface.blit(prepare_game.GFX['controles'],(0, 0))
            self.overhead_labels.update(self.game_info)
            self.overhead_labels.draw(surface)
        else:
            self.done = True
