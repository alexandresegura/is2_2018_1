from . import setup, means
from . import constants
from .States import main_menu, load_screen, level1, level2, level3

def main():

    """Agregar los estados para poder gestionarlos"""

    run_game = means.Manage(setup.ORIGINAL_CAPTION)
    state_dict = {constants.MAIN_MENU: main_menu.Menu(),
                  constants.LOAD_SCREEN: load_screen.LoadScreen(),
                  constants.TIME_OUT: load_screen.TimeOut(),
                  constants.GAME_OVER: load_screen.GameOver(),
                  constants.LEVEL1: level1.Level1(),
                  constants.LEVEL2: level2.Level2(),
                  constants.LEVEL3: level3.Level3()}


    run_game.setup_state(state_dict, constants.MAIN_MENU)
    run_game.main()
