import pygame as pg
from .. import constants as c
from .. import prepare_game
from . import animated_coin


class Character(pg.sprite.Sprite):

    """
    Parent class for all characters used for the overhead level labels
    """

    def __init__(self, image):

        """
        Initializes the state
        """

        super(Character, self).__init__()
        self.image = image
        self.rect = self.image.get_rect()


class OverheadLabels:

    """
    Class for states labels like score, coin total, and time remaining
    """

    def __init__(self, game_labels, state):

        """
        Initializes the state with all the variables needed
        """

        self.sprite_sheet = prepare_game.GFX['game_text']
        self.coin_total = game_labels[c.COIN_TOTAL]
        self.time = 401
        self.current_time = 0
        self.total_lives = game_labels[c.LIVES]
        self.top_score = game_labels[c.TOP_SCORE]
        self.state = state
        self.special_state = None
        self.game_labels = game_labels

        self.images_dict()
        self.score_group()
        self.info_labels()
        self.load_screen_labels()
        self.load_screen_labels2()
        self.countdown_clock()
        self.coin_counter()
        self.animated_coin()
        self.char_image()
        self.game_over_label()
        self.time_out_label()
        self.main_menu_labels()
        self.controls_menu_labels()
        self.credits_menu_labels()

    def images_dict(self):

        """
        Creates the image dict, which are got from the game_text file.
        It uses the method get_image to get the images for the character_string
        variable content
        """

        self.image_dict = {}
        image_list = []

        image_list.append(self.get_image(0, 0, 7, 7))
        image_list.append(self.get_image(9, 0, 7, 7))
        image_list.append(self.get_image(16, 0, 7, 7))
        image_list.append(self.get_image(24, 0, 7, 7))
        image_list.append(self.get_image(32, 0, 7, 7))
        image_list.append(self.get_image(40, 0, 7, 7))
        image_list.append(self.get_image(48, 0, 7, 7))
        image_list.append(self.get_image(56, 0, 7, 7))
        image_list.append(self.get_image(64, 0, 7, 7))
        image_list.append(self.get_image(72, 0, 7, 7))
        image_list.append(self.get_image(80, 0, 7, 7))
        image_list.append(self.get_image(88, 0, 7, 7))
        image_list.append(self.get_image(96, 0, 7, 7))
        image_list.append(self.get_image(104, 0, 7, 7))
        image_list.append(self.get_image(112, 0, 7, 7))
        image_list.append(self.get_image(120, 0, 7, 7))
        image_list.append(self.get_image(0, 8, 7, 7))
        image_list.append(self.get_image(8, 8, 7, 7))
        image_list.append(self.get_image(17, 8, 7, 7))
        image_list.append(self.get_image(24, 8, 7, 7))
        image_list.append(self.get_image(32, 8, 7, 7))
        image_list.append(self.get_image(41, 8, 7, 7))
        image_list.append(self.get_image(48, 8, 7, 7))
        image_list.append(self.get_image(56, 8, 7, 7))
        image_list.append(self.get_image(64, 8, 7, 7))
        image_list.append(self.get_image(72, 8, 7, 7))
        image_list.append(self.get_image(80, 8, 7, 7))
        image_list.append(self.get_image(88, 8, 7, 7))
        image_list.append(self.get_image(96, 8, 7, 7))
        image_list.append(self.get_image(105, 8, 7, 7))
        image_list.append(self.get_image(112, 8, 7, 7))
        image_list.append(self.get_image(120, 8, 7, 7))
        image_list.append(self.get_image(0, 16, 7, 7))
        image_list.append(self.get_image(8, 16, 7, 7))
        image_list.append(self.get_image(17, 16, 7, 7))
        image_list.append(self.get_image(24, 16, 7, 7))
        image_list.append(self.get_image(45, 18, 7, 7))
        image_list.append(self.get_image(65, 19, 6, 2))
        image_list.append(self.get_image(72, 17, 6, 6))

        character_string = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ -*'

        for character, image in zip(character_string, image_list):
            self.image_dict[character] = image

    def get_image(self, x, y, width, height):

        """
        Extracts images from the sprite sheet
        """

        image = pg.Surface([width, height])
        rect = image.get_rect()

        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey(c.BLACK)
        image = pg.transform.scale(image,
                                   (int(rect.width*2.9),
                                    int(rect.height*2.9)))
        return image

    def score_group(self):

        """
        Creates the initial empty score (0000000)
        """

        self.score_images = []
        self.create_label(self.score_images, '0000000', 100, 55)

    def info_labels(self):

        """
        Creates the labels that describe each variable
        """

        self.char_label = []
        self.world_label = []
        self.time_label = []
        self.stage_label = []

        self.create_label(self.char_label, 'CARLOBROS', 75, 30)
        self.create_label(self.world_label, 'LEVEL', 450, 30)
        self.create_label(self.time_label, 'TIME', 625, 30)
        self.create_label(self.stage_label, '1', 492, 55)

        self.label_list = [self.char_label,
                           self.world_label,
                           self.time_label,
                           self.stage_label]

    def load_screen_labels(self):

        """
        Creates labels for the center labels of the load screen
        """

        world_label = []
        number_label = []

        self.create_label(world_label, 'LEVEL', 310, 200)
        self.create_label(number_label, '1', 460, 200)

        self.center_labels = [world_label, number_label]

    def load_screen_labels2(self):

        """
        Creates labels for the center labels of the load screen
        """

        world_label2 = []
        number_label2 = []

        self.create_label(world_label2, 'LEVEL', 310, 200)
        self.create_label(number_label2, '2', 460, 200)

        self.center_labels2 = [world_label2, number_label2]

    def countdown_clock(self):

        """
        Creates the count down clock for the level
        """

        self.count_down_images = []
        self.create_label(self.count_down_images, str(self.time), 645, 55)

    def create_label(self, label_list, string, x, y):

        """
        Method to actually make the labels
        """

        for letter in string:
            label_list.append(Character(self.image_dict[letter]))

        self.set_label_rects(label_list, x, y)

    def set_label_rects(self, label_list, x, y):

        """
        Set the location of each individual char
        """

        for i, letter in enumerate(label_list):
            letter.rect.x = x + ((letter.rect.width + 3) * i)
            letter.rect.y = y
            if letter.image == self.image_dict['-']:
                letter.rect.y += 7
                letter.rect.x += 2

    def coin_counter(self):

        """
        Creates the label that tracks the number of coins the character gets
        """

        self.coin_count_images = []
        self.create_label(self.coin_count_images, '*00', 320, 55)

    def animated_coin(self):

        """
        Creates the animated coin next to the coin score
        """

        self.animated_coin = animated_coin.Coin(300, 53)

    def char_image(self):

        """
        Get the char image and some of the char game logic
        """

        self.lifes_image = self.get_image(75, 247, 6, 6)
        self.lifes_rect = self.lifes_image.get_rect(center=(408, 295))
        self.life_total_label = []
        self.create_label(self.life_total_label, str(self.total_lives),
                          430, 305)

        self.sprite_sheet = prepare_game.GFX['main']
        self.char_image = self.get_image(0, 0, 26, 65)
        self.char_rect = self.char_image.get_rect(center=(360, 320))

    def game_over_label(self):

        """
        Create the labels for the GAME OVER screen/state
        """

        game_label = []
        over_label = []

        self.create_label(game_label, 'GAME', 300, 270)
        self.create_label(over_label, 'OVER', 420, 270)

        self.game_over_label = [game_label, over_label]

    def time_out_label(self):

        """
        Create the label for the time out screen/state
        """

        time_out_label = []

        self.create_label(time_out_label, 'TIME OUT', 290, 310)
        self.time_out_label = [time_out_label]

    def main_menu_labels(self):

        """
        Create labels for the MAIN MENU screen/state
        """

        game_start = []
        controls = []
        credits = []
        exit = []
        top = []
        top_score = []

        self.create_label(game_start, 'START GAME', 302, 340)
        self.create_label(controls, 'CONTROLS', 302, 385)
        self.create_label(credits, 'CREDITS', 302, 430)
        self.create_label(exit, 'QUIT GAME', 302, 475)
        self.create_label(top, 'TOP - ', 320, 535)
        self.create_label(top_score, '000000', 450, 535)

        self.main_menu_labels = [game_start, controls, credits,
                                 exit, top, top_score]

    def controls_menu_labels(self):
        """
        Create labels for the CONTROLS MENU screen/state
        """
        back = []
        self.create_label(back, 'BACK', 900, 640)
        self.controls_menu_labels = [back]

    def credits_menu_labels(self):
        """
        Create labels for the CREDITS MENU screen/state
        """

        grupo = []
        integ1 = []
        integ2 = []
        integ3 = []
        integ4 = []
        back = []
        #self.create_label(integrantes, 'INTEGRANTES', 440, 100)
        self.create_label(grupo, 'GRUPO 7', 350, 100)
        self.create_label(integ1, 'RENATO ARTEAGA', 300, 180)
        self.create_label(integ2, 'JUAN BENATE', 300, 250)
        self.create_label(integ3, 'GUSTAVO REYES', 300, 300)
        self.create_label(integ4, 'AUGUSTO SEGURA', 300, 360)
        self.create_label(back, 'BACK', 600, 500)

        self.credits_menu_labels = [grupo, integ1, integ2, integ3, integ4, back]

    def update(self, level_labels, char=None):

        """
        Updates all overhead labels
        """

        self.char = char
        self.handle_level_state(level_labels)

    def handle_level_state(self, level_labels):

        """
        Updates lavels based on what state the game is in
        """

        if self.state == c.MAIN_MENU:
            self.score = level_labels[c.SCORE]
            self.update_score_images(self.score_images, self.score)
            self.update_score_images(self.main_menu_labels[5], self.top_score)
            self.update_coin_total(level_labels)
            self.animated_coin.update(level_labels[c.CURRENT_TIME])

        elif self.state == c.LOAD_SCREEN:
            self.score = level_labels[c.SCORE]
            self.update_score_images(self.score_images, self.score)
            self.update_coin_total(level_labels)

        elif self.state == c.LOAD_SCREEN2:
            self.score = level_labels[c.SCORE]
            self.update_score_images(self.score_images, self.score)
            self.update_coin_total(level_labels)

        elif self.state == c.LEVEL:
            self.score = level_labels[c.SCORE]
            self.update_score_images(self.score_images, self.score)
            if level_labels[c.LEVEL_STATE] != c.FROZEN \
                    and self.char.state != c.WALKING_TO_CASTLE \
                    and self.char.state != c.END_OF_LEVEL_FALL \
                    and not self.char.dead:
                self.update_count_down_clock(level_labels)
            self.update_coin_total(level_labels)
            self.animated_coin.update(level_labels[c.CURRENT_TIME])

        elif self.state == c.TIME_OUT:
            self.score = level_labels[c.SCORE]
            self.update_score_images(self.score_images, self.score)
            self.update_coin_total(level_labels)

        elif self.state == c.GAME_OVER:
            self.score = level_labels[c.SCORE]
            self.update_score_images(self.score_images, self.score)
            self.update_coin_total(level_labels)

        elif self.state == c.FAST_COUNT_DOWN:
            level_labels[c.SCORE] += 50
            self.score = level_labels[c.SCORE]
            self.update_count_down_clock(level_labels)
            self.update_score_images(self.score_images, self.score)
            self.update_coin_total(level_labels)
            self.animated_coin.update(level_labels[c.CURRENT_TIME])
            if self.time == 0:
                self.state = c.END_OF_LEVEL

        elif self.state == c.END_OF_LEVEL:
            self.animated_coin.update(level_labels[c.CURRENT_TIME])

    def update_score_images(self, images, score):

        """
        Updates what numbers are to be blitted for the score
        """

        index = len(images) - 1
        for digit in reversed(str(score)):
            rect = images[index].rect
            images[index] = Character(self.image_dict[digit])
            images[index].rect = rect
            index -= 1

    def update_count_down_clock(self, level_labels):

        """
        Updates current time
        """

        if self.state == c.FAST_COUNT_DOWN:
            self.time -= 1

        elif (level_labels[c.CURRENT_TIME] - self.current_time) > 400:
            self.current_time = level_labels[c.CURRENT_TIME]
            self.time -= 1
        self.count_down_images = []
        self.create_label(self.count_down_images, str(self.time), 645, 55)
        if len(self.count_down_images) < 2:
            for i in range(2):
                self.count_down_images.insert(0,
                                              Character(self.image_dict['0']))
            self.set_label_rects(self.count_down_images, 645, 55)
        elif len(self.count_down_images) < 3:
            self.count_down_images.insert(0,
                                          Character(self.image_dict['0']))
            self.set_label_rects(self.count_down_images, 645, 55)

    def update_coin_total(self, level_labels):

        """
        Updates the coin total and adjusts the labels accordingly
        """

        self.coin_total = level_labels[c.COIN_TOTAL]

        coin_string = str(self.coin_total)
        if len(coin_string) < 2:
            coin_string = '*0' + coin_string
        elif len(coin_string) > 2:
            coin_string = '*00'
        else:
            coin_string = '*' + coin_string

        x = self.coin_count_images[0].rect.x
        y = self.coin_count_images[0].rect.y

        self.coin_count_images = []
        self.create_label(self.coin_count_images, coin_string, x, y)

    def draw(self, surface):

        """
        Draws overhead labels based on state
        """

        if self.state == c.MAIN_MENU:
            self.draw_main_menu_labels(surface)
        elif self.state == c.CONTROLS_MENU:
            self.draw_controls_menu_labels(surface)
        elif self.state == c.CREDITS_MENU:
            self.draw_credits_menu_labels(surface)
        elif self.state == c.LOAD_SCREEN:
            self.draw_loading_screen_labels(surface)
        elif self.state == c.LOAD_SCREEN2:
            self.draw_loading_screen_labels2(surface)
        elif self.state == c.LEVEL:
            self.draw_level_screen_labels(surface)
        elif self.state == c.GAME_OVER:
            self.draw_game_over_screen_labels(surface)
        elif self.state == c.FAST_COUNT_DOWN:
            self.draw_level_screen_labels(surface)
        elif self.state == c.END_OF_LEVEL:
            self.draw_level_screen_labels(surface)
        elif self.state == c.TIME_OUT:
            self.draw_time_out_screen_labels(surface)
        else:
            pass

    def draw_main_menu_labels(self, surface):

        """
        Draws labels for main menu state
        """

        for label in self.main_menu_labels:
            for letter in label:
                surface.blit(letter.image, letter.rect)

    def draw_controls_menu_labels(self, surface):

        """
        Draws labels for controls menu state
        """

        for label in self.controls_menu_labels:
            for letter in label:
                surface.blit(letter.image, letter.rect)

    def draw_credits_menu_labels(self, surface):

        """
        Draws labels for credits menu state
        """

        for label in self.credits_menu_labels:
            for letter in label:
                surface.blit(letter.image, letter.rect)

    def draw_loading_screen_labels(self, surface):

        """
        Draws labels for loading screen state
        """

        for word in self.center_labels:
            for letter in word:
                surface.blit(letter.image, letter.rect)

        for word in self.life_total_label:
            surface.blit(word.image, word.rect)

        surface.blit(self.char_image, self.char_rect)
        surface.blit(self.lifes_image, self.lifes_rect)


    def draw_loading_screen_labels2(self, surface):

        """
        Draws labels for loading screen state
        """

        for word in self.center_labels2:
            for letter in word:
                surface.blit(letter.image, letter.rect)

        for word in self.life_total_label:
            surface.blit(word.image, word.rect)

        surface.blit(self.char_image, self.char_rect)
        surface.blit(self.lifes_image, self.lifes_rect)

    def draw_level_screen_labels(self, surface):

        """
        Draws labels during regular game play
        """

        for label in self.score_images:
            surface.blit(label.image, label.rect)

        for digit in self.count_down_images:
                surface.blit(digit.image, digit.rect)

        for character in self.coin_count_images:
            surface.blit(character.image, character.rect)

        for label in self.label_list:
            for letter in label:
                surface.blit(letter.image, letter.rect)

        surface.blit(self.animated_coin.image, self.animated_coin.rect)

    def draw_game_over_screen_labels(self, surface):

        """
        Draws labels for game over state
        """

        for word in self.game_over_label:
            for letter in word:
                surface.blit(letter.image, letter.rect)

    def draw_time_out_screen_labels(self, surface):

        """
        Draws labels for the time out screen state
        """

        for label in self.score_images:
            surface.blit(label.image, label.rect)

        for word in self.time_out_label:
            for letter in word:
                surface.blit(letter.image, letter.rect)

        for character in self.coin_count_images:
            surface.blit(character.image, character.rect)

        for label in self.label_list:
            for letter in label:
                surface.blit(letter.image, letter.rect)

        surface.blit(self.animated_coin.image, self.animated_coin.rect)


class OverheadLabels2(OverheadLabels):

    def __init__(self, game_labels, state):

        """
        Initializes the state with all the variables needed
        """

        self.sprite_sheet = prepare_game.GFX['game_text']
        self.coin_total = game_labels[c.COIN_TOTAL]
        self.time = 401
        self.current_time = 0
        self.total_lives = game_labels[c.LIVES]
        self.top_score = game_labels[c.TOP_SCORE]
        self.state = state
        self.special_state = None
        self.game_labels = game_labels

        self.images_dict()
        self.score_group()
        self.info_labels()
        self.load_screen_labels()
        self.load_screen_labels2()
        self.countdown_clock()
        self.coin_counter()
        self.animated_coin()
        self.char_image()
        self.game_over_label()
        self.time_out_label()
        self.main_menu_labels()
        self.controls_menu_labels()
        self.credits_menu_labels()

    def info_labels(self):

        """
        Creates the labels that describe each variable
        """

        self.char_label = []
        self.world_label = []
        self.time_label = []
        self.stage_label = []

        self.create_label(self.char_label, 'CARLOBROS', 75, 30)
        self.create_label(self.world_label, 'LEVEL', 450, 30)
        self.create_label(self.time_label, 'TIME', 625, 30)
        self.create_label(self.stage_label, '2', 492, 55)

        self.label_list = [self.char_label,
                           self.world_label,
                           self.time_label,
                           self.stage_label]
