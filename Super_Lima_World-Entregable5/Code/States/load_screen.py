from .. import control
from .. import constants as c
from .. import music_sound
from ..Classes import labels


class LoadScreen(control._State):

    """
    State of loading, between states.
    """

    def __init__(self):

        """
        Initializes the state
        """

        control._State.__init__(self)

    def startup(self, current_time, persist):

        """
        Called every time the game's state becomes this one.  Initializes
        certain values
        """

        self.start_time = current_time
        self.persist = persist
        self.game_labels = self.persist
        self.next = self.set_next_state()
        info_state = self.set_overhead_label_state()
        self.overhead_labels_display = labels.OverheadLabels(self.game_labels,
                                                             info_state)
        self.sound_manager = music_sound.Sound(self.overhead_labels_display)

    def set_next_state(self):

        """
        Sets the next state
        """

        return c.LEVEL1

    def set_overhead_label_state(self):

        """
        Sets the state to send to the overhead info object
        """

        return c.LOAD_SCREEN

    def update(self, surface, keys, current_time):

        """
        Updates the Loading Screen
        """

        if (current_time - self.start_time) < 2400:
            surface.fill(c.BLACK)
            self.overhead_labels_display.update(self.game_labels)
            self.overhead_labels_display.draw(surface)

        elif (current_time - self.start_time) < 2600:
            surface.fill(c.BLACK)

        elif (current_time - self.start_time) < 2635:
            surface.fill((106, 150, 252))

        else:
            self.done = True


class GameOver(LoadScreen):

    """
    Game Over state
    """

    def __init__(self):
        super(GameOver, self).__init__()

    def set_next_state(self):

        """
        Sets next state
        """

        return c.MAIN_MENU

    def set_overhead_label_state(self):

        """
        Sets the state to send to the overhead label object
        """

        return c.GAME_OVER

    def update(self, surface, keys, current_time):
        self.current_time = current_time
        self.sound_manager.update(self.persist, None)

        if (self.current_time - self.start_time) < 7000:
            surface.fill(c.BLACK)
            self.overhead_labels_display.update(self.game_labels)
            self.overhead_labels_display.draw(surface)
        elif (self.current_time - self.start_time) < 7200:
            surface.fill(c.BLACK)
        elif (self.current_time - self.start_time) < 7235:
            surface.fill((106, 150, 252))
        else:
            self.done = True


class TimeOut(LoadScreen):

    """
    Time Out state
    """

    def __init__(self):
        super(TimeOut, self).__init__()

    def set_next_state(self):

        """
        Sets next state
        """

        if self.persist[c.LIVES] == 0:
            return c.GAME_OVER
        else:
            return c.LOAD_SCREEN

    def set_overhead_label_state(self):

        """
        Sets the state to send to the overhead label object
        """

        return c.TIME_OUT

    def update(self, surface, keys, current_time):
        self.current_time = current_time

        if (self.current_time - self.start_time) < 2400:
            surface.fill(c.BLACK)
            self.overhead_labels_display.update(self.game_labels)
            self.overhead_labels_display.draw(surface)
        else:
            self.done = True


class LoadScreen2(LoadScreen):

    """
    Game Over state
    """

    def __init__(self):
        super(LoadScreen2, self).__init__()

    def set_next_state(self):

        """
        Sets next state
        """

        return c.LEVEL2

    def set_overhead_label_state(self):

        """
        Sets the state to send to the overhead info object
        """

        return c.LOAD_SCREEN2
