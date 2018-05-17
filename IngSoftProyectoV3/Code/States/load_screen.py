from .. import means
from .. import constants
from .. import music_sound
from ..Classes import info

class LoadScreen(means.State):

    def __init__(self):
        means.State.__init__(self)

    def startup(self, current_time, persist):

        self.start_time = current_time
        self.persist = persist
        self.game_info = self.persist
        self.next = self.set_next_state()
        info_state = self.set_overhead_info_state()
        self.additional_info = info.AdditionalInfo(self.game_info, info_state)
        self.sound_manager = music_sound.Sound(self.additional_info)


    def set_next_state(self):

        """Configura el siguiente estado"""

        return constants.LEVEL1

    def set_overhead_info_state(self):

        """Configura el estado para que pueda ingresar el contenido de la clase info"""

        return constants.LOAD_SCREEN


    def update(self, surface, keys, current_time):

        if (current_time - self.start_time) < 2400:
            surface.fill(constants.BLACK)
            self.additional_info.update(self.game_info)
            self.additional_info.draw(surface)

        elif (current_time - self.start_time) < 2600:
            surface.fill(constants.BLACK)

        elif (current_time - self.start_time) < 2635:
            surface.fill((106, 150, 252))

        else:
            self.done = True


class GameOver(LoadScreen):

    """Pantalla de Game Over Cuando el juego termina"""

    def __init__(self):
        super(GameOver, self).__init__ ()

    def set_next_state(self):

        """Configurar el siguiente state"""

        return constants.MAIN_MENU

    def set_overhead_info_state(self):


        return constants.GAME_OVER

    def update(self, surface, keys, current_time):
        self.current_time = current_time
        self.sound_manager.update(self.persist, None)

        if (self.current_time - self.start_time) < 7000:
            surface.fill (constants.BLACK)
            self.additional_info.update (self.game_info)
            self.additional_info.draw (surface)
        elif (self.current_time - self.start_time) < 7200:
            surface.fill (constants.BLACK)
        elif (self.current_time - self.start_time) < 7235:
            surface.fill ((106, 150, 252))
        else:
            self.done = True


class TimeOut(LoadScreen):

    """Tiempo para los load screens"""

    def __init__(self):
        super(TimeOut, self).__init__()

    def set_next_state(self):

        """Configura el siguiente state"""

        if self.persist[constants.LIVES] == 0:
            return constants.GAME_OVER
        else:
            return constants.LOAD_SCREEN

    def set_overhead_info_state(self):

        """Configura el estado para que pueda ingresar el contenido de la clase info"""

        return constants.TIME_OUT

    def update(self, surface, keys, current_time):
        self.current_time = current_time

        if (self.current_time - self.start_time) < 2400:
            surface.fill(constants.BLACK)
            self.additional_info.update(self.game_info)
            self.additional_info.draw(surface)
        else:
            self.done = True
