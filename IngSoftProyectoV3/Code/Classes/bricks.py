import pygame
from .. import setup
from .. import constants
from . import powerups
from . import money


class Brick(pygame.sprite.Sprite):

    """Obstaculos que se pueden destruir"""

    def __init__(self, x, y, contents=None, powerup_group=None, name='brick'):

        pygame.sprite.Sprite.__init__(self)
        self.sprite_sheet = setup.GFX['tile_set']

        self.frames = []
        self.frame_index = 0
        self.setup_frames()
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.mask = pygame.mask.from_surface(self.image)
        self.bumped_up = False
        self.rest_height = y
        self.state = constants.RESTING
        self.y_vel = 0
        self.gravity = 1.2
        self.name = name
        self.contents = contents
        self.setup_contents()
        self.group = powerup_group
        self.powerup_in_box = True


    def get_image(self, x, y, width, height):

        """Obtener la imagen del archivo de sprite"""

        image = pygame.Surface([width, height]).convert()
        rect = image.get_rect()

        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey(constants.BLACK)
        image = pygame.transform.scale(image,
                                   (int(rect.width*constants.BRICK_SIZE_MULTIPLIER),
                                    int(rect.height*constants.BRICK_SIZE_MULTIPLIER)))
        return image


    def setup_frames(self):

        """Ingresa los frames a una lista"""

        self.frames.append(self.get_image(16, 0, 16, 16))
        self.frames.append(self.get_image(432, 0, 16, 16))


    def setup_contents(self):

        """6 monedas en un obstaculo (si es necesario)"""

        if self.contents == '6coins':
            self.coin_total = 6
        else:
            self.coin_total = 0


    def update(self):

        """Updates los obstaculos"""

        self.handle_states()


    def handle_states(self):

        """Determina la logica de los obstaculos de acuerdo al estado en que se encuentran"""

        if self.state == constants.RESTING:
            self.resting()
        elif self.state == constants.BUMPED:
            self.bumped()
        elif self.state == constants.OPENED:
            self.opened()

    def resting(self):

        """State cuando no se toca al obstaculo"""

        if self.contents == '6coins':
            if self.coin_total == 0:
                self.state = constants.OPENED


    def bumped(self):

        """Comportamiento de los obstaculos cuando son tocados"""

        self.rect.y += self.y_vel
        self.y_vel += self.gravity

        if self.rect.y >= (self.rest_height + 5):
            self.rect.y = self.rest_height
            if self.contents == 'star':
                self.state = constants.OPENED
            elif self.contents == '6coins':
                if self.coin_total == 0:
                    self.state = constants.OPENED
                else:
                    self.state = constants.RESTING
            else:
                self.state = constants.RESTING


    def start_bump(self, score_group):

        """Transicion del obstaculo hacia el state bumped (tocado)"""

        self.y_vel = -6

        if self.contents == '6coins':
            setup.SFX['coin'].play()

            if self.coin_total > 0:
                self.group.add(money.Money(self.rect.centerx, self.rect.y, score_group))
                self.coin_total -= 1
                if self.coin_total == 0:
                    self.frame_index = 1
                    self.image = self.frames[self.frame_index]
        elif self.contents == 'star':
            setup.SFX['powerup_appears'].play()
            self.frame_index = 1
            self.image = self.frames[self.frame_index]

        self.state = constants.BUMPED


    def opened(self):

        """Comportamiento de los obstaculos cuando se obtiene el powerup de ellos"""

        self.frame_index = 1
        self.image = self.frames[self.frame_index]

        if self.contents == 'star' and self.powerup_in_box:
            self.group.add(powerups.Star(self.rect.centerx, self.rest_height))
            self.powerup_in_box = False


class BrickPiece(pygame.sprite.Sprite):

    """Escombros del obstaculo cuando este es destruido"""

    def __init__(self, x, y, xvel, yvel):
        super(BrickPiece, self).__init__()
        self.sprite_sheet = setup.GFX['item_objects']
        self.setup_frames()
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x_vel = xvel
        self.y_vel = yvel
        self.gravity = .8


    def setup_frames(self):

        """Lista de los frames"""

        self.frames = []

        image = self.get_image(68, 20, 8, 8)
        reversed_image = pygame.transform.flip(image, True, False)

        self.frames.append(image)
        self.frames.append(reversed_image)


    def get_image(self, x, y, width, height):

        """Obtener la imagen del archivo de sprite"""

        image = pygame.Surface([width, height]).convert()
        rect = image.get_rect()

        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey(constants.BLACK)
        image = pygame.transform.scale(image,
                                   (int(rect.width*constants.BRICK_SIZE_MULTIPLIER),
                                    int(rect.height*constants.BRICK_SIZE_MULTIPLIER)))
        return image


    def update(self):

        """Updates los escombros de los obstaculos"""

        self.rect.x += self.x_vel
        self.rect.y += self.y_vel
        self.y_vel += self.gravity
        self.check_if_off_screen()

    def check_if_off_screen(self):

        """Sacar de la pantalla los escombros"""

        if self.rect.y > constants.SCREEN_HEIGHT:
            self.kill()
