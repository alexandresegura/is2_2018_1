import pygame
from .. import setup
from .. import constants
from . import flashing_money

class Character(pygame.sprite.Sprite):

    def __init__(self, image):
        super(Character, self).__init__()
        self.image = image
        self.rect = self.image.get_rect()

class AdditionalInfo:

    """Clase para brindar información del dinero, tiempo transcurrido y puntaje"""

    def __init__(self, game_info, state):
        self.sprite_sheet = setup.GFX['text_images']
        self.coin_total = game_info[constants.COIN_TOTAL]
        self.time = 401
        self.current_time = 0
        self.total_lives = game_info[constants.LIVES]
        self.top_score = game_info[constants.TOP_SCORE]
        self.state = state
        self.special_state = None
        self.game_info = game_info
        self.create_image_dict()
        self.create_score_group()
        self.create_info_labels()
        self.create_load_screen_labels()
        self.create_countdown_clock()
        self.create_money_counter()
        self.create_flashing_money()
        self.create_game_image()
        self.create_game_over_label()
        self.create_time_out_label()
        self.create_main_menu_labels()

    def create_image_dict(self):
        character_string = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ -*'

        self.image_dict = {}
        image_list = []

        image_list.append(self.get_image (3, 230, 7, 7))
        image_list.append(self.get_image (12, 230, 7, 7))
        image_list.append(self.get_image (19, 230, 7, 7))
        image_list.append(self.get_image (27, 230, 7, 7))
        image_list.append(self.get_image (35, 230, 7, 7))
        image_list.append(self.get_image (43, 230, 7, 7))
        image_list.append(self.get_image (51, 230, 7, 7))
        image_list.append(self.get_image (59, 230, 7, 7))
        image_list.append(self.get_image (67, 230, 7, 7))
        image_list.append(self.get_image (75, 230, 7, 7))
        image_list.append(self.get_image (83, 230, 7, 7))
        image_list.append(self.get_image (91, 230, 7, 7))
        image_list.append(self.get_image (99, 230, 7, 7))
        image_list.append(self.get_image (107, 230, 7, 7))
        image_list.append(self.get_image (115, 230, 7, 7))
        image_list.append(self.get_image (123, 230, 7, 7))
        image_list.append(self.get_image (3, 238, 7, 7))
        image_list.append(self.get_image (11, 238, 7, 7))
        image_list.append(self.get_image (20, 238, 7, 7))
        image_list.append(self.get_image (27, 238, 7, 7))
        image_list.append(self.get_image (35, 238, 7, 7))
        image_list.append(self.get_image (44, 238, 7, 7))
        image_list.append(self.get_image (51, 238, 7, 7))
        image_list.append(self.get_image (59, 238, 7, 7))
        image_list.append(self.get_image (67, 238, 7, 7))
        image_list.append(self.get_image (75, 238, 7, 7))
        image_list.append(self.get_image (83, 238, 7, 7))
        image_list.append(self.get_image (91, 238, 7, 7))
        image_list.append(self.get_image (99, 238, 7, 7))
        image_list.append(self.get_image (108, 238, 7, 7))
        image_list.append(self.get_image (115, 238, 7, 7))
        image_list.append(self.get_image (123, 238, 7, 7))
        image_list.append(self.get_image (3, 246, 7, 7))
        image_list.append(self.get_image (11, 246, 7, 7))
        image_list.append(self.get_image (20, 246, 7, 7))
        image_list.append(self.get_image (27, 246, 7, 7))
        image_list.append(self.get_image (48, 248, 7, 7))
        image_list.append(self.get_image (68, 249, 6, 2))
        image_list.append(self.get_image (75, 247, 6, 6))

        for character, image in zip(character_string, image_list):
            self.image_dict[character] = image

    def get_image(self, x, y, width, height):

        """Funcion para separar y sacar las imagenes necesarias
        del archivo de sprites"""

        image = pygame.Surface([width, height])
        rect = image.get_rect()
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey((92, 148, 252))
        image = pygame.transform.scale(image,
                                    (int(rect.width * 2.9),
                                     int(rect.height * 2.9)))
        return image

    def create_score_group(self):

        """Crea el score inicial (0000000)"""

        self.score_images = []
        self.create_label(self.score_images, '0000000', 75, 55)

    def create_info_labels(self):

        """Crea los labels para el juego"""

        self.game_label = []
        self.world_label = []
        self.time_label = []
        self.stage_label = []
        self.create_label(self.game_label, 'CARLOBROS', 55, 30) # Tiene que poder modificarse
        self.create_label(self.world_label, 'LEVEL', 450, 30)
        self.create_label(self.time_label, 'TIME', 645, 30)
        self.create_label(self.stage_label, '1', 492, 55) # Tiene que cambiar de acuerdo a los niveles
        self.label_list = [self.game_label,
                           self.world_label,
                           self.time_label,
                           self.stage_label]

    def create_load_screen_labels(self):

        """Labels para el load screen del juego """

        world_label = []
        number_label = []

        self.create_label(world_label, 'LEVEL', 280, 200)
        self.create_label(number_label, '1', 430, 200)
        self.center_labels = [world_label, number_label]

    def create_countdown_clock(self):

        """Countdown para los niveles"""

        self.count_down_images = []
        self.create_label(self.count_down_images, str(self.time), 645, 55)

    def create_label(self, label_list, string, x, y):

        """Label de (WORLD, TIME, SUPER LIMA)"""

        for letter in string:
            label_list.append(Character(self.image_dict[letter]))

        self.set_label_rects (label_list, x, y)

    def set_label_rects(self, label_list, x, y):

        """Posición  de los characters"""

        for i, letter in enumerate (label_list):
            letter.rect.x = x + ((letter.rect.width + 3) * i)
            letter.rect.y = y
            if letter.image == self.image_dict['-']:
                letter.rect.y += 7
                letter.rect.x += 2

    def create_money_counter(self):

        """Info para contar la cantidad de dinero del personaje principal"""

        self.money_count_images = []
        self.create_label(self.money_count_images, '*00', 300, 55)

    def create_flashing_money(self):

        """Flashing money junto al score total"""

        self.flashing_money = flashing_money.Money(280, 53)

    def create_game_image(self):

        """Metodo para obtener la imagen del personaje principal"""

        self.life_times_image = self.get_image(75, 247, 6, 6)
        self.life_times_rect = self.life_times_image.get_rect(center=(378, 295))
        self.life_total_label = []
        self.create_label(self.life_total_label, str(self.total_lives),
                           450, 285)
        self.sprite_sheet = setup.GFX['vaw']
        self.game_image = self.get_image(178, 32, 12, 16)
        self.game_rect = self.game_image.get_rect(center=(320, 290))

    def create_game_over_label(self):

        """Labels para la pantalla de GAME OVER"""

        game_label = []
        over_label = []

        self.create_label(game_label, 'GAME', 280, 300)
        self.create_label(over_label, 'OVER', 400, 300)
        self.game_over_label = [game_label, over_label]

    def create_time_out_label(self):

        """Labels para la pantalla de Time Out"""

        time_out_label = []

        self.create_label(time_out_label, 'TIME OUT', 290, 310)
        self.time_out_label = [time_out_label]

    def create_main_menu_labels(self):

        """Labels para la pantalla Principal de Menu"""

        player_one_game = []
        game_controls = []
        top = []
        top_score = []

        self.create_label(player_one_game, '1 PLAYER GAME', 272, 360)
        self.create_label (game_controls, 'CONTROLS', 272, 405)
        self.create_label(top, 'TOP - ', 290, 465)
        self.create_label(top_score, '000000', 400, 465)

        self.main_menu_labels = [player_one_game, game_controls, top, top_score]

    def update(self, level_info, game=None):

        """Update para toda la informacion adicional"""

        self.game = game
        self.handle_level_state(level_info)

    def handle_level_state(self, level_info):

        """Updates la info basada en que state esta el juego """

        if self.state == constants.MAIN_MENU:
            self.score = level_info[constants.SCORE]
            self.update_score_images(self.score_images, self.score)
            self.update_score_images(self.main_menu_labels[3], self.top_score)
            self.update_money_total(level_info)
            self.flashing_money.update(level_info[constants.CURRENT_TIME])

        elif self.state == constants.LOAD_SCREEN:
            self.score = level_info[constants.SCORE]
            self.update_score_images (self.score_images, self.score)
            self.update_money_total(level_info)

        elif self.state == constants.LEVEL:
            self.score = level_info[constants.SCORE]
            self.update_score_images(self.score_images, self.score)
            if level_info[constants.LEVEL_STATE] != constants.FROZEN \
                    and self.game.state != constants.WALKING_TO_CASTLE \
                    and self.game.state != constants.END_OF_LEVEL_FALL \
                    and not self.game.dead:
                self.update_count_down_clock(level_info)
            self.update_money_total(level_info)
            self.flashing_money.update(level_info[constants.CURRENT_TIME])

        elif self.state == constants.TIME_OUT:
            self.score = level_info[constants.SCORE]
            self.update_score_images(self.score_images, self.score)
            self.update_money_total(level_info)

        elif self.state == constants.GAME_OVER:
            self.score = level_info[constants.SCORE]
            self.update_score_images(self.score_images, self.score)
            self.update_money_total(level_info)

        elif self.state == constants.FAST_COUNT_DOWN:
            level_info[constants.SCORE] += 50
            self.score = level_info[constants.SCORE]
            self.update_count_down_clock(level_info)
            self.update_score_images(self.score_images, self.score)
            self.update_money_total(level_info)
            self.flashing_money.update(level_info[constants.CURRENT_TIME])
            if self.time == 0:
                self.state = constants.END_OF_LEVEL

        elif self.state == constants.END_OF_LEVEL:
            self.flashing_money.update(level_info[constants.CURRENT_TIME])

    def update_score_images(self, images, score):

        """Updates los números del score"""

        index = len(images) - 1

        for digit in reversed(str(score)):
            rect = images[index].rect
            images[index] = Character(self.image_dict[digit])
            images[index].rect = rect
            index -= 1

    def update_count_down_clock(self, level_info):

        """Updates el tiempo (reloj)"""

        if self.state == constants.FAST_COUNT_DOWN:
            self.time -= 1

        elif (level_info[constants.CURRENT_TIME] - self.current_time) > 400:
            self.current_time = level_info[constants.CURRENT_TIME]
            self.time -= 1
        self.count_down_images = []
        self.create_label (self.count_down_images, str(self.time), 645, 55)
        if len(self.count_down_images) < 2:
            for i in range(2):
                self.count_down_images.insert(0, Character(self.image_dict['0']))
            self.set_label_rects(self.count_down_images, 645, 55)
        elif len(self.count_down_images) < 3:
            self.count_down_images.insert(0, Character(self.image_dict['0']))
            self.set_label_rects(self.count_down_images, 645, 55)

    def update_money_total(self, level_info):

        """Updates el total de money (dinero)"""

        self.money_total = level_info[constants.COIN_TOTAL]

        money_string = str(self.money_total)
        if len(money_string) < 2:
            money_string = '*0' + money_string
        elif len(money_string) > 2:
            money_string = '*00'
        else:
            money_string = '*' + money_string

        x = self.money_count_images[0].rect.x
        y = self.money_count_images[0].rect.y

        self.money_count_images = []

        self.create_label(self.money_count_images, money_string, x, y)

    def draw(self, surface):

        """Muestra la info basada en el state """

        if self.state == constants.MAIN_MENU:
            self.draw_main_menu_info(surface)
        elif self.state == constants.LOAD_SCREEN:
            self.draw_loading_screen_info(surface)
        elif self.state == constants.LEVEL:
            self.draw_level_screen_info(surface)
        elif self.state == constants.GAME_OVER:
            self.draw_game_over_screen_info(surface)
        elif self.state == constants.FAST_COUNT_DOWN:
            self.draw_level_screen_info(surface)
        elif self.state == constants.END_OF_LEVEL:
            self.draw_level_screen_info(surface)
        elif self.state == constants.TIME_OUT:
            self.draw_time_out_screen_info(surface)
        else:
            pass

    def draw_main_menu_info(self, surface):

        """Muestra la info para el main menu"""

        for info in self.score_images:
            surface.blit(info.image, info.rect)

        for label in self.main_menu_labels:
            for letter in label:
                surface.blit(letter.image, letter.rect)

        for character in self.money_count_images:
            surface.blit(character.image, character.rect)

        for label in self.label_list:
            for letter in label:
                surface.blit(letter.image, letter.rect)

        surface.blit(self.flashing_money.image, self.flashing_money.rect)

    def draw_loading_screen_info(self, surface):

        """Muestra la info para el loading screen"""

        for info in self.score_images:
            surface.blit(info.image, info.rect)

        for word in self.center_labels:
            for letter in word:
                surface.blit(letter.image, letter.rect)

        for word in self.life_total_label:
            surface.blit(word.image, word.rect)

        surface.blit(self.game_image, self.game_rect)
        surface.blit(self.life_times_image, self.life_times_rect)

        for character in self.money_count_images:
            surface.blit(character.image, character.rect)

        for label in self.label_list:
            for letter in label:
                surface.blit(letter.image, letter.rect)

        surface.blit(self.flashing_money.image, self.flashing_money.rect)

    def draw_level_screen_info(self, surface):

        """Muestra la info en los niveles"""

        for info in self.score_images:
            surface.blit(info.image, info.rect)

        for digit in self.count_down_images:
            surface.blit(digit.image, digit.rect)

        for character in self.money_count_images:
            surface.blit(character.image, character.rect)

        for label in self.label_list:
            for letter in label:
                surface.blit(letter.image, letter.rect)

        surface.blit(self.flashing_money.image, self.flashing_money.rect)

    def draw_game_over_screen_info(self, surface):

        """Muestra la info en el state game over"""

        for info in self.score_images:
            surface.blit(info.image, info.rect)

        for word in self.game_over_label:
            for letter in word:
                surface.blit(letter.image, letter.rect)

        for character in self.money_count_images:
            surface.blit(character.image, character.rect)

        for label in self.label_list:
            for letter in label:
                surface.blit(letter.image, letter.rect)

        surface.blit(self.flashing_money.image, self.flashing_money.rect)

    def draw_time_out_screen_info(self, surface):

        """Muestra la infor en la pantalla time out"""

        for info in self.score_images:
            surface.blit(info.image, info.rect)

        for word in self.time_out_label:
            for letter in word:
                surface.blit(letter.image, letter.rect)

        for character in self.money_count_images:
            surface.blit(character.image, character.rect)

        for label in self.label_list:
            for letter in label:
                surface.blit(letter.image, letter.rect)

        surface.blit(self.flashing_money.image, self.flashing_money.rect)
