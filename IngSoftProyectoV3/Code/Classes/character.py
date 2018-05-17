import pygame
from .. import setup, means
from .. import constants
from . import powerups


class Character(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__ (self)
        self.sprite_sheet = setup.GFX['vaw']
        self.setup_timers()
        self.setup_state_booleans()
        self.setup_forces()
        self.setup_counters()
        self.load_images_from_sheet()

        self.state = constants.WALK
        self.image = self.right_frames[self.frame_index]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

        self.key_timer = 0

    def setup_timers(self):

        """Timers para las animaciones"""

        self.walking_timer = 0
        self.invincible_animation_timer = 0
        self.invincible_start_timer = 0
        self.fire_transition_timer = 0
        self.death_timer = 0
        self.transition_timer = 0
        self.last_fireball_time = 0
        self.hurt_invisible_timer = 0
        self.hurt_invisible_timer2 = 0
        self.flag_pole_timer = 0

    def setup_state_booleans(self):

        """Booleans para la logica del personaje principal"""

        self.facing_right = True
        self.allow_jump = True
        self.dead = False
        self.invincible = False
        self.big = False
        self.fire = False
        self.allow_fireball = True
        self.in_transition_state = False
        self.hurt_invincible = False
        self.in_castle = False
        self.crouching = False
        self.losing_invincibility = False

    def setup_forces(self):

        """Atributos para codificar la velocidad del personaje principal"""

        self.x_vel = 0
        self.y_vel = 0
        self.max_x_vel = constants.MAX_WALK_SPEED
        self.max_y_vel = constants.MAX_Y_SPEED
        self.x_accel = constants.WALK_ACC
        self.jump_vel = constants.JUMP_SPEED
        self.gravity = constants.GRAVITY

    def setup_counters(self):

        """Ayuda para controlar algunos valores"""

        self.frame_index = 0
        self.invincible_index = 0
        self.fire_transition_index = 0
        self.fireball_count = 0
        self.flag_pole_right = 0

    def load_images_from_sheet(self):

        """Extrae las imagenes del personaje principal del archivo de sprites y
           los asigna a una lista"""

        self.right_frames = []
        self.left_frames = []
        self.right_small_normal_frames = []
        self.left_small_normal_frames = []
        self.right_small_green_frames = []
        self.left_small_green_frames = []
        self.right_small_red_frames = []
        self.left_small_red_frames = []
        self.right_small_black_frames = []
        self.left_small_black_frames = []
        self.right_big_normal_frames = []
        self.left_big_normal_frames = []
        self.right_big_green_frames = []
        self.left_big_green_frames = []
        self.right_big_red_frames = []
        self.left_big_red_frames = []
        self.right_big_black_frames = []
        self.left_big_black_frames = []
        self.right_fire_frames = []
        self.left_fire_frames = []

        # Imagenes del personaje principal en modo normal

        self.right_small_normal_frames.append (
            self.get_image (178, 32, 12, 16))  # Mirando hacia la derecha [0]
        self.right_small_normal_frames.append (
            self.get_image (80, 32, 15, 16))  # Caminando hacia la derecha [1]
        self.right_small_normal_frames.append (
            self.get_image (96, 32, 16, 16))  # Caminando hacia la derecha 2 [2]
        self.right_small_normal_frames.append (
            self.get_image (112, 32, 16, 16))  # Caminando hacia la derecha 3 [3]
        self.right_small_normal_frames.append (
            self.get_image (144, 32, 16, 16))  # Salto a la derecha [4]
        self.right_small_normal_frames.append (
            self.get_image (130, 32, 14, 16))  # Skid hacia la derecha [5]
        self.right_small_normal_frames.append (
            self.get_image (160, 32, 15, 16))  # Muerte [6]
        self.right_small_normal_frames.append (
            self.get_image (320, 8, 16, 24))  # Cambio de chico a grande [7]
        self.right_small_normal_frames.append (
            self.get_image (241, 33, 16, 16))  # Cambio de grande a chico [8]
        self.right_small_normal_frames.append (
            self.get_image (194, 32, 12, 16))  # Slide del Pole [9]
        self.right_small_normal_frames.append (
            self.get_image (210, 33, 12, 16))  # Slide 2 del Pole [10]

        # Inagenes del personaje principal verde

        self.right_small_green_frames.append (
            self.get_image (178, 224, 12, 16))  # Mirando hacia la derecha [0]
        self.right_small_green_frames.append (
            self.get_image (80, 224, 15, 16))  # Caminando hacia la derecha [1]
        self.right_small_green_frames.append (
            self.get_image (96, 224, 16, 16))  # Caminando hacia la derecha  2 [2]
        self.right_small_green_frames.append (
            self.get_image (112, 224, 15, 16))  # Caminando hacia la derecha  3 [3]
        self.right_small_green_frames.append (
            self.get_image (144, 224, 16, 16))  # Salto a la derecha [4]
        self.right_small_green_frames.append (
            self.get_image (130, 224, 14, 16))  # Skid hacia la derecha [5]

        # Imagenes del personaje principal rojo

        self.right_small_red_frames.append (
            self.get_image (178, 272, 12, 16))  # Mirando hacia la derecha [0]
        self.right_small_red_frames.append (
            self.get_image (80, 272, 15, 16))  # Caminando hacia la derecha [1]
        self.right_small_red_frames.append (
            self.get_image (96, 272, 16, 16))  # Caminando hacia la derecha 2 [2]
        self.right_small_red_frames.append (
            self.get_image (112, 272, 15, 16))  # Caminando hacia la derecha 3 [3]
        self.right_small_red_frames.append (
            self.get_image (144, 272, 16, 16))  # Salto a la derecha [4]
        self.right_small_red_frames.append (
            self.get_image (130, 272, 14, 16))  # Skid hacia la derecha [5]

        # Imagenes del personaje principal negro

        self.right_small_black_frames.append (
            self.get_image (178, 176, 12, 16))  # Mirando hacia la derecha [0]
        self.right_small_black_frames.append (
            self.get_image (80, 176, 15, 16))  # Caminando hacia la derecha 1 [1]
        self.right_small_black_frames.append (
            self.get_image (96, 176, 16, 16))  # Caminando hacia la derecha 2 [2]
        self.right_small_black_frames.append (
            self.get_image (112, 176, 15, 16))  # Caminando hacia la derecha 3 [3]
        self.right_small_black_frames.append (
            self.get_image (144, 176, 16, 16))  # Salto a la derecha [4]
        self.right_small_black_frames.append (
            self.get_image (130, 176, 14, 16))  # Skid hacia la derecha [5]

        # Imagenes para el personaje principal

        self.right_big_normal_frames.append (
            self.get_image (176, 0, 16, 32))  # Mirando hacia la derecha [0]
        self.right_big_normal_frames.append (
            self.get_image (81, 0, 16, 32))  # Caminando hacia la derecha 1 [1]
        self.right_big_normal_frames.append (
            self.get_image (97, 0, 15, 32))  # Caminando hacia la derecha 2 [3]
        self.right_big_normal_frames.append (
            self.get_image (113, 0, 15, 32))  # Caminando hacia la derecha 3 [3]
        self.right_big_normal_frames.append (
            self.get_image (144, 0, 16, 32))  # Salto a la derecha [4]
        self.right_big_normal_frames.append (
            self.get_image (128, 0, 16, 32))  # Skid hacia la derecha [5]
        self.right_big_normal_frames.append (
            self.get_image (336, 0, 16, 32))  # Lanzar hacia la derecha [6]
        self.right_big_normal_frames.append (
            self.get_image (160, 10, 16, 22))  # Agacharse hacia la derecha [7]
        self.right_big_normal_frames.append (
            self.get_image (272, 2, 16, 29))  # Chico a grande [8]
        self.right_big_normal_frames.append (
            self.get_image (193, 2, 16, 30))  # Frame 1 del flag pole [9]
        self.right_big_normal_frames.append (
            self.get_image (209, 2, 16, 29))  # Frame 2 del flag pole [10]

        # Imagenes para personaje principal grande Verde

        self.right_big_green_frames.append (
            self.get_image (176, 192, 16, 32))  # Mirando hacia la derecha [0]
        self.right_big_green_frames.append (
            self.get_image (81, 192, 16, 32))  # Caminando hacia la derecha 1 [1]
        self.right_big_green_frames.append (
            self.get_image (97, 192, 15, 32))  # Caminando hacia la derecha 2 [2]
        self.right_big_green_frames.append (
            self.get_image (113, 192, 15, 32))  # Caminando hacia la derecha 3 [3]
        self.right_big_green_frames.append (
            self.get_image (144, 192, 16, 32))  # Salto a la derecha [4]
        self.right_big_green_frames.append (
            self.get_image (128, 192, 16, 32))  # Skid hacia la derecha [5]
        self.right_big_green_frames.append (
            self.get_image (336, 192, 16, 32))  # Lanzar hacia la derecha [6]
        self.right_big_green_frames.append (
            self.get_image (160, 202, 16, 22))  # Agacharse hacia la derecha [7]

        # Imagenes para personaje principal grande Rojo

        self.right_big_red_frames.append (
            self.get_image (176, 240, 16, 32))  # Mirando hacia la derecha [0]
        self.right_big_red_frames.append (
            self.get_image (81, 240, 16, 32))  # Caminando hacia la derecha 1 [1]
        self.right_big_red_frames.append (
            self.get_image (97, 240, 15, 32))  # Caminando hacia la derecha 2 [2]
        self.right_big_red_frames.append (
            self.get_image (113, 240, 15, 32))  # Caminando hacia la derecha 3 [3]
        self.right_big_red_frames.append (
            self.get_image (144, 240, 16, 32))  # Salto a la derecha [4]
        self.right_big_red_frames.append (
            self.get_image (128, 240, 16, 32))  # Skid hacia la derecha [5]
        self.right_big_red_frames.append (
            self.get_image (336, 240, 16, 32))  # Lanzar hacia la derecha [6]
        self.right_big_red_frames.append (
            self.get_image (160, 250, 16, 22))  # Agacharse hacia la derecha [7]

        # Imagesnes para personaje principal grande Negro

        self.right_big_black_frames.append (
            self.get_image (176, 144, 16, 32))  # Mirando hacia la derecha [0]
        self.right_big_black_frames.append (
            self.get_image (81, 144, 16, 32))  # Caminando hacia la derecha 1 [1]
        self.right_big_black_frames.append (
            self.get_image (97, 144, 15, 32))  # Caminando hacia la derecha 2 [2]
        self.right_big_black_frames.append (
            self.get_image (113, 144, 15, 32))  # Caminando hacia la derecha 3 [3]
        self.right_big_black_frames.append (
            self.get_image (144, 144, 16, 32))  # Salto a la derecha [4]
        self.right_big_black_frames.append (
            self.get_image (128, 144, 16, 32))  # Skid hacia la derecha [5]
        self.right_big_black_frames.append (
            self.get_image (336, 144, 16, 32))  # Lanzar hacia la derecha [6]
        self.right_big_black_frames.append (
            self.get_image (160, 154, 16, 22))  # Agacharse hacia la derecha [7]

        # Imagenes para personaje modo fire

        self.right_fire_frames.append (
            self.get_image (176, 48, 16, 32))  # Mirando hacia la derecha [0]
        self.right_fire_frames.append (
            self.get_image (81, 48, 16, 32))  # Caminando hacia la derecha 1 [1]
        self.right_fire_frames.append (
            self.get_image (97, 48, 15, 32))  # Caminando hacia la derecha 2 [2]
        self.right_fire_frames.append (
            self.get_image (113, 48, 15, 32))  # Caminando hacia la derecha 3 [3]
        self.right_fire_frames.append (
            self.get_image (144, 48, 16, 32))  # Salto a la derecha [4]
        self.right_fire_frames.append (
            self.get_image (128, 48, 16, 32))  # Skid hacia la derecha [5]
        self.right_fire_frames.append (
            self.get_image (336, 48, 16, 32))  # Lanzar hacia la derecha [6]
        self.right_fire_frames.append (
            self.get_image (160, 58, 16, 22))  # Agacharse hacia la derecha [7]
        self.right_fire_frames.append (
            self.get_image (0, 0, 0, 0))
        self.right_fire_frames.append (
            self.get_image (193, 50, 16, 29))  # Frame 1 del flag pole [9]
        self.right_fire_frames.append (
            self.get_image (209, 50, 16, 29))  # Frame 2 del flag pole [9]


        for frame in self.right_small_normal_frames:
            new_image = pygame.transform.flip (frame, True, False)
            self.left_small_normal_frames.append (new_image)

        for frame in self.right_small_green_frames:
            new_image = pygame.transform.flip (frame, True, False)
            self.left_small_green_frames.append (new_image)

        for frame in self.right_small_red_frames:
            new_image = pygame.transform.flip (frame, True, False)
            self.left_small_red_frames.append (new_image)

        for frame in self.right_small_black_frames:
            new_image = pygame.transform.flip (frame, True, False)
            self.left_small_black_frames.append (new_image)

        for frame in self.right_big_normal_frames:
            new_image = pygame.transform.flip (frame, True, False)
            self.left_big_normal_frames.append (new_image)

        for frame in self.right_big_green_frames:
            new_image = pygame.transform.flip (frame, True, False)
            self.left_big_green_frames.append (new_image)

        for frame in self.right_big_red_frames:
            new_image = pygame.transform.flip (frame, True, False)
            self.left_big_red_frames.append (new_image)

        for frame in self.right_big_black_frames:
            new_image = pygame.transform.flip (frame, True, False)
            self.left_big_black_frames.append (new_image)

        for frame in self.right_fire_frames:
            new_image = pygame.transform.flip (frame, True, False)
            self.left_fire_frames.append (new_image)

        self.normal_small_frames = [self.right_small_normal_frames,
                                    self.left_small_normal_frames]

        self.green_small_frames = [self.right_small_green_frames,
                                   self.left_small_green_frames]

        self.red_small_frames = [self.right_small_red_frames,
                                 self.left_small_red_frames]

        self.black_small_frames = [self.right_small_black_frames,
                                   self.left_small_black_frames]

        self.invincible_small_frames_list = [self.normal_small_frames,
                                             self.green_small_frames,
                                             self.red_small_frames,
                                             self.black_small_frames]

        self.normal_big_frames = [self.right_big_normal_frames,
                                  self.left_big_normal_frames]

        self.green_big_frames = [self.right_big_green_frames,
                                 self.left_big_green_frames]

        self.red_big_frames = [self.right_big_red_frames,
                               self.left_big_red_frames]

        self.black_big_frames = [self.right_big_black_frames,
                                 self.left_big_black_frames]

        self.fire_frames = [self.right_fire_frames,
                            self.left_fire_frames]

        self.invincible_big_frames_list = [self.normal_big_frames,
                                           self.green_big_frames,
                                           self.red_big_frames,
                                           self.black_big_frames]

        self.all_images = [self.right_big_normal_frames,
                           self.right_big_black_frames,
                           self.right_big_red_frames,
                           self.right_big_green_frames,
                           self.right_small_normal_frames,
                           self.right_small_green_frames,
                           self.right_small_red_frames,
                           self.right_small_black_frames,
                           self.left_big_normal_frames,
                           self.left_big_black_frames,
                           self.left_big_red_frames,
                           self.left_big_green_frames,
                           self.left_small_normal_frames,
                           self.left_small_red_frames,
                           self.left_small_green_frames,
                           self.left_small_black_frames]

        self.right_frames = self.normal_small_frames[0]
        self.left_frames = self.normal_small_frames[1]

    def get_image(self, x, y, width, height):

        """Extrae la imagen del archivo sprite"""

        image = pygame.Surface ([width, height])
        rect = image.get_rect ()

        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey (constants.BLACK)
        image = pygame.transform.scale (image,
                                    (int (rect.width * constants.SIZE_MULTIPLIER),
                                     int (rect.height * constants.SIZE_MULTIPLIER)))
        return image

    def update(self, keys, game_info, fire_group):

        """Update de los states del personaje principal y tambien las animaciones"""

        self.current_time = game_info[constants.CURRENT_TIME]
        self.handle_state (keys, fire_group)
        self.check_for_special_state ()
        self.animation ()

    def handle_state(self, keys, fire_group):

        """Determina la logica del personaje principal basado en sus states"""

        if self.state == constants.STAND:
            self.standing (keys, fire_group)
        elif self.state == constants.WALK:
            self.walking (keys, fire_group)
        elif self.state == constants.JUMP:
            self.jumping (keys, fire_group)
        elif self.state == constants.FALL:
            self.falling (keys, fire_group)
        elif self.state == constants.DEATH_JUMP:
            self.jumping_to_death ()
        elif self.state == constants.SMALL_TO_BIG:
            self.changing_to_big ()
        elif self.state == constants.BIG_TO_FIRE:
            self.changing_to_fire ()
        elif self.state == constants.BIG_TO_SMALL:
            self.changing_to_small ()
        elif self.state == constants.FLAGPOLE:
            self.flag_pole_sliding ()
        elif self.state == constants.BOTTOM_OF_POLE:
            self.sitting_at_bottom_of_pole ()
        elif self.state == constants.WALKING_TO_CASTLE:
            self.walking_to_castle ()
        elif self.state == constants.END_OF_LEVEL_FALL:
            self.falling_at_end_of_level ()

    def standing(self, keys, fire_group):

        """Logica del personaje principal cuando esta estatico"""

        self.check_to_allow_jump (keys)
        self.check_to_allow_fireball (keys)

        self.frame_index = 0
        self.x_vel = 0
        self.y_vel = 0

        if keys[means.keybinding['action']]:
            if self.fire and self.allow_fireball:
                self.shoot_fireball (fire_group)

        if keys[means.keybinding['down']]:
            self.crouching = True

        if keys[means.keybinding['left']]:
            self.facing_right = False
            self.get_out_of_crouch ()
            self.state = constants.WALK
        elif keys[means.keybinding['right']]:
            self.facing_right = True
            self.get_out_of_crouch ()
            self.state = constants.WALK
        elif keys[means.keybinding['jump']]:
            if self.allow_jump:
                if self.big:
                    setup.SFX['big_jump'].play ()
                else:
                    setup.SFX['small_jump'].play ()
                self.state = constants.JUMP
                self.y_vel = constants.JUMP_SPEED
        else:
            self.state = constants.STAND

        if not keys[means.keybinding['down']]:
            self.get_out_of_crouch ()

    def get_out_of_crouch(self):

        """Salir del state crouch (agachado)"""

        bottom = self.rect.bottom
        left = self.rect.x
        if self.facing_right:
            self.image = self.right_frames[0]
        else:
            self.image = self.left_frames[0]
        self.rect = self.image.get_rect ()
        self.rect.bottom = bottom
        self.rect.x = left
        self.crouching = False

    def check_to_allow_jump(self, keys):

        """Confirmar para que el personaje principal salte"""

        if not keys[means.keybinding['jump']]:
            self.allow_jump = True

    def check_to_allow_fireball(self, keys):

        """Confirmar para que el personaje principal dispare"""

        if not keys[means.keybinding['action']]:
            self.allow_fireball = True

    def shoot_fireball(self, powerup_group):

        """Logica para disparar los proyectiles"""

        setup.SFX['fireball'].play ()
        self.fireball_count = self.count_number_of_fireballs (powerup_group)

        if (self.current_time - self.last_fireball_time) > 200:
            if self.fireball_count < 2:
                self.allow_fireball = False
                powerup_group.add (
                    powerups.FireBall (self.rect.right, self.rect.y, self.facing_right))
                self.last_fireball_time = self.current_time

                self.frame_index = 6
                if self.facing_right:
                    self.image = self.right_frames[self.frame_index]
                else:
                    self.image = self.left_frames[self.frame_index]

    def count_number_of_fireballs(self, powerup_group):

        """Contar el numero de proyectiles disparados en el nivel """

        fireball_list = []

        for powerup in powerup_group:
            if powerup.name == constants.FIREBALL:
                fireball_list.append (powerup)

        return len (fireball_list)

    def walking(self, keys, fire_group):

        """Funcion que define el state de caminar, se encarga de toda la logica necesaria"""

        self.check_to_allow_jump (keys)
        self.check_to_allow_fireball (keys)

        if self.frame_index == 0:
            self.frame_index += 1
            self.walking_timer = self.current_time
        else:
            if (self.current_time - self.walking_timer >
                    self.calculate_animation_speed ()):
                if self.frame_index < 3:
                    self.frame_index += 1
                else:
                    self.frame_index = 1

                self.walking_timer = self.current_time

        if keys[means.keybinding['action']]:
            self.max_x_vel = constants.MAX_RUN_SPEED
            self.x_accel = constants.RUN_ACC
            if self.fire and self.allow_fireball:
                self.shoot_fireball (fire_group)
        else:
            self.max_x_vel = constants.MAX_WALK_SPEED
            self.x_accel = constants.WALK_ACC

        if keys[means.keybinding['jump']]:
            if self.allow_jump:
                if self.big:
                    setup.SFX['big_jump'].play ()
                else:
                    setup.SFX['small_jump'].play ()
                self.state = constants.JUMP
                if self.x_vel > 4.5 or self.x_vel < -4.5:
                    self.y_vel = constants.JUMP_SPEED - .5
                else:
                    self.y_vel = constants.JUMP_SPEED

        if keys[means.keybinding['left']]:
            self.get_out_of_crouch ()
            self.facing_right = False
            if self.x_vel > 0:
                self.frame_index = 5
                self.x_accel = constants.TURNAROUND
            else:
                self.x_accel = constants.WALK_ACC

            if self.x_vel > (self.max_x_vel * -1):
                self.x_vel -= self.x_accel
                if self.x_vel > -0.5:
                    self.x_vel = -0.5
            elif self.x_vel < (self.max_x_vel * -1):
                self.x_vel += self.x_accel

        elif keys[means.keybinding['right']]:
            self.get_out_of_crouch ()
            self.facing_right = True
            if self.x_vel < 0:
                self.frame_index = 5
                self.x_accel = constants.TURNAROUND
            else:
                self.x_accel = constants.WALK_ACC

            if self.x_vel < self.max_x_vel:
                self.x_vel += self.x_accel
                if self.x_vel < 0.5:
                    self.x_vel = 0.5
            elif self.x_vel > self.max_x_vel:
                self.x_vel -= self.x_accel

        else:
            if self.facing_right:
                if self.x_vel > 0:
                    self.x_vel -= self.x_accel
                else:
                    self.x_vel = 0
                    self.state = constants.STAND
            else:
                if self.x_vel < 0:
                    self.x_vel += self.x_accel
                else:
                    self.x_vel = 0
                    self.state = constants.STAND

    def calculate_animation_speed(self):

        """Metodo para que relacionar la velocidad de mario con su velocidad en el eje x"""

        if self.x_vel == 0:
            animation_speed = 130
        elif self.x_vel > 0:
            animation_speed = 130 - (self.x_vel * (13))
        else:
            animation_speed = 130 - (self.x_vel * (13) * -1)

        return animation_speed

    def jumping(self, keys, fire_group):

        """Metodo que contiene la logica del state Jump."""

        self.allow_jump = False
        self.frame_index = 4
        self.gravity = constants.JUMP_GRAVITY
        self.y_vel += self.gravity
        self.check_to_allow_fireball (keys)

        if self.y_vel >= 0 and self.y_vel < self.max_y_vel:
            self.gravity = constants.GRAVITY
            self.state = constants.FALL

        if keys[means.keybinding['left']]:
            if self.x_vel > (self.max_x_vel * - 1):
                self.x_vel -= self.x_accel

        elif keys[means.keybinding['right']]:
            if self.x_vel < self.max_x_vel:
                self.x_vel += self.x_accel

        if not keys[means.keybinding['jump']]:
            self.gravity = constants.GRAVITY
            self.state = constants.FALL

        if keys[means.keybinding['action']]:
            if self.fire and self.allow_fireball:
                self.shoot_fireball (fire_group)

    def falling(self, keys, fire_group):

        """Metodo que contiene la logica del state Fall"""

        self.check_to_allow_fireball (keys)
        if self.y_vel < constants.MAX_Y_SPEED:
            self.y_vel += self.gravity

        if keys[means.keybinding['left']]:
            if self.x_vel > (self.max_x_vel * - 1):
                self.x_vel -= self.x_accel

        elif keys[means.keybinding['right']]:
            if self.x_vel < self.max_x_vel:
                self.x_vel += self.x_accel

        if keys[means.keybinding['action']]:
            if self.fire and self.allow_fireball:
                self.shoot_fireball (fire_group)

    def jumping_to_death(self):

        """Metodo que contiene la logica del state Fall Death"""

        if self.death_timer == 0:
            self.death_timer = self.current_time
        elif (self.current_time - self.death_timer) > 500:
            self.rect.y += self.y_vel
            self.y_vel += self.gravity

    def start_death_jump(self, game_info):

        self.dead = True
        game_info[constants.CHAR_DEAD] = True
        self.y_vel = -11
        self.gravity = .5
        self.frame_index = 6
        self.image = self.right_frames[self.frame_index]
        self.state = constants.DEATH_JUMP
        self.in_transition_state = True

    def changing_to_big(self):

        """Cambia la imagen del personaje principal a una grande"""

        self.in_transition_state = True

        if self.transition_timer == 0:
            self.transition_timer = self.current_time
        elif self.timer_between_these_two_times (135, 200):
            self.set_char_to_middle_image ()
        elif self.timer_between_these_two_times (200, 365):
            self.set_char_to_small_image ()
        elif self.timer_between_these_two_times (365, 430):
            self.set_char_to_middle_image ()
        elif self.timer_between_these_two_times (430, 495):
            self.set_char_to_small_image ()
        elif self.timer_between_these_two_times (495, 560):
            self.set_char_to_middle_image ()
        elif self.timer_between_these_two_times (560, 625):
            self.set_char_to_big_image ()
        elif self.timer_between_these_two_times (625, 690):
            self.set_char_to_small_image ()
        elif self.timer_between_these_two_times (690, 755):
            self.set_char_to_middle_image ()
        elif self.timer_between_these_two_times (755, 820):
            self.set_char_to_big_image ()
        elif self.timer_between_these_two_times (820, 885):
            self.set_char_to_small_image ()
        elif self.timer_between_these_two_times (885, 950):
            self.set_char_to_big_image ()
            self.state = constants.WALK
            self.in_transition_state = False
            self.transition_timer = 0
            self.become_big ()

    def timer_between_these_two_times(self, start_time, end_time):

        """Mejora 1 (Mide el tiempo entre states)."""

        if (self.current_time - self.transition_timer) >= start_time \
                and (self.current_time - self.transition_timer) < end_time:
            return True

    def set_char_to_middle_image(self):

        """Cambia la imagen del personaje principal a una intermedia"""

        if self.facing_right:
            self.image = self.normal_small_frames[0][7]
        else:
            self.image = self.normal_small_frames[1][7]
        bottom = self.rect.bottom
        centerx = self.rect.centerx
        self.rect = self.image.get_rect ()
        self.rect.bottom = bottom
        self.rect.centerx = centerx

    def set_char_to_small_image(self):

        """DCambia la imagen del personaje principal a una chica"""

        if self.facing_right:
            self.image = self.normal_small_frames[0][0]
        else:
            self.image = self.normal_small_frames[1][0]
        bottom = self.rect.bottom
        centerx = self.rect.centerx
        self.rect = self.image.get_rect ()
        self.rect.bottom = bottom
        self.rect.centerx = centerx

    def set_char_to_big_image(self):

        """Imagen del personaje grande"""

        if self.facing_right:
            self.image = self.normal_big_frames[0][0]
        else:
            self.image = self.normal_big_frames[1][0]
        bottom = self.rect.bottom
        centerx = self.rect.centerx
        self.rect = self.image.get_rect()
        self.rect.bottom = bottom
        self.rect.centerx = centerx

    def become_big(self):

        self.big = True
        self.right_frames = self.right_big_normal_frames
        self.left_frames = self.left_big_normal_frames
        bottom = self.rect.bottom
        left = self.rect.x
        image = self.right_frames[0]
        self.rect = image.get_rect ()
        self.rect.bottom = bottom
        self.rect.x = left

    def changing_to_fire(self):

        """Metodo que contiene la logica para cambiar al modo fire"""

        self.in_transition_state = True

        if self.facing_right:
            frames = [self.right_fire_frames[3],
                      self.right_big_green_frames[3],
                      self.right_big_red_frames[3],
                      self.right_big_black_frames[3]]
        else:
            frames = [self.left_fire_frames[3],
                      self.left_big_green_frames[3],
                      self.left_big_red_frames[3],
                      self.left_big_black_frames[3]]

        if self.fire_transition_timer == 0:
            self.fire_transition_timer = self.current_time
        elif (self.current_time - self.fire_transition_timer) > 65 and (
                self.current_time - self.fire_transition_timer) < 130:
            self.image = frames[0]
        elif (self.current_time - self.fire_transition_timer) < 195:
            self.image = frames[1]
        elif (self.current_time - self.fire_transition_timer) < 260:
            self.image = frames[2]
        elif (self.current_time - self.fire_transition_timer) < 325:
            self.image = frames[3]
        elif (self.current_time - self.fire_transition_timer) < 390:
            self.image = frames[0]
        elif (self.current_time - self.fire_transition_timer) < 455:
            self.image = frames[1]
        elif (self.current_time - self.fire_transition_timer) < 520:
            self.image = frames[2]
        elif (self.current_time - self.fire_transition_timer) < 585:
            self.image = frames[3]
        elif (self.current_time - self.fire_transition_timer) < 650:
            self.image = frames[0]
        elif (self.current_time - self.fire_transition_timer) < 715:
            self.image = frames[1]
        elif (self.current_time - self.fire_transition_timer) < 780:
            self.image = frames[2]
        elif (self.current_time - self.fire_transition_timer) < 845:
            self.image = frames[3]
        elif (self.current_time - self.fire_transition_timer) < 910:
            self.image = frames[0]
        elif (self.current_time - self.fire_transition_timer) < 975:
            self.image = frames[1]
        elif (self.current_time - self.fire_transition_timer) < 1040:
            self.image = frames[2]
            self.fire = True
            self.in_transition_state = False
            self.state = constants.WALK
            self.transition_timer = 0

    def changing_to_small(self):

        """Animacion que cambia al personaje principal luego de colisionar con un enemigo"""

        self.in_transition_state = True
        self.hurt_invincible = True
        self.state = constants.BIG_TO_SMALL

        if self.facing_right:
            frames = [self.right_big_normal_frames[4],
                      self.right_big_normal_frames[8],
                      self.right_small_normal_frames[8]
                      ]
        else:
            frames = [self.left_big_normal_frames[4],
                      self.left_big_normal_frames[8],
                      self.left_small_normal_frames[8]
                      ]

        if self.transition_timer == 0:
            self.transition_timer = self.current_time
        elif (self.current_time - self.transition_timer) < 265:
            self.image = frames[0]
            self.hurt_invincible_check()
            self.adjust_rect()
        elif (self.current_time - self.transition_timer) < 330:
            self.image = frames[1]
            self.hurt_invincible_check()
            self.adjust_rect()
        elif (self.current_time - self.transition_timer) < 395:
            self.image = frames[2]
            self.hurt_invincible_check()
            self.adjust_rect()
        elif (self.current_time - self.transition_timer) < 460:
            self.image = frames[1]
            self.hurt_invincible_check()
            self.adjust_rect()
        elif (self.current_time - self.transition_timer) < 525:
            self.image = frames[2]
            self.hurt_invincible_check()
            self.adjust_rect()
        elif (self.current_time - self.transition_timer) < 590:
            self.image = frames[1]
            self.hurt_invincible_check()
            self.adjust_rect()
        elif (self.current_time - self.transition_timer) < 655:
            self.image = frames[2]
            self.hurt_invincible_check()
            self.adjust_rect()
        elif (self.current_time - self.transition_timer) < 720:
            self.image = frames[1]
            self.hurt_invincible_check()
            self.adjust_rect()
        elif (self.current_time - self.transition_timer) < 785:
            self.image = frames[2]
            self.hurt_invincible_check()
            self.adjust_rect()
        elif (self.current_time - self.transition_timer) < 850:
            self.image = frames[1]
            self.hurt_invincible_check()
            self.adjust_rect()
        elif (self.current_time - self.transition_timer) < 915:
            self.image = frames[2]
            self.adjust_rect()
            self.in_transition_state = False
            self.state = constants.WALK
            self.big = False
            self.transition_timer = 0
            self.hurt_invisible_timer = 0
            self.become_small()

    def adjust_rect(self):

        x = self.rect.x
        bottom = self.rect.bottom
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.bottom = bottom

    def become_small(self):

        self.big = False
        self.right_frames = self.right_small_normal_frames
        self.left_frames = self.left_small_normal_frames
        bottom = self.rect.bottom
        left = self.rect.x
        image = self.right_frames[0]
        self.rect = image.get_rect()
        self.rect.bottom = bottom
        self.rect.x = left

    def flag_pole_sliding(self):

        """State en el que el personaje principal esta bajando por el pole"""

        self.state = constants.FLAGPOLE
        self.in_transition_state = True
        self.x_vel = 0
        self.y_vel = 0

        if self.flag_pole_timer == 0:
            self.flag_pole_timer = self.current_time
        elif self.rect.bottom < 493:
            if (self.current_time - self.flag_pole_timer) < 65:
                self.image = self.right_frames[9]
            elif (self.current_time - self.flag_pole_timer) < 130:
                self.image = self.right_frames[10]
            elif (self.current_time - self.flag_pole_timer) >= 130:
                self.flag_pole_timer = self.current_time

            self.rect.right = self.flag_pole_right
            self.y_vel = 5
            self.rect.y += self.y_vel

            if self.rect.bottom >= 488:
                self.flag_pole_timer = self.current_time

        elif self.rect.bottom >= 493:
            self.image = self.right_frames[10]

    def sitting_at_bottom_of_pole(self):

        """State cuando el personaje principal esta en la parte inferior del pole"""

        if self.flag_pole_timer == 0:
            self.flag_pole_timer = self.current_time
            self.image = self.left_frames[10]
        elif (self.current_time - self.flag_pole_timer) < 210:
            self.image = self.left_frames[10]
        else:
            self.in_transition_state = False
            if self.rect.bottom < 485:
                self.state = constants.END_OF_LEVEL_FALL
            else:
                self.state = constants.WALKING_TO_CASTLE

    def set_state_to_bottom_of_pole(self):

        """Configura al personaje principal en el state BOTTOM_OF_POLE"""

        self.image = self.left_frames[9]
        right = self.rect.right
        # self.rect.bottom = 493
        self.rect.x = right
        if self.big:
            self.rect.x -= 10
        self.flag_pole_timer = 0
        self.state = constants.BOTTOM_OF_POLE

    def walking_to_castle(self):

        """State cuando el personaje principal esta llegando a la meta (castillo)"""

        self.max_x_vel = 5
        self.x_accel = constants.WALK_ACC

        if self.x_vel < self.max_x_vel:
            self.x_vel += self.x_accel

        if (self.walking_timer == 0 or (self.current_time - self.walking_timer) > 200):
            self.walking_timer = self.current_time

        elif (self.current_time - self.walking_timer) > \
                self.calculate_animation_speed():
            if self.frame_index < 3:
                self.frame_index += 1
            else:
                self.frame_index = 1
            self.walking_timer = self.current_time

    def falling_at_end_of_level(self, *args):

        """State al final de los niveles (cuando esta bajando del pole) """

        self.y_vel += constants.GRAVITY

    def check_for_special_state(self):

        """Determina en que estado se encuentra el personaje principal"""

        self.check_if_invincible()
        self.check_if_fire()
        self.check_if_hurt_invincible()
        self.check_if_crouching()

    def check_if_invincible(self):

        if self.invincible:
            if ((self.current_time - self.invincible_start_timer) < 10000):
                self.losing_invincibility = False
                self.change_frame_list(30)
            elif ((self.current_time - self.invincible_start_timer) < 12000):
                self.losing_invincibility = True
                self.change_frame_list(100)
            else:
                self.losing_invincibility = False
                self.invincible = False
        else:
            if self.big:
                self.right_frames = self.right_big_normal_frames
                self.left_frames = self.left_big_normal_frames
            else:
                self.right_frames = self.invincible_small_frames_list[0][0]
                self.left_frames = self.invincible_small_frames_list[0][1]

    def change_frame_list(self, frame_switch_speed):

        if (self.current_time - self.invincible_animation_timer) > frame_switch_speed:
            if self.invincible_index < (len(self.invincible_small_frames_list) - 1):
                self.invincible_index += 1
            else:
                self.invincible_index = 0

            if self.big:
                frames = self.invincible_big_frames_list[self.invincible_index]
            else:
                frames = self.invincible_small_frames_list[self.invincible_index]

            self.right_frames = frames[0]
            self.left_frames = frames[1]

            self.invincible_animation_timer = self.current_time

    def check_if_fire(self):

        if self.fire and self.invincible == False:
            self.right_frames = self.fire_frames[0]
            self.left_frames = self.fire_frames[1]

    def check_if_hurt_invincible(self):

        """Metodo para verificar la logica del modo invensible"""

        if self.hurt_invincible and self.state != constants.BIG_TO_SMALL:
            if self.hurt_invisible_timer2 == 0:
                self.hurt_invisible_timer2 = self.current_time
            elif (self.current_time - self.hurt_invisible_timer2) < 2000:
                self.hurt_invincible_check ()
            else:
                self.hurt_invincible = False
                self.hurt_invisible_timer = 0
                self.hurt_invisible_timer2 = 0
                for frames in self.all_images:
                    for image in frames:
                        image.set_alpha(255)

    def hurt_invincible_check(self):

        """Metodo para convertir al personaje principal invensible"""

        if self.hurt_invisible_timer == 0:
            self.hurt_invisible_timer = self.current_time
        elif (self.current_time - self.hurt_invisible_timer) < 35:
            self.image.set_alpha (0)
        elif (self.current_time - self.hurt_invisible_timer) < 70:
            self.image.set_alpha (255)
            self.hurt_invisible_timer = self.current_time

    def check_if_crouching(self):

        """Verificar si el personaje principal esta agachado"""

        if self.crouching and self.big:
            bottom = self.rect.bottom
            left = self.rect.x
            if self.facing_right:
                self.image = self.right_frames[7]
            else:
                self.image = self.left_frames[7]
            self.rect = self.image.get_rect()
            self.rect.bottom = bottom
            self.rect.x = left

    def animation(self):

        """Modifica la imagen del personaje principal para las animaciones"""

        if self.state == constants.DEATH_JUMP \
                or self.state == constants.SMALL_TO_BIG \
                or self.state == constants.BIG_TO_FIRE \
                or self.state == constants.BIG_TO_SMALL \
                or self.state == constants.FLAGPOLE \
                or self.state == constants.BOTTOM_OF_POLE \
                or self.crouching:
            pass
        elif self.facing_right:
            self.image = self.right_frames[self.frame_index]
        else:
            self.image = self.left_frames[self.frame_index]
