from . import prepare_game, control
from .States import main_menu, load_screen, level1, credits_menu, controls_menu
from . import constants as c


def main():

    """
    Add all the states needed in the game.
    """

    run_it = control.Control(prepare_game.GAME_CAPTION)
    state_dict = {c.MAIN_MENU: main_menu.Menu(),
                  c.LOAD_SCREEN: load_screen.LoadScreen(),
                  c.CONTROLS_MENU: controls_menu.ControlsMenu(),
                  c.CREDITS_MENU: credits_menu.CreditsMenu(),
                  c.TIME_OUT: load_screen.TimeOut(),
                  c.GAME_OVER: load_screen.GameOver(),
                  c.LEVEL1: level1.Level1()}

    run_it.setup_states(state_dict, c.MAIN_MENU)
    run_it.main()
