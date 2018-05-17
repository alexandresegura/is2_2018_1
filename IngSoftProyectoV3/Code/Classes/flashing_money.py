import pygame
from .. import setup
from .. import constants


class Money(pygame.sprite.Sprite):

    """Dinero animado al costado de la info del dinero"""

    def __init__(self, x, y):
        super(Money, self).__init__()
        self.sprite_sheet = setup.GFX['item_objects']
        self.create_frames()
        self.image = self.frames[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.timer = 0
        self.first_half = True
        self.frame_index = 0

    def create_frames(self):

        """Extrae las imagenes del dinero del archivo de Sprite y los asigna a una lista"""

        self.frames = []
        self.frame_index = 0
        self.frames.append(self.get_image(1, 160, 5, 8))
        self.frames.append(self.get_image(9, 160, 5, 8))
        self.frames.append(self.get_image(17, 160, 5, 8))

    def get_image(self, x, y, width, height):

        """Extrae las imagenes del archivo de Sprite"""

        image = pygame.Surface([width, height])
        rect = image.get_rect()

        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey(constants.BLACK)
        image = pygame.transform.scale(image,
                                   (int(rect.width*constants.BRICK_SIZE_MULTIPLIER),
                                    int(rect.height*constants.BRICK_SIZE_MULTIPLIER)))
        return image

    def update(self, current_time):

        """Logica de la clase (anima el dinero)"""

        if self.first_half:
            if self.frame_index == 0:
                if (current_time - self.timer) > 375:
                    self.frame_index += 1
                    self.timer = current_time
            elif self.frame_index < 2:
                if (current_time - self.timer) > 125:
                    self.frame_index += 1
                    self.timer = current_time
            elif self.frame_index == 2:
                if (current_time - self.timer) > 125:
                    self.frame_index -= 1
                    self.first_half = False
                    self.timer = current_time
        else:
            if self.frame_index == 1:
                if (current_time - self.timer) > 125:
                    self.frame_index -= 1
                    self.first_half = True
                    self.timer = current_time

        self.image = self.frames[self.frame_index]
