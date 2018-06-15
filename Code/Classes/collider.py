import pygame as pg


class Collider(pg.sprite.Sprite):

    """
    Invisible sprites placed over background parts
    that can be collided with (pipes, steps, ground, etc.
    """

    def __init__(self, x, y, width, height, name='collider'):

        """
        Initializes the state with all the variables needed
        """

        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((width, height)).convert()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.state = None