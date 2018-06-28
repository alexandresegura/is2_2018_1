import pygame as pg
import sys
from . import load_screen
from .. import prepare_game
from .. import control
from .. import constants as c
from .. import music_sound
from ..Classes import labels


class CreditsMenu(load_screen.LoadScreen):

    """
    State of Credits Menu
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
        self.setup_cursor()

    def set_next_state(self):

        """
        Sets the next state
        """

        return c.MAIN_MENU

    def set_overhead_info_state(self):

        """
        Sets the state to send to the overhead info object
        """

        return c.CREDITS_MENU

    def get_image(self, x, y, width, height, dest, sprite_sheet):

        """
        Get the image frames from the sprite sheet
        """

        image = pg.Surface([width, height])
        rect = image.get_rect()

        image.blit(sprite_sheet, (0, 0), (x, y, width, height))
        if sprite_sheet == prepare_game.GFX['game_title']:
            image.set_colorkey(c.WHITE)

        else:
            image.set_colorkey(c.BLACK)
            image = pg.transform.scale(image,
                                       (int(rect.width*3),
                                        int(rect.height*3)))

        rect = image.get_rect()
        rect.x = dest[0]
        rect.y = dest[1]
        return (image, rect)

    def setup_cursor(self):

        """
        Creates the cursor to select the main menu options
        """

        self.cursor = pg.sprite.Sprite()
        dest = (550, 500)
        self.cursor.image, self.cursor.rect = self.get_image(
            0, 0, 8, 8, dest, prepare_game.GFX['game_cursor'])
        self.cursor.state = c.START_GAME

    def update_cursor(self, keys):

        """
        Update the position of the cursor
        """

        input_list = [pg.K_RETURN]

        if self.cursor.state == c.BACK:
            self.cursor.rect.y = 550
            for input in input_list:
                if keys[input]:
                    self.main_menu()
                    self.done = True

    def main_menu(self):

        """
        Calls Credits Menu State
        """

        self.next = c.MAIN_MENU

    def update(self, surface, keys, current_time):

        """
        Updates the Credits Menu
        """

        if (current_time - self.start_time) < 8000:
            surface.blit(prepare_game.GFX['menu_bg'],(0, 0))
            self.overhead_labels.update(self.game_info)
            self.overhead_labels.draw(surface)
            self.update_cursor(keys)
            surface.blit(self.cursor.image, self.cursor.rect)

        else:
            self.done = True
