import pygame as pg
from .. import prepare_game
from .. import constants as c


class Digit(pg.sprite.Sprite):

    """
    Individual digit for score
    """

    def __init__(self, image):
        super(Digit, self).__init__()
        self.image = image
        self.rect = image.get_rect()


class Score(object):

    """
    Game score that appear, float up, and disappear
    """

    def __init__(self, x, y, score):
        self.x = x
        self.y = y
        self.y_vel = -3
        self.sprite_sheet = prepare_game.GFX['score_numbers']
        self.image_dict()
        self.score_string = str(score)
        self.digit_list()

    def image_dict(self):

        """
        Creates the dictionary for all the number images needed
        """

        self.image_dict = {}

        image0 = self.get_image(1, 1, 3, 8)
        image1 = self.get_image(5, 1, 3, 8)
        image2 = self.get_image(8, 1, 4, 8)
        image4 = self.get_image(12, 1, 4, 8)
        image5 = self.get_image(16, 1, 5, 8)
        image8 = self.get_image(20, 1, 4, 8)
        image9 = self.get_image(32, 1, 5, 8)
        image10 = self.get_image(37, 1, 6, 8)
        image11 = self.get_image(43, 1, 5, 8)

        self.image_dict['0'] = image0
        self.image_dict['1'] = image1
        self.image_dict['2'] = image2
        self.image_dict['4'] = image4
        self.image_dict['5'] = image5
        self.image_dict['8'] = image8
        self.image_dict['3'] = image9
        self.image_dict['7'] = image10
        self.image_dict['9'] = image11

    def get_image(self, x, y, width, height):

        """
        Extracts images from the sprite sheet
        """

        image = pg.Surface([width, height]).convert()
        rect = image.get_rect()

        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey(c.BLACK)
        image = pg.transform.scale(image,
                                   (int(rect.width*c.BRICK_SIZE_MULTIPLIER),
                                    int(rect.height*c.BRICK_SIZE_MULTIPLIER)))
        return image

    def digit_list(self):

        """
        Creates the group of images based on score received
        """

        self.digit_list = []
        self.digit_group = pg.sprite.Group()

        for digit in self.score_string:
            self.digit_list.append(Digit(self.image_dict[digit]))

        self.set_rects_for_images()

    def set_rects_for_images(self):

        """
        Set the rect attributes for each image in self.image_list
        """

        for i, digit in enumerate(self.digit_list):
            digit.rect = digit.image.get_rect()
            digit.rect.x = self.x + (i * 10)
            digit.rect.y = self.y

    def update(self, score_list, level_info):

        """
        Updates score movement
        """

        for number in self.digit_list:
            number.rect.y += self.y_vel

        if score_list:
            self.check_to_delete_floating_scores(score_list, level_info)

    def draw(self, screen):

        """
        Draws score numbers onto screen
        """

        for digit in self.digit_list:
            screen.blit(digit.image, digit.rect)

    def check_to_delete_floating_scores(self, score_list, level_info):

        """
        Check if scores need to be deleted
        """

        for i, score in enumerate(score_list):
            if int(score.score_string) == 1000:
                if (score.y - score.digit_list[0].rect.y) > 130:
                    score_list.pop(i)
            else:
                if (score.y - score.digit_list[0].rect.y) > 75:
                    score_list.pop(i)
