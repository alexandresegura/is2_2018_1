import pygame as pg
from .. import constants as c


class Checkpoint(pg.sprite.Sprite):

    """
    Invisible sprite used to add enemies and special boxes
    """

    def __init__(self, x, name, y=0, width=1, height=600):
        super(Checkpoint, self).__init__()
        self.image = pg.Surface((width, height), pg.SRCALPHA)
        self.image.fill((255, 255, 255, 128))
        self.image.blit(self.image, (0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.name = name
