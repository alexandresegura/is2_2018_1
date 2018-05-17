import pygame
from .. import setup, means
from .. import constants
from .. Classes import info

class Menu(means.State):
    def __init__(self):

        """Inicializa el State"""

        means.State.__init__(self)
        persist = {constants.COIN_TOTAL: 0,
                   constants.SCORE: 0,
                   constants.LIVES: 3,
                   constants.TOP_SCORE: 0,
                   constants.CURRENT_TIME: 0.0,
                   constants.LEVEL_STATE: None,
                   constants.CAMERA_START_X: 0,
                   constants.CHAR_DEAD: False}
        self.startup(0.0, persist)

    def startup(self, current_time, persist):

        """Inicializa algunos states del juego"""

        self.next = constants.LOAD_SCREEN
        self.persist = persist
        self.game_info = persist
        self.overhead_info = info.AdditionalInfo(self.game_info, constants.MAIN_MENU)

        self.sprite_sheet = setup.GFX['waa']
        self.setup_background()
        self.setup_cursor()


    def setup_cursor(self):

        """Cursor para seleccionar player1 o Controls"""

        self.cursor = pygame.sprite.Sprite()
        dest = (220, 358)
        self.cursor.image, self.cursor.rect = self.get_image(
            24, 160, 8, 8, dest, setup.GFX['item_objects'])
        self.cursor.state = constants.PLAYER1


    def setup_background(self):

        """Configura la imagen de fondo"""

        self.background = setup.GFX['aw']
        self.background_rect = self.background.get_rect()

        self.viewport = setup.SCREEN.get_rect(bottom=setup.SCREEN_RECT.bottom)

        self.image_dict = {}
        self.image_dict['GAME_NAME_BOX'] = self.get_image(
            1, 60, 176, 88, (170, 100), setup.GFX['waa'])



    def get_image(self, x, y, width, height, dest, sprite_sheet):

        image = pygame.Surface([width, height])
        rect = image.get_rect()

        image.blit(sprite_sheet, (0, 0), (x, y, width, height))
        if sprite_sheet == setup.GFX['waa']:
            image.set_colorkey((255, 0, 220))
            image = pygame.transform.scale(image,
                                   (int(rect.width*constants.SIZE_MULTIPLIER),
                                    int(rect.height*constants.SIZE_MULTIPLIER)))
        else:
            image.set_colorkey(constants.BLACK)
            image = pygame.transform.scale(image,
                                   (int(rect.width*3),
                                    int(rect.height*3)))

        rect = image.get_rect()
        rect.x = dest[0]
        rect.y = dest[1]
        return (image, rect)


    def update(self, surface, keys, current_time):

        self.current_time = current_time
        self.game_info[constants.CURRENT_TIME] = self.current_time
        self.update_cursor(keys)
        self.overhead_info.update(self.game_info)

        surface.blit(self.background, self.viewport, self.viewport)
        surface.blit(self.image_dict['GAME_NAME_BOX'][0],
                     self.image_dict['GAME_NAME_BOX'][1])
        surface.blit(self.cursor.image, self.cursor.rect)
        self.overhead_info.draw(surface)


    def update_cursor(self, keys):

        input_list = [pygame.K_RETURN, pygame.K_a, pygame.K_s]

        if self.cursor.state == constants.PLAYER1:
            self.cursor.rect.y = 358
            if keys[pygame.K_DOWN]:
                self.cursor.state = constants.CONTROLS
            for input in input_list:
                if keys[input]:
                    self.reset_game_info()
                    self.done = True
        elif self.cursor.state == constants.CONTROLS:
            self.cursor.rect.y = 403
            if keys[pygame.K_UP]:
                self.cursor.state = constants.PLAYER1


    def reset_game_info(self):

        """Resetea la info del juego luego de que este termine o sea reiniciado"""

        self.game_info[constants.COIN_TOTAL] = 0
        self.game_info[constants.SCORE] = 0
        self.game_info[constants.LIVES] = 3
        self.game_info[constants.CURRENT_TIME] = 0.0
        self.game_info[constants.LEVEL_STATE] = None

        self.persist = self.game_info
