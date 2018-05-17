import pygame
from .. import constants
from .. import setup


class Powerup(pygame.sprite.Sprite):

    """Clase general para los powerups"""

    def __init__(self, x, y):
        super(Powerup, self).__init__()

    def setup_powerup(self, x, y, name, setup_frames):

        """Metodo que sirve como un manager para los diferentes powerups"""

        self.sprite_sheet = setup.GFX['item_objects']
        self.frames = []
        self.frame_index = 0
        setup_frames()
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.y = y
        self.state = constants.REVEAL
        self.y_vel = -1
        self.x_vel = 0
        self.direction = constants.RIGHT
        self.box_height = y
        self.gravity = 1
        self.max_y_vel = 8
        self.animate_timer = 0
        self.name = name

    def get_image(self, x, y, width, height):

        """Obtener la imagen del archivo de sprites"""

        image = pygame.Surface([width, height]).convert()
        rect = image.get_rect()

        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey(constants.BLACK)


        image = pygame.transform.scale(image,
                                   (int(rect.width*constants.SIZE_MULTIPLIER),
                                    int(rect.height*constants.SIZE_MULTIPLIER)))
        return image

    def update(self, game_info, *args):

        """Updates la logica de los powerups"""

        self.current_time = game_info[constants.CURRENT_TIME]
        self.handle_state()

    def handle_state(self):
        pass

    def revealing(self, *args):

        """Logica que contiene el comportamiento de los powerups cuando son usados"""

        self.rect.y += self.y_vel

        if self.rect.bottom <= self.box_height:
            self.rect.bottom = self.box_height
            self.y_vel = 0
            self.state = constants.SLIDE

    def sliding(self):

        """Metodo que contiene el comportamiento de los powerups cuando estan sliding (desplazandose por el suelo)"""

        if self.direction == constants.RIGHT:
            self.x_vel = 3
        else:
            self.x_vel = -3

    def falling(self):

        """etodo que contiene el comportamiento de los powerups cuando estan en caida"""
        if self.y_vel < self.max_y_vel:
            self.y_vel += self.gravity


class Mushroom(Powerup):

    """Powerup para convertir al personaje principal grande"""

    def __init__(self, x, y, name='mushroom'):
        super(Mushroom, self).__init__(x, y)
        self.setup_powerup(x, y, name, self.setup_frames)

    def setup_frames(self):


        self.frames.append(self.get_image(0, 0, 16, 16))

    def handle_state(self):

        """Configurar de la logica basado en el state"""

        if self.state == constants.REVEAL:
            self.revealing()
        elif self.state == constants.SLIDE:
            self.sliding()
        elif self.state == constants.FALL:
            self.falling()


class LifeMushroom(Mushroom):

    """Powerup que aumenta una vida"""

    def __init__(self, x, y, name='1up_mushroom'):
        super(LifeMushroom, self).__init__(x, y)
        self.setup_powerup(x, y, name, self.setup_frames)

    def setup_frames(self):
        self.frames.append(self.get_image(16, 0, 16, 16))

class FireFlower(Powerup):

    """Powerup para que el personaje principal pueda lanzar proyectiles"""

    def __init__(self, x, y, name=constants.FIREFLOWER):
        super(FireFlower, self).__init__(x, y)
        self.setup_powerup(x, y, name, self.setup_frames)

    def setup_frames(self):

        self.frames.append(
            self.get_image(0, 32, 16, 16))
        self.frames.append(
            self.get_image(16, 32, 16, 16))
        self.frames.append(
            self.get_image(32, 32, 16, 16))
        self.frames.append(
            self.get_image(48, 32, 16, 16))

    def handle_state(self):

        """Configurar de la logica basado en el state"""

        if self.state == constants.REVEAL:
            self.revealing()
        elif self.state == constants.RESTING:
            self.resting()

    def revealing(self):

        """Animacion de aparecer del FireFlower"""

        self.rect.y += self.y_vel

        if self.rect.bottom <= self.box_height:
            self.rect.bottom = self.box_height
            self.state = constants.RESTING

        self.animation()

    def resting(self):

        """FireFlower en estado de resting (sin moverse)"""

        self.animation()

    def animation(self):

        """Metodo para hacer que el FireFlower este en modo desaparecer"""

        if (self.current_time - self.animate_timer) > 30:
            if self.frame_index < 3:
                self.frame_index += 1
            else:
                self.frame_index = 0

            self.image = self.frames[self.frame_index]
            self.animate_timer = self.current_time

class Star(Powerup):

    """Powerup para convertir al personaje principal invulnerable"""

    def __init__(self, x, y, name='star'):
        super(Star, self).__init__(x, y)
        self.setup_powerup(x, y, name, self.setup_frames)
        self.animate_timer = 0
        self.rect.y += 1
        self.gravity = .4

    def setup_frames(self):

        self.frames.append(self.get_image(1, 48, 15, 16))
        self.frames.append(self.get_image(17, 48, 15, 16))
        self.frames.append(self.get_image(33, 48, 15, 16))
        self.frames.append(self.get_image(49, 48, 15, 16))

    def handle_state(self):

        """Configurar de la logica basado en el state"""

        if self.state == constants.REVEAL:
            self.revealing()
        elif self.state == constants.BOUNCE:
            self.bouncing()

    def revealing(self):

        """Animacion de aparecer de la Star"""

        self.rect.y += self.y_vel

        if self.rect.bottom <= self.box_height:
            self.rect.bottom = self.box_height
            self.start_bounce(-2)
            self.state = constants.BOUNCE

        self.animation()

    def animation(self):

        """Animacion del powerup Star"""

        if (self.current_time - self.animate_timer) > 30:
            if self.frame_index < 3:
                self.frame_index += 1
            else:
                self.frame_index = 0
            self.animate_timer = self.current_time
            self.image = self.frames[self.frame_index]

    def start_bounce(self, vel):

        """Empezar el state de bounce (rebotar)"""

        self.y_vel = vel

    def bouncing(self):

        """Animacion bounce"""

        self.animation()

        if self.direction == constants.LEFT:
            self.x_vel = -5
        else:
            self.x_vel = 5


class FireBall(pygame.sprite.Sprite):

    """Proyectil del FireFlower """

    def __init__(self, x, y, facing_right, name=constants.FIREBALL):
        super(FireBall, self).__init__()
        self.sprite_sheet = setup.GFX['item_objects']
        self.setup_frames()
        if facing_right:
            self.direction = constants.RIGHT
            self.x_vel = 12
        else:
            self.direction = constants.LEFT
            self.x_vel = -12
        self.y_vel = 10
        self.gravity = .9
        self.frame_index = 0
        self.animation_timer = 0
        self.state = constants.FLYING
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.right = x
        self.rect.y = y
        self.name = name

    def setup_frames(self):

        self.frames = []
        self.frames.append(
            self.get_image(96, 144, 8, 8))
        self.frames.append(
            self.get_image(104, 144, 8, 8))
        self.frames.append(
            self.get_image(96, 152, 8, 8))
        self.frames.append(
            self.get_image(104, 152, 8, 8))
        self.frames.append(
            self.get_image(112, 144, 16, 16))
        self.frames.append(
            self.get_image(112, 160, 16, 16))
        self.frames.append(
            self.get_image(112, 176, 16, 16))

    def get_image(self, x, y, width, height):

        """Obtener la imagen del archivo de sprite"""

        image = pygame.Surface([width, height]).convert()
        rect = image.get_rect()

        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey(constants.BLACK)


        image = pygame.transform.scale(image,
                                   (int(rect.width*constants.SIZE_MULTIPLIER),
                                    int(rect.height*constants.SIZE_MULTIPLIER)))
        return image

    def update(self, game_info, viewport):

        """Metodo update para el proyectil"""

        self.current_time = game_info[constants.CURRENT_TIME]
        self.handle_state()
        self.check_if_off_screen(viewport)

    def handle_state(self):

        """Configurar de la logica basado en el state"""

        if self.state == constants.FLYING:
            self.animation()
        elif self.state == constants.BOUNCING:
            self.animation()
        elif self.state == constants.EXPLODING:
            self.animation()

    def animation(self):

        """Metodo general de la animacion, usado para configurar los frames"""

        if self.state == constants.FLYING or self.state == constants.BOUNCING:
            if (self.current_time - self.animation_timer) > 200:
                if self.frame_index < 3:
                    self.frame_index += 1
                else:
                    self.frame_index = 0
                self.animation_timer = self.current_time
                self.image = self.frames[self.frame_index]


        elif self.state == constants.EXPLODING:
            if (self.current_time - self.animation_timer) > 50:
                if self.frame_index < 6:
                    self.frame_index += 1
                    self.image = self.frames[self.frame_index]
                    self.animation_timer = self.current_time
                else:
                    self.kill()

    def explode_transition(self):

        """Proyectil explotando"""

        self.frame_index = 4
        centerx = self.rect.centerx
        self.image = self.frames[self.frame_index]
        self.rect.centerx = centerx
        self.state = constants.EXPLODING

    def check_if_off_screen(self, viewport):

        if (self.rect.x > viewport.right) or (self.rect.y > viewport.bottom) \
            or (self.rect.right < viewport.x):
            self.kill()
