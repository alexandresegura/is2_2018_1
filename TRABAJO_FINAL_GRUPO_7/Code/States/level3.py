import pygame as pg
from . import level1
from .. import constants as c
from .. import prepare_game, music_sound
from .. Classes import labels


class Level3(level1.Level1):

    """
    State of Credits Menu
    """

    def __init__(self):

        """
        Initializes the state
        """

        level1.Level1.__init__(self)

    def startup(self, current_time, persist):

        """
        Called when the State object is created
        """

        self.game_labels = persist
        self.persist = self.game_labels
        self.game_labels[c.CURRENT_TIME] = current_time
        self.game_labels[c.LEVEL_STATE] = c.NOT_FROZEN
        self.game_labels[c.CHAR_DEAD] = False
        self.state = c.NOT_FROZEN
        self.death_timer = 0
        self.moving_score_list = []
        self.overhead_labels_display = labels.OverheadLabels3(self.game_labels,
                                                              c.LEVEL)
        self.sound_manager = music_sound.Sound(self.overhead_labels_display)

        self.setup_background()
        self.setup_ground()
        self.setup_pipes()
        self.setup_steps()
        self.setup_bricks()
        self.setup_coin_boxes()
        self.setup_enemies()
        self.setup_char()
        self.setup_checkpoints()
        self.setup_spritegroups()

    def setup_background(self):

        """
        Sets the background image, rect and scales it to the correct
        proportions
        """

        self.background = prepare_game.GFX['level_3']
        self.back_rect = self.background.get_rect()
        self.background = pg.transform.scale(self.background,
                                             (int(self.back_rect.width *
                                                  c.BACKGROUND_MULTIPLER),
                                              int(self.back_rect.height *
                                                  c.BACKGROUND_MULTIPLER)))
        self.back_rect = self.background.get_rect()
        width = self.back_rect.width
        height = self.back_rect.height

        self.level = pg.Surface((width, height)).convert()
        self.level_rect = self.level.get_rect()
        self.viewport = prepare_game.SCREEN.get_rect(bottom=self.level_rect.bottom)
        self.viewport.x = self.game_labels[c.CAMERA_START_X]

    def end_game(self):

        """
        Ends the game
        """
        self.current_time = 0
        if self.current_time == 0:
            self.set_game_labels_values()
            self.next = c.GAME_OVER
            self.sound_manager.stop_music()
            self.done = True
