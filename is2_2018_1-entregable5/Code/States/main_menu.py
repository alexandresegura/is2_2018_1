import pygame as pg
import sys
from .. import control, music_sound
from .. import constants as c
from .. import prepare_game
from .. Classes import labels


class Menu(control._State):

    """
    Initial state of the game.
    """

    def __init__(self):

        """
        Initializes the state
        """

        control._State.__init__(self)
        persist = {c.COIN_TOTAL: 0,
                   c.SCORE: 0,
                   c.LIVES: 3,
                   c.TOP_SCORE: 0,
                   c.CURRENT_TIME: 0.0,
                   c.LEVEL_STATE: None,
                   c.CAMERA_START_X: 0,
                   c.CHAR_DEAD: False}
        self.startup(0.0, persist)

    def startup(self, current_time, persist):

        """
        Called every time the game's state becomes this one.  Initializes
        certain values
        """

        self.next = c.LOAD_SCREEN
        self.persist = persist
        self.game_labels = persist
        self.overhead_labels_display = labels.OverheadLabels(self.game_labels,
                                                     c.MAIN_MENU)
        self.sprite_sheet = prepare_game.GFX['game_title']
        self.sound_manager = music_sound.Sound(self.overhead_labels_display)
        self.setup_background()
        self.setup_cursor()

    def setup_cursor(self):

        """
        Creates the cursor to select the main menu options
        """

        self.cursor = pg.sprite.Sprite()
        dest = (270, 470)
        self.cursor.image, self.cursor.rect = self.get_image(
            0, 0, 8, 8, dest, prepare_game.GFX['game_cursor'])
        self.cursor.state = c.START_GAME

    def setup_background(self):

        """
        Setup the background main menu image to blit
        """

        self.background = prepare_game.GFX['menu_bg']
        self.background_rect = self.background.get_rect()
        self.viewport = prepare_game.SCREEN.get_rect(
                                        bottom=prepare_game.SCREEN_RECT.bottom)

        self.image_dict = {}
        self.image_dict['GAME_TITLE'] = self.get_image(
            0, 0, 500, 171, (170, 100), prepare_game.GFX['game_title'])

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

    def update(self, surface, keys, current_time):

        """
        Updates the state every time the screen refreshes
        """

        self.current_time = current_time
        self.game_labels[c.CURRENT_TIME] = self.current_time
        self.update_cursor(keys)
        self.overhead_labels_display.update(self.game_labels)

        surface.blit(self.background, self.viewport, self.viewport)
        surface.blit(self.image_dict['GAME_TITLE'][0],
                     self.image_dict['GAME_TITLE'][1])
        surface.blit(self.cursor.image, self.cursor.rect)
        self.overhead_labels_display.draw(surface)

    def update_cursor(self, keys):

        """
        Update the position of the cursor
        """

        clock = pg.time.Clock ()
        input_list = [pg.K_RETURN]

        if self.cursor.state == c.START_GAME:
            self.cursor.rect.y = 340
            if keys[pg.K_DOWN]:
                self.cursor.state = c.CONTROLS
            for input in input_list:
                if keys[input]:
                    self.box_input()
                    self.done = True
        elif self.cursor.state == c.CONTROLS:
            self.cursor.rect.y = 385
            if keys[pg.K_UP]:
                self.cursor.state = c.START_GAME
            elif keys[pg.K_DOWN]:
                self.cursor.state = c.CREDITS
            for input in input_list:
                if keys[input]:
                    self.menu_controls()
                    self.done = True
        elif self.cursor.state == c.CREDITS:
            self.cursor.rect.y = 430
            if keys[pg.K_UP]:
                self.cursor.state = c.CONTROLS
            elif keys[pg.K_DOWN]:
                self.cursor.state = c.QUIT_GAME
            for input in input_list:
                if keys[input]:
                    self.menu_credits()
                    self.done = True
        elif self.cursor.state == c.QUIT_GAME:
            self.cursor.rect.y = 475
            for input in input_list:
                if keys[input]:
                    self.reset_game_labels ()
                    self.done = True
                    pg.quit ()
                    sys.exit ()
            if keys[pg.K_UP]:
                self.cursor.state = c.CREDITS

        clock.tick(40)

    def menu_controls(self):

        """
        Calls Control Menu State
        """

        self.next = c.CONTROLS_MENU
        self.background = prepare_game.GFX['controles']

    def menu_credits(self):

        """
        Calls Credits Menu State
        """

        self.next = c.CREDITS_MENU
        self.background = prepare_game.GFX['menu_bg']

    def box_input(self):

        """
        Calls Input Box State
        """

        self.next = c.INPUT_BOX
        self.background = prepare_game.GFX['menu_bg']

    def reset_game_labels(self):

        """
        Resets the game labels in case of a Game Over or a restart
        """

        self.game_labels[c.COIN_TOTAL] = 0
        self.game_labels[c.SCORE] = 0
        self.game_labels[c.LIVES] = 3
        self.game_labels[c.CURRENT_TIME] = 0.0
        self.game_labels[c.LEVEL_STATE] = None
        self.persist = self.game_labels
