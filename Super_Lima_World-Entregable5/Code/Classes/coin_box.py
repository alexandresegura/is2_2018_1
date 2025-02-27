import pygame as pg
from .. import constants as c
from .. import prepare_game
from . import coin, powerups


class Coin_box(pg.sprite.Sprite):

    """
    Coin box sprite
    """

    def __init__(self, x, y, contents='coin', group=None):
        pg.sprite.Sprite.__init__(self)
        self.sprite_sheet = prepare_game.GFX['coin_box']
        self.frames = []
        self.setup_frames()
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.mask = pg.mask.from_surface(self.image)
        self.animation_timer = 0
        self.first_half = True   # First half of animation cycle
        self.state = c.RESTING
        self.rest_height = y
        self.gravity = 1.2
        self.y_vel = 0
        self.contents = contents
        self.group = group

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

    def setup_frames(self):

        """
        Creates frame list
        """

        self.frames.append(
            self.get_image(0, 0, 16, 16))
        self.frames.append(
            self.get_image(16, 0, 16, 16))
        self.frames.append(
            self.get_image(32, 0, 16, 16))
        self.frames.append(
            self.get_image(48, 0, 16, 16))

    def update(self, game_labels):

        """
        Updates coin box logic
        """
        self.current_time = game_labels[c.CURRENT_TIME]
        self.handle_states()

    def handle_states(self):

        """
        Determinates action based on RESTING, BUMPED or OPENED
        state
        """

        if self.state == c.RESTING:
            self.resting()
        elif self.state == c.BUMPED:
            self.bumped()
        elif self.state == c.OPENED:
            self.opened()

    def resting(self):

        """
        Action when in the RESTING state
        """

        if self.first_half:
            if self.frame_index == 0:
                if (self.current_time - self.animation_timer) > 375:
                    self.frame_index += 1
                    self.animation_timer = self.current_time
            elif self.frame_index < 2:
                if (self.current_time - self.animation_timer) > 125:
                    self.frame_index += 1
                    self.animation_timer = self.current_time
            elif self.frame_index == 2:
                if (self.current_time - self.animation_timer) > 125:
                    self.frame_index -= 1
                    self.first_half = False
                    self.animation_timer = self.current_time
        else:
            if self.frame_index == 1:
                if (self.current_time - self.animation_timer) > 125:
                    self.frame_index -= 1
                    self.first_half = True
                    self.animation_timer = self.current_time

        self.image = self.frames[self.frame_index]

    def bumped(self):

        """
        Action when in the BUMPED state
        """

        self.rect.y += self.y_vel
        self.y_vel += self.gravity
        if self.rect.y > self.rest_height + 5:
            self.rect.y = self.rest_height
            self.state = c.OPENED
            if self.contents == 'bigchar':
                self.group.add(powerups.BigChar(self.rect.centerx,
                                                 self.rect.y))
            elif self.contents == 'firechar':
                self.group.add(powerups.FireChar(self.rect.centerx,
                                                   self.rect.y))
            elif self.contents == 'onelife':
                self.group.add(powerups.OneLife(self.rect.centerx,
                                                     self.rect.y))

        self.frame_index = 3
        self.image = self.frames[self.frame_index]

    def start_bump(self, score_group):

        """
        Transitions box into BUMPED state
        """

        self.y_vel = -6
        self.state = c.BUMPED

        if self.contents == 'coin':
            self.group.add(coin.Coin(self.rect.centerx,
                                     self.rect.y,
                                     score_group))
            prepare_game.SFX['coin'].play()
        else:
            prepare_game.SFX['powerup_appears'].play()

    def opened(self):

        """
        Placeholder for OPENED state
        """

        pass
