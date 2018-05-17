import pygame
from . import setup
from . import constants

class Sound(object):

    """Sonido del juego"""

    def __init__(self, overhead_info):

        self.sfx_dict = setup.SFX
        self.music_dict = setup.MUSIC
        self.overhead_info = overhead_info
        self.game_info = overhead_info.game_info
        self.set_music_mixer()

    def set_music_mixer(self):

        """Musica para los niveles"""

        if self.overhead_info.state == constants.LEVEL:
            pygame.mixer.music.load(self.music_dict['main_theme2'])
            pygame.mixer.music.play()
            self.state = constants.NORMAL
        elif self.overhead_info.state == constants.GAME_OVER:
            pygame.mixer.music.load(self.music_dict['game_over'])
            pygame.mixer.music.play()
            self.state = constants.GAME_OVER

    def update(self, game_info, char):

        self.game_info = game_info
        self.char = char
        self.handle_state()

    def  handle_state(self):

        """Configura el state de cada sonido"""

        if self.state == constants.NORMAL:
            if self.char.dead:
                self.play_music('death', constants.CHAR_DEAD)
            elif self.char.invincible \
                    and self.char.losing_invincibility == False:
                self.play_music('invincible', constants.CHAR_INVINCIBLE)
            elif self.char.state == constants.FLAGPOLE:
                self.play_music('flagpole', constants.FLAGPOLE)
            elif self.overhead_info.time == 100:
                self.play_music('out_of_time', constants.TIME_WARNING)

        elif self.state == constants.FLAGPOLE:
            if self.char.state == constants.WALKING_TO_CASTLE:
                self.play_music('stage_clear', constants.STAGE_CLEAR)

        elif self.state == constants.STAGE_CLEAR:
            if self.char.in_castle:
                self.sfx_dict['count_down'].play()
                self.state = constants.FAST_COUNT_DOWN

        elif self.state == constants.FAST_COUNT_DOWN:
            if self.overhead_info.time == 0:
                self.sfx_dict['count_down'].stop()
                self.state = constants.WORLD_CLEAR

        elif self.state == constants.TIME_WARNING:
            if pygame.mixer.music.get_busy() == 0:
                self.play_music('main_theme_sped_up', constants.SPED_UP_NORMAL)
            elif self.char.dead:
                self.play_music('death', constants.CHAR_DEAD)

        elif self.state == constants.SPED_UP_NORMAL:
            if self.char.dead:
                self.play_music('death', constants.CHAR_DEAD)
            elif self.char.state == constants.FLAGPOLE:
                self.play_music('flagpole', constants.FLAGPOLE)

        elif self.state == constants.CHAR_INVINCIBLE:
            if (self.char.current_time - self.char.invincible_start_timer) > 11000:
                self.play_music('main_theme2', constants.NORMAL)
            elif self.char.dead:
                self.play_music('death', constants.CHAR_DEAD)

        elif self.state == constants.WORLD_CLEAR:
            pass
        elif self.state == constants.CHAR_DEAD:
            pass
        elif self.state == constants.GAME_OVER:
            pass

    def play_music(self, key, state):

        pygame.mixer.music.load(self.music_dict[key])
        pygame.mixer.music.play()
        self.state = state

    def stop_music(self):

        pygame.mixer.music.stop()
