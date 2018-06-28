import pygame as pg
from . import prepare_game
from . import constants as c


class Sound(object):

    """
    Handles all sound for the game
    """

    def __init__(self, overhead_labels):

        """
        Initialize the class
        """

        self.sfx_dict = prepare_game.SFX
        self.music_dict = prepare_game.MUSIC
        self.overhead_labels = overhead_labels
        self.game_labels = overhead_labels.game_labels
        self.set_music_mixer()

    def set_music_mixer(self):

        """
        Sets music for each level
        """

        if self.overhead_labels.state == c.MAIN_MENU:
            pg.mixer.music.load(self.music_dict['menu_music'])
            pg.mixer.music.play()
            self.state = c.MAIN_MENU
        elif self.overhead_labels.state == c.LOAD_SCREEN:
            pg.mixer.music.stop()
            self.state = c.LOAD_SCREEN
        elif self.overhead_labels.state == c.LEVEL:
            pg.mixer.music.load(self.music_dict['main_theme'])
            pg.mixer.music.play()
            self.state = c.NORMAL
        elif self.overhead_labels.state == c.GAME_OVER:
            pg.mixer.music.load(self.music_dict['game_over'])
            pg.mixer.music.play()
            self.state = c.GAME_OVER

    def update(self, game_labels, char):

        """
        Updates sound object with game info
        """

        self.game_labels = game_labels
        self.char = char
        self.handle_state()

    def handle_state(self):

        """
        Handles the state of the sound object
        """

        if self.state == c.NORMAL:
            if self.char.dead:
                self.play_music('death', c.CHAR_DEAD)
            elif self.char.invincible \
                    and self.char.losing_invincibility is False:
                self.play_music('invincible', c.CHAR_INVINCIBLE)
            elif self.overhead_labels.time == 100:
                self.play_music('out_of_time', c.TIME_WARNING)

        elif self.state == c.STAGE_CLEAR:
            if self.char.in_castle:
                self.sfx_dict['count_down'].play()
                self.state = c.FAST_COUNT_DOWN

        elif self.state == c.FAST_COUNT_DOWN:
            if self.overhead_labels.time == 0:
                self.sfx_dict['count_down'].stop()
                self.state = c.WORLD_CLEAR

        elif self.state == c.TIME_WARNING:
            if pg.mixer.music.get_busy() == 0:
                self.play_music('main_theme_sped_up', c.SPEED_UP_NORMAL)
            elif self.char.dead:
                self.play_music('death', c.CHAR_DEAD)

        elif self.state == c.SPEED_UP_NORMAL:
            if self.char.dead:
                self.play_music('death', c.CHAR_DEAD)

        elif self.state == c.CHAR_INVINCIBLE:
            if (self.char.current_time - self.char.invincible_start_timer) > 11000:
                self.play_music('main_theme', c.NORMAL)
            elif self.char.dead:
                self.play_music('death', c.CHAR_DEAD)

        elif self.state == c.WORLD_CLEAR:
            pass
        elif self.state == c.CHAR_DEAD:
            pass
        elif self.state == c.GAME_OVER:
            pass

    def play_music(self, key, state):

        """
        Plays the music
        """

        pg.mixer.music.load(self.music_dict[key])
        pg.mixer.music.play()
        self.state = state

    def stop_music(self):

        """
        Stops the music
        """

        pg.mixer.music.stop()
